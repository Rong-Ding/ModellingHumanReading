## Assignment 2
The current project aims at comparing SRN vs LSTM in characterising the statistical structure of language and syntactic ambiguity (garden-path sentences)
- Training: SRN vs LSTM models on a large English corpus with 8.7 billion words; _training data size_ varied
- Testing: The models' ability to characterise language statistics (_perplexity_) and predict human performance (_sensitivity to syntactic ambiguity_)
- Findings:
  - With big training sizes, SRN and LSTM give almost equally low perplexity, meaning that they both capture well the statistical structure of language.
  - However, LSTMs show higher sensitivity to syntactically ambiguous sentences than SRNs do.
  - Characterising linguistic statistics well, therefore, does not necessarily indicate good prediction of human sentence processing.

## Explanation per file:

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
