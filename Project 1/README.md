## Project 1
The current project aims to examine how well semantic models, that is _Word2Vec_, handle word semantics
- Training: CBOW Word2Vec models on a large English corpus (ENCOW) with 16 billion words; _hidden layer size_ and _context window_ varied
- Testing: The models' ability to predict humans' semantics-based word processing (categorisation and semantic priming)
- Findings:
  - Distributional word vectors from Word2Vec generally capture well word semantics used by humans.
  - The bigger the hidden layer size, the better a Word2Vec model predicts human word processing.
  - However, models with a smaller context window size tend to predict human behaviour better, indicating limited working memory capacity in word processing

## How to Use / Reproduce
