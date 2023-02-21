
import random
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause        
import time

dim=150
matrix=np.zeros([dim, dim])
matrices=[]

iterations=50   

for iter in range(0, iterations):
    
    new_matrix=matrix.copy()
    
    for i in range(0,np.shape(matrix)[0]):
        for j in range(0,np.shape(matrix)[1]):
            if random.random() > 0.99:
                new_matrix[i][j] = 1
            else:
                new_matrix[i][j] = 0
     
    matrices.append(new_matrix)
        
        
############################ Plot over time #############################

# The plot over time of the brain matrices
fg = figure(figsize=(8,6))
ax = fg.gca()    

# I used here "gray" colormap
h = ax.imshow(matrices[0], cmap="gray", vmin=0, vmax=1)  # set initial display dimensions


# time per each image (in seconds)
# you can change the speed of the animation concerning the value of this variable
# here is a simple way of you roughly determining (in seconds) the animation time: number of iterations * time_image
time_image=0.10

# keep track of simulation time
start=time.time()
i=0
for img in matrices:  
    i=i+1
    plt.title("iteration "+str(i))
    h.set_data(img)
    draw(), pause(time_image)
    
# end of simulation
end=time.time()

# printing the simulation time
print("Animation lasted: "+str(end-start)+" seconds")
