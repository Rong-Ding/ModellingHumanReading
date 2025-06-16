
Statistical testing is performed in R.

## Explanation per file

<b>word2vec_training_finalised.ipynb:</b>\
This script implements the training Word2Vec models of various parameter sets (of vector size and window).

<b>Data preprocessing.ipynb:</b>\
This script preprocesses raw human data and transforms outputs of the trained Word2Vec models for stats analyses.

<b>anova_cosine.R:</b>\
This script statistically compares the ANOVA model fit (across semantically highly and lowly correlated and uncorrelated words) over different parameter sets.

<b>lme_priming_cosine.R:</b>\
This script computes and statistically compares the linear mixed-effect model fit (across different semantic correlation and inter-stimulus intervals) over different parameter sets.
