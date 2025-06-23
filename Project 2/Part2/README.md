This folder contains subfolders storing each step of Part 2 in Project 2. Part 1 aims at comparing the ability of SRN and LSTM models to predict human performance (sensitivity to syntactic ambiguity)

## How to Use / Reproduce
1. Follow the script in the subfolder _Test_set_selection_ to build and save a set of test stimuli for models
2. Train the model with the data in the subfolder _Model_Training_Surprisal_, and compute surprisal for chosen stimuli (both with one single script _get_surp.py_ under the same subfolder)
3. Build preprocessed data files for stats analyses using the script in the subfolder _Datafile_Building_
4. Use the scripts in the subfolder _Analyses_ to conduct data analyses on the files saved from data file building
