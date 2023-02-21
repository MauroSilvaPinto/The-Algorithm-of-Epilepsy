# The algorithm of Epilepsy: merging theatre with Epilepsy
# Game of Life simulations

Code based on cellular automaton.
The brain is one matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).

## How to execute this code

You execute "main.py" and then "matlab_animation.m". The first code will perform the Game of Life simulation and store the simulation in a .mat file. The second code will transform the .mat file into a video.

- [main.py] - a code to check evts files, which are headlines for the raw binary data. It concerns patient selection: minimum number of 4 seizures separated by at least 4h30 of data.
- [structure.py] - a code to check recording gaps, which concerns patient selection criteria: patients with gaps longer than 1 hour were discarded.
- [matlab_animation.m] - a code to preprocess and extract first-level features, from raw data to chronologically extracted first-level features in non-overlapping windows of 5 seconds. output example: pat[patient_number]_seizure[seizure_number]_featureMatrix.npy
