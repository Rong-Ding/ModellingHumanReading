## Assignment 1
The current project aims to examine how well semantic models, that is _Word2Vec_, handle word semantics
- Training: CBOW Word2Vec models on a large English corpus (ENCOW) with 16 billion words; _hidden layer size_ and _context window_ varied
- Testing: The models' ability to predict humans' semantics-based word processing (categorisation and semantic priming)
- Findings:
  - Distributional word vectors from Word2Vec generally capture well word semantics used by humans.
  - The bigger the hidden layer size, the better a Word2Vec model predicts human word processing.
  - However, models with a smaller context window size tend to predict human behaviour better, indicating limited working memory capacity in word processing

## Explanation per file

<b>word2vec_training_finalised.ipynb:</b>\
This script implements the training Word2Vec models of various parameter sets (of vector size and window).

<b>Data preprocessing.ipynb:</b>\
This script preprocesses raw human data and transforms outputs of the trained Word2Vec models for stats analyses.

<b>anova_cosine.R:</b>\
This script statistically compares the ANOVA model fit (across semantically highly and lowly correlated and uncorrelated words) over different parameter sets.

<b>lme_priming_cosine.R:</b>\
This script computes and statistically compares the linear mixed-effect model fit (across different semantic correlation and inter-stimulus intervals) over different parameter sets.
