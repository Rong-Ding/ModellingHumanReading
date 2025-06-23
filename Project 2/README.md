## Project 2
The current project aims at comparing SRN vs LSTM in characterising the statistical structure of language and syntactic ambiguity (garden-path sentences)
- Training: SRN vs LSTM models on a large English corpus with 8.7 billion words; _training data size_ varied
- Testing: The models' ability to characterise language statistics (_perplexity_) (**Part 1**) and predict human performance (_sensitivity to syntactic ambiguity_) (**Part 2**)
- Findings:
  - With big training sizes, SRN and LSTM give almost equally low perplexity, meaning that they both capture well the statistical structure of language.
  - However, LSTMs show higher sensitivity to syntactically ambiguous sentences than SRNs do.
  - Characterising linguistic statistics well, therefore, does not necessarily indicate good prediction of human sentence processing.

## How to Use / Reproduce
1. Follow the script in the subfolder _Test_set_selection_ to build and save a set of test stimuli for models
2. Train the model with the data in the subfolder _Model_Training_Surprisal_, and compute surprisal for chosen stimuli (both with one single script _get_surp.py_ under the same subfolder)
3. Build preprocessed data files for stats analyses using the script in the subfolder _Datafile_Building_
4. Use the scripts in the subfolder _Analyses_ to conduct data analyses on the files saved from data file building
