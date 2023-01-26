# -*- coding: utf-8 -*-
"""
@author: mauro


19-26/01/2022

"""


import numpy as np
import matplotlib.pyplot as plt
import time

brain_size=250
focus_size=15


# Define the initial state of the brain as a 2D matrix: estado actual -> está a fazer descarga elétrica ou não
brain_matrix = np.zeros((brain_size, brain_size), dtype=int)

number_of_focus=1


for f in range(0,number_of_focus):
    focus_x = np.random.randint(0, brain_size-focus_size)
    focus_y = np.random.randint(0, brain_size-focus_size)
    
    # provide the focus
    for i in range(focus_x, focus_x + focus_size):
        for j in range(focus_y, focus_y + focus_size):
            # Update the value of the matrix in the focus area
            brain_matrix[i][j] = int(1)


# Define the probability of a cell switching its state: podemos ver isto como a susceptibilidade às crises
p_switch = 0.51

p_switches=[]
p_switches.append(p_switch)

# Define the number of iterations
n_iterations = 500

# Define the strategy of the cells -> tenderá a excitar ou não?
strategy = np.random.randint(2, size=(brain_size, brain_size))

# Initialize a list to store the brain matrix at each iteration
brain_matrices = []

start=time.time()

# Loop for the number of iterations
for i in range(n_iterations):
    
    if(i>=1 and i<=4):
        p_switch=0.07*i+0.51
    
    elif(i>=5 and i<=6):
        p_switch=0.95
        
    elif(i>=7 and p_switch>0.45):
        p_switch=p_switch-0.03  
        
    elif(i>=22 and p_switch<=0.45):
        p_switch=p_switch
        
    p_switches.append(p_switch)
    
    #(fazer para aqui algo sinosoidal para se aguentar mais tempo?)
    
    # Append the current brain matrix to the list
    brain_matrices.append(brain_matrix.copy())
    new_brain_matrix=brain_matrix.copy()
    
    # Loop through each cell in the brain matrix
    for x in range(brain_matrix.shape[0]):
        for y in range(brain_matrix.shape[1]):
            # Get the number of neighboring cells that are in the "on" state
            neighbors = (brain_matrix[x-1:x+2, y-1:y+2] == 1).sum() - brain_matrix[x, y]

            # Check if the cell should switch its state based on the number of "on" neighboring cells and the probability of switching
            if (neighbors >= 2) and (np.random.rand() < p_switch):
                new_brain_matrix[x, y] = 1
            else:
                new_brain_matrix[x, y] = 0


    brain_matrix=new_brain_matrix.copy()         


end=time.time()
print("Execution lasted: "+str(end-start)+" seconds")

from matplotlib.pyplot import figure, draw, pause


# plot over time from brain matrices

fg = figure()
ax = fg.gca()    
    
h = ax.imshow(brain_matrices[0])  # set initial display dimensions

i=0
for img in brain_matrices:  
    i=i+1
    plt.title("iteration "+str(i))
    h.set_data(img)
    draw(), pause(0.05)


# plot of p_switch over time
fg = figure()
ax = fg.gca()    

plt.plot(p_switches)
plt.title('P_switch value')
plt.xlabel('Iterations')
plt.ylim([0,1])
plt.show()

