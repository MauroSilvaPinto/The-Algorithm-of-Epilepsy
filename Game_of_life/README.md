# The algorithm of Epilepsy: merging theatre with Epilepsy
# Game of Life simulations

Code based on cellular automaton.
The brain is represented here by a matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).

I was interested in complex systems: complex structures obtained from many individuals, where each follows simple rules.
We have many complex systems in nature, including the rules of darwin's evolution, the brain, and even computation.

Videos of neurons on the microscope also inspired me. The Game of Life could be an excellent metaphor for all of this.

If you would like to understand what I am talking about, check out these videos:
- https://www.youtube.com/watch?v=2TIK9oXc5Wo
- https://www.youtube.com/shorts/A9zLKmt2nHo
- https://www.youtube.com/watch?v=3fkJA5gZDcI 
- https://www.youtube.com/watch?v=HM17p1vDF9A


## How to execute this code

You execute `main.py` and then `matlab_animation.m`. The first code will perform the Game of Life simulation and store the simulation in a `.mat` file. The second code will transform the `.mat` file into a video.

- [main.py](/Game_of_life/main.py) - a code that performs the Game of Life simulation. The simulation begins with `N` gliders, and some more are created in the matrix side borders during the simulation. The code saves the simulation as a 3D matrix into a `.mat` file.
- [structure.py](/Game_of_life/structure.py) - this code contains all the utilities to perform the Game of Life. This includes the rules of life, how to create structures, how to rotate, how to interact with the matrix borders, etc. Many structures are available, including spaceships, oscillators, still forms, and some methuselahs.
- [matlab_animation.m](/Game_of_life/matlab_animation.m) - a code to transform the `.mat` file from `main.py` into an MP4 video.
