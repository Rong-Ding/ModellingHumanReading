#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import sys
import numpy as np
import pandas as pd
import os

modeltype  = "lstm"                     # The type of RNN: "srn" for Simple Recurrent Network, or "lstm" for Long Short-Term Memory network
items_file = "amb_good_fit.txt"         # Name of the file with test sentences
home_dir   = "C:\\Users\\rondin\\Desktop\\Courses\\Computational Psycholinguistics\\Assignment\\Assignment 2" 
model_dir  = home_dir + '/trained_models/'
items_dir  = home_dir + '/items/'

# RNN used for next word prediction
class nwp_rnn_encoder(nn.Module):
    def __init__(self, config):
        super(nwp_rnn_encoder, self).__init__()
        embed = config['embed']
        rnn = config['rnn']
        lin = config['lin']

        self.max_len = config['max_len']
        
        self.embed = nn.Embedding(num_embeddings = embed['n_embeddings'], 
                                  embedding_dim = embed['embedding_dim'], 
                                  sparse = embed['sparse'],
                                  padding_idx = embed['padding_idx'])

        if rnn['type'].lower() == 'srn':
            self.RNN = nn.RNN(input_size = rnn['in_size'], 
                          hidden_size = rnn['hidden_size'], 
                          num_layers = rnn['n_layers'],
                          batch_first = rnn['batch_first'],
                          bidirectional = rnn['bidirectional'], 
                          dropout = rnn['dropout'])
        if rnn['type'].lower() == 'lstm':
            self.RNN = nn.LSTM(input_size = rnn['in_size'], 
                          hidden_size = rnn['hidden_size'], 
                          num_layers = rnn['n_layers'],
                          batch_first = rnn['batch_first'],
                          bidirectional = rnn['bidirectional'], 
                          dropout = rnn['dropout'])

        self.linear = nn.Sequential(nn.Linear(rnn['hidden_size'], 
                                              lin['hidden_size']
                                              ), 
                                    nn.Tanh(), 
                                    nn.Linear(lin['hidden_size'],
                                              embed['n_embeddings']
                                              )
                                    )

    def forward(self, input, sent_lens):
        targs      = nn.functional.pad(input[:,1:], [0,1]).long()    # create the targets by shifting the input left
        embeddings = self.embed(input.long())

        x       = nn.utils.rnn.pack_padded_sequence(embeddings, sent_lens, batch_first = True, enforce_sorted = False)
        x, hx   = self.RNN(x)
        x, lens = nn.utils.rnn.pad_packed_sequence(x, batch_first = True)

        out = self.linear(x)  
        
        return out, targs

# load the vocabulary and store as dictionary and reverse dictionary. It turned out that
# for network training, word indices start at 1, not 0. The 0 is used for sentence paddding. 
with open(home_dir+"/vocabulary.txt") as f:
    vocab = f.read().split()
vocab_dict    = dict(zip(vocab, range(1,len(vocab)+1)))       # word -> index dictionary
vocab_revdict = dict(zip(range(1,len(vocab)+1), vocab))       # index -> word dictionary
vocab_revdict[0] = 0

# Function that turns a list of sentences-as-word-indices into a list of sentences-as-words
def index_2_word(indices, vocab_revdict):
    sentences = [[vocab_revdict[int(i)] for i in ind] for ind in indices]   
    return(sentences)

# Function that turns a list of sentences-as-words into a list of sentences-as-word-indices.
# Sentences that are shorter than the longest sentences are padded with 0s for efficient 
# processing by torch.
def word_2_index(sentences, vocab_dict):
    index_sents_list = [[vocab_dict[word] for word in sent] for sent in sentences]
    lengths = [len(sent) for sent in sentences]
    max_len = max(lengths)
    index_sents_array = np.zeros([len(sentences), max_len])
    for idx, sent in enumerate(index_sents_list):
        index_sents_array[idx][:lengths[idx]] = sent
    return index_sents_array, lengths

