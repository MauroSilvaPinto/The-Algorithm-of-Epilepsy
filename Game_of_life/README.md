# The algorithm of Epilepsy: merging theatre with Epilepsy
# Game of Life simulations

Code based on cellular automaton.
The brain is one matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).

## How to execute this code

You can not execute this code as it is necessary the raw data from EEG recordings. As the used dataset belongs to EPILEPSIAE, we can not make it publicly available online due to ethical concerns. We can only offer the extracted first-level features from non-overlapping windows of 5 seconds. In preprocessing code:
- [check_evts.py] - a code to check evts files, which are headlines for the raw binary data. It concerns patient selection: minimum number of 4 seizures separated by at least 4h30 of data.
- [check_gaps.py] - a code to check recording gaps, which concerns patient selection criteria: patients with gaps longer than 1 hour were discarded.
- [pre_processing.py] - a code to preprocess and extract first-level features, from raw data to chronologically extracted first-level features in non-overlapping windows of 5 seconds. output example: pat[patient_number]_seizure[seizure_number]_featureMatrix.npy
