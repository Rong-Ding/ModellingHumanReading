## Project 1
The current project aims to examine how well semantic models, that is _Word2Vec_, handle word semantics
- Training: CBOW Word2Vec models on a large English corpus (ENCOW) with 16 billion words; _hidden layer size_ and _context window_ varied
- Testing: The models' ability to predict humans' semantics-based word processing (categorisation and semantic priming)
- Findings:
  - Distributional word vectors from Word2Vec generally capture well word semantics used by humans.
  - The bigger the hidden layer size, the better a Word2Vec model predicts human word processing.
  - However, models with a smaller context window size tend to predict human behaviour better, indicating limited working memory capacity in word processing

## How to Use / Reproduce
1. Follow the script in the folder _Model_Training_ to train and save Word2Vec models (the training corpus, unfortunately, is not available online due to its big size; may be available upon request)
2. Follow the scripts and data files in the folder _Data_Preprocessing_, where saved Word2Vec models are also used to compute surprisal values; analysis-ready datafiles are saved
3. Analyse data and compute the measure (Goodness-of-fit) using the scripts in _Measure_Computation_Analyses_
