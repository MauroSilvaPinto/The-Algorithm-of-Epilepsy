# The algorithm of Epilepsy: merging theatre with Epilepsy
# Game of Life simulations

Code based on cellular automaton.
The brain is one matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).

I was interested in complex systems, developed from many individuals where each follows simple rules.
We have many complex systems in nature, including the rules of darwin evolution, the brain, even computation.

I was also inspired by videos of neurons on the microscope, and I believed the Game of Life could be a great methaphor for all of this.
If you would like to understand what I'm talking about, check these videos:
- 1
- 2
- 3
- 4
- 


## How to execute this code

You execute "main.py" and then "matlab_animation.m". The first code will perform the Game of Life simulation and store the simulation in a .mat file. The second code will transform the .mat file into a video.

- [main.py] - a code perform the Game of Life simulation. The simulation begins with N gliders and some more are created during the simulation, in the matrix side borders. The code saves the simulation as a 3D matrix into a .mat file.
- [structure.py] - this code contains all the utils to perform game of life: the rules of life, how to create structures, how to rotate, how to interact with the matrix borders, etc. Many structures are available, including: spaceships, oscillators, still forms, and also some methusalens.
- [matlab_animation.m] - a code to transform the .mat file from "main.py" into a MP4 video.
