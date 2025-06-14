#----------------------Library Declarations--------------------------####

library(tidyverse)
library(ggpubr)
library(rstatix)
library(lme4)
library(arm)
library(lattice)
library(effects)
library(sjPlot)
library(piecewiseSEM)
library(glmmTMB)
library(lmtest)

# Download a package if it's not installed yet
if (!require(package, character.only=T, quietly=T)) {
  install.packages(package)
  library(package, character.only = T)
}
#---------------------------------------------------------------------###
#----------------------Parameters------------------------------------####

# alter the directory and the datafile name here
directory = 'C:/Users/rondin/Desktop/Courses/Computational Psycholinguistics/Assignment/Assignment 2'
filename = 'data_LSTM_1000.csv'

#---------------------------------------------------------------------###
#----------------------Data Prep-------------------------------------####

setwd(directory)
data <- read.csv(file = filename)

# double-check data format
tail(data)

# mark categorical variables
data$subj_nr = as.factor(data$subj_nr)
data$sent_nr = as.factor(data$sent_nr)
data$word_pos = as.factor(data$word_pos)
data$sent_pos = as.factor(data$sent_pos)
data$word = as.factor(data$word)
#---------------------------------------------------------------------###
#----------------------Model Implementation--------------------------####
# control model: w/o surprisal
lme.control <- lmerTest::lmer(RT ~ word_freq + wordLen 
                                + (1 | subj_nr) + (1 | word_pos) + (1 | sent_nr) + (1 | sent_pos) + (1 | word),
                                data = data)
summary(lme.control)

# full model: with surprisal
lme.full <- lmerTest::lmer(RT ~ surprisal + surprisal_.1 + surprisal_.2 # target variables
                              + word_freq + wordLen # control variables
                              + (1 | subj_nr) + (1 | word_pos) + (1 | sent_nr) + (1 | sent_pos) + (1 | word), # random structure
                              data = data)
summary(lme.full)

lrtest(lme.control, lme.full)