# Function to get surprisal values for the test sentences
def calc_surprisal(items_loc, model):
    surprisal = []
    sents     = []
    
    with open(items_loc) as file:
        for line in file:
            sents.append(['<s>'] + line.split() + ['</s>'])              # split the sentence into words and add sentence-start and -end symbols
    
    sents, lengths   = word_2_index(sents, vocab_dict)
    outputs, targets = model(torch.FloatTensor(sents), lengths)          # get the outputs and targets for these sentences
    
    surprisal = -torch.log_softmax(outputs, dim = 2).squeeze()           # convert the outputs into surprisal
    surprisal = surprisal.gather(-1, targets.unsqueeze(-1))            # extract only the surpisal ratings for the target words
    surprisal = np.array(surprisal.data.numpy())                         
    surprisal = [s[:l-2] for s, l in zip(surprisal, lengths)]            # remove any padding applied by word_2_index and remove end-of-sentence prediction
    return(surprisal, targets)

# config settings for the models
rnn_config = {'embed':{'n_embeddings': len(vocab_dict)+1, 'embedding_dim': 300, 
                       'sparse': False, 'padding_idx': 0
                       }, 
                      'max_len': 52,
                      'rnn':{'in_size': 300, 'hidden_size': 600, 
                             'n_layers': 1, 'batch_first': True,
                             'bidirectional': False, 'dropout': 0,
                             'type': modeltype
                             }, 
                      'lin':{'hidden_size': 300
                             }, 
                      'cuda': False
              }

rnn = nwp_rnn_encoder(rnn_config)

###############################################################################

data = pd.DataFrame()

# list all the trained models of the current model type
model_dir_content = [x for x in os.walk(model_dir)][0][2]
model_list = [os.path.join(model_dir, x) for x in model_dir_content if x.startswith(modeltype.upper())]

for model_loc in model_list:
    print(model_loc)
    model = torch.load(model_loc, map_location = 'cpu')         # load the trained model
    rnn.load_state_dict(model)
    rnn.eval()

    # set requires_grad to false for faster encoding
    for param in rnn.parameters():
        param.requires_grad = False
    
    surps, targets = calc_surprisal(items_dir+items_file, rnn)  # get all the surprisal values and the target sequence
    targets        = index_2_word(targets, vocab_revdict)       # convert the target indices back to words
    
    # add sentence and word position indices to the surprisal ratings and convert to DataFrame object
    surprisal = [(sent_index, word_index, targets[sent_index][word_index], surp[0]) for sent_index, sent in enumerate(surps) for word_index, surp in enumerate(sent)]
    surprisal = pd.DataFrame(np.array(surprisal))
    surp_name = model_loc.split('/')[-1]        # create a unique name for the current surprisal values
    surprisal.columns = ['sent_nr', 'word_pos', 'word', surp_name]
    
    # Add unique item number for each word token, for merging current surprisals with data set
    item_nr = []
    for x, y in zip(surprisal.sent_nr, surprisal.word_pos):    
        item_nr.append(100*int(x)+int(y))
    surprisal['item'] = pd.Series(item_nr)
    if not data.empty:
        data[surp_name] = data.join(surprisal[[surp_name, 'item']].set_index('item'), on = 'item')[surp_name]
    else:
        data = surprisal

###############################################################################
# now drop the 'item' column and sort the column names 
data = data.drop(['item'],1)

col_names = data.columns.tolist()
models    = col_names[3:]
nrtrain   = [int(m.split('_')[-1]) for m in models]
order     = np.argsort(nrtrain)
models    = [models[i] for i in order]
col_names = col_names[:3] + models
data      = data[col_names]

# round the surprisal to 4 decimals and convert the sent_nr and word_pos from float to int
data[models]  = data[models].round(4)
data.sent_nr  = data.sent_nr.astype(int)
data.word_pos = data.word_pos.astype(int)

data.to_csv(index = False, path_or_buf = home_dir + '/surprisal.' + modeltype + '.' + items_file.split('.')[0] + '.csv')