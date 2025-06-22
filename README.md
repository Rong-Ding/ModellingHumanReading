## 📖 Modelling Human Reading
This repository contains scripts for the two Python-based modelling projects (Assignments 1 and 2), where **semantic models** (_Word2Vec_) and **recurrent neural networks** (that is, simple recurrent networks (SRNs) and long-short-term memory (LSTM) models) were trained to simulate and interpret human reading. 

**Impact**: Modelling how humans process and interpret language provides valuable insights into **neuro-cognitive behaviour**. This could help **neuropsychologists** better understand language processing impairments, such as in aphasia or autism spectrum disorders. In practical applications, understanding human reading performance via modelling improves **language learning technologies** (e.g., Duolingo, Babbel), by making them more tailored as **adaptive learning systems** to real cognitive patterns.

### Assignment 1: Semantic models (Word2Vec) in handling word semantics
- Training: **CBOW Word2Vec models** on a large English corpus (ENCOW) with **16 billion words**; _hidden layer size_ and _context window_ varied
- Testing: The models' ability to predict humans' semantics-based word processing (categorisation and semantic priming)
- Findings:
  - Distributional word vectors from Word2Vec generally capture well **word semantics used by humans**.
  - The bigger the hidden layer size, the better a Word2Vec model predicts human word processing.
  - However, models with a smaller context window size tend to predict human behaviour better, indicating limited **working memory capacity** in human word processing

### Assignment 2: SRN vs LSTM in characterising the statistical structure of language and syntactic ambiguity (garden-path sentences)
- Training: SRN vs LSTM models on a large English corpus with 8.7 billion words; _training data size_ varied
- Testing: The models' ability to characterise language statistics (_perplexity_) and predict human performance (_sensitivity to syntactic ambiguity_)
- Findings:
  - With big training sizes, SRN and LSTM give almost equally low perplexity, meaning that they both capture well the statistical structure of language.
  - However, LSTMs show higher sensitivity to syntactically ambiguous sentences than SRNs do.
  - Characterising linguistic statistics well therefore does not necessarily indicate good prediction of human sentence processing.
