This repository contains scripts and reports for the two projects (Assignments 1 and 2) of the graduate course Computational Psycholinguistics at Radboud University. Both projects are Python-based, with the goal of training models to simulate and interpret human reading data. Statistical testing, in most cases here linear mixed-effect models, is performed in R.

In the first project (Assignment 1), collaborating with one other fellow student, I trained Word2Vec models on a large English corpus (ENCOW), varying parameters _size_ and _window_. The aim was to test the Word2Vec model's ability to predict humans' word categorisation, naming and reading time. Findings show that distributional word
vectors from Word2Vec capture well the semantic properties of words from human data.

In the second project (Assignment 2), I trained simple and gated recurrent neural networks, namely SRN and long-short-term memory (LSTM), on a large English language corpus containing more than 8.7 million words, and tested 1) how well they captured the statistical structure of language, as well as 2) how well they predicted human reading performance. Results show that gated recurrent neural networks such as LSTM generally performed better in characterising the statistical structure of language and also the reading performance in humans.

## Explanation
The repository consists of two subfolders, containing the scripts and a resulting report for each project respectively. 

### Assignment 1:

<b>word2vec_training_finalised.ipynb:</b>\
This script implements the training Word2Vec models of various parameter sets (of size and window).

<b>Data preprocessing.ipynb:</b>\
This script preprocesses raw human data and transforms outputs of the trained Word2Vec models for stats analyses.

<b>anova_cosine.R:</b>\
This script statistically compares the ANOVA model fit (across semantically highly and lowly correlated and uncorrelated words) over different parameter sets.

<b>lme_priming_cosine.R:</b>\
This script computes and statistically compares the linear mixed-effect model fit (across different semantic correlation and inter-stimulus intervals) over different parameter sets.

### Assignment 2:

<b>Datafile_building_Part1.ipynb & Datafile_building_Part2.ipynb:</b>\
These scripts transform outputs of the trained SRN and LSTM models for stats analyses.

<b>Test set selection.ipynb & Sentence selection_Part 2.ipynb:</b>\
These scripts select test sets by filtering whether a sentence stimulus contains any vocabulary that is not in the trained models.

<b>GoodnessofFit_Plotting.ipynb & Perplexity computation & plotting.ipynb:</b>\
Result plotting for the report, characterising the model fit of the statistical structure of language.

<b>rt_surp_LMER.R:</b>\
This script conducts linear mixed-effects models on human reading pace data, including measures generated from trained recurrent models as a predictor and other variables as control.

<b>surp_amb_fit_LMER.R:</b>\
This script conducts two-way ANOVAs on the models' prediction on reading performance.
