This folder contains the script and data used for SRN and LSTM model training and surprisal computation for a set of chosen stimuli.

## Explanation
<b>get_surp.py:</b>\
This script trains SRN and LSTM models and saves them (at various training steps possible). Then, each model computes surprisal for each word in every chosen sentence stimulus (from a file created from stimulus set selection).

<b>vocabulary.txt:</b>\
The training corpus for both models.
