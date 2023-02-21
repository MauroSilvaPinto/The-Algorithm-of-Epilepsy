'''

   Game of life experimeeeents
   
'''

############################ Imports #############################

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause        

import numpy as np
import time

from structure import structure

############################ Inputs and Variables #############################

# brain_dimensions
brain_dim=[240, 135]

# Define the initial state of the brain as a 2D matrix (all 0's, so all neurons are off)
brain_matrix = np.zeros((brain_dim[0], brain_dim[1]), dtype=int)

# Initialize a list to store the brain state at each iteration
brain_matrices = []

# number of iterations
n_iterations=2857

# lets keep track of the time
start=time.time()


########################### Structures to put in the brain ##################

# RANDOM INITIALIZATION ALL NEURONS
# random 1's and 0's
# brain_matrix= np.random.randint(2, size=(250, 250))

# # FAMOUS STRUCTURES Manually
# # insert structures
# piece=structure.acorn()
# # rotate the structure
# piece=structure.random_rotate_structure(piece)
# # place the structure in the brain
# brain_matrix=structure.place_structure_into_matrix(piece, brain_matrix, [49,49])

# thunderbird 49,49, - 200 iter
# beehive 49,49 - 215 iter 
# acorn 49, 49, - 300 iter
# INSERT RANDOM STRUCTURES AUTOMATICALLY
# insert structures
for i in range (0,20):
    # create piece
    piece=structure.glider()
    # rotate the structure
    piece=structure.random_rotate_structure(piece)
    # place the structure in the brain
    brain_matrix=structure.place_randomnly_structure_into_matrix(piece, brain_matrix)

############################ Execution #############################

# Loop for the number of iterations
for i in range(n_iterations):
    print(i)
    # brain matrix of the new generation
    new_brain_matrix=brain_matrix.copy()
    
    # Loop through each cell in the brain matrix
    for x in range(brain_matrix.shape[0]):
        for y in range(brain_matrix.shape[1]):
            # Get the number of neighboring cells that are in the "on" state
            neighbors = (brain_matrix[x-1:x+2, y-1:y+2] == 1).sum() - brain_matrix[x, y]

            # any live cell with fewer than two live neighbours dies (underpopulation).
            if (brain_matrix[x,y]==1 and neighbors<2):
                new_brain_matrix[x,y]=0
                
            # any live cell with more than three live neighbours dies (overpopulation).
            elif (brain_matrix[x,y]==1 and neighbors>3):
                 new_brain_matrix[x,y]=0
                 
            # any live cell with two or three live neighbours lives, unchanged, to the next generation.
            elif (brain_matrix[x,y]==1 and (neighbors==2 or neighbors==3)):
                 new_brain_matrix[x,y]=1
                 
            # any dead cell with exactly three live neighbours will come to life..
            elif (brain_matrix[x,y]==0 and (neighbors==3)):
                 new_brain_matrix[x,y]=1


    new_brain_matrix=structure.replace_still_blocks(new_brain_matrix)
    
    if (i%5==0):
        # create piece
        piece=structure.glider()
        # rotate the structure
        piece=structure.random_rotate_structure(piece)
        # place the structure in the brain
        random_side=np.random.randint(2)
        
        # left side
        if random_side==0:
            random_line=1+np.random.randint(brain_dim[0]-5)
            new_brain_matrix=structure.place_structure_into_matrix(piece, new_brain_matrix, [random_line,2])
        # right side
        elif random_side==1:
            random_line=1+np.random.randint(brain_dim[0]-5)
            new_brain_matrix=structure.place_structure_into_matrix(piece, new_brain_matrix, [random_line,brain_dim[1]-5])
    
    
    brain_matrix=new_brain_matrix.copy() 
    
    # save the brain state
    brain_matrices.append(new_brain_matrix)

# end of the execution   
end=time.time()

# printing the execution time
print("Execution lasted: "+str(end-start)+" seconds")


############################ Plot over time #############################

# The plot over time of the brain matrices
fg = figure(figsize=(960,540))
ax = fg.gca()    

# I used here "gray" colormap
h = ax.imshow(brain_matrices[0], cmap="gray", vmin=0, vmax=1)  # set initial display dimensions


# time per each image (in seconds)
# you can change the speed of the animation concerning the value of this variable
# here is a simple way of you roughly determining (in seconds) the animation time: number of iterations * time_image
time_image=0.10

# keep track of simulation time
start=time.time()
i=0
for img in brain_matrices:  
    i=i+1
    plt.title("iteration "+str(i))
    h.set_data(img)
    draw(), pause(time_image)
    
# end of simulation
end=time.time()

# printing the simulation time
print("Animation lasted: "+str(end-start)+" seconds")
    

######################### Video over time biiiithc #############################    

import scipy.io
scipy.io.savemat('test.mat',{ 'data': np.array(brain_matrices)})