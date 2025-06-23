## Project 2
The current project aims at comparing SRN vs LSTM in characterising the statistical structure of language and syntactic ambiguity (garden-path sentences)
- Training: SRN vs LSTM models on a large English corpus with 8.7 billion words; _training data size_ varied
- Testing: The models' ability to characterise language statistics (_perplexity_) (**Part 1**) and predict human performance (_sensitivity to syntactic ambiguity_) (**Part 2**)
- Findings:
  - With big training sizes, SRN and LSTM give almost equally low perplexity, meaning that they both capture well the statistical structure of language.
  - However, LSTMs show higher sensitivity to syntactically ambiguous sentences than SRNs do.
  - Characterising linguistic statistics well, therefore, does not necessarily indicate good prediction of human sentence processing.

## Explanation
In the subfolders _Part 1_ and _Part 2_, you may find scripts and data for each part.
