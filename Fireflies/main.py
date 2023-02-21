#### 
#
# criar aqui um espaço de possibilidades, um road map
#   (este será executado várias vezes, para existirem vários roadmaps)
#
# escolher um sítio random onde disparar e escolher um espaço de possibilidades
# (espalhar este imoulso e fazê-lo até ao fim)
#
# desligar...
# fazer isto all over again
#
#
#
####

def create_brain_connections(brain_dim,p_connect):
    brain_connections=np.zeros(brain_dim)
    for i in range(0,brain_dim[0]):
        for j in range(0,brain_dim[1]):
            if (np.random.rand()<(p_connect*0.03)):
                brain_connections[i,j]=1
    
    return brain_connections



def select_center(brain_dim):
    radius_x=int(round(np.random.rand()*brain_dim[0]*0.01,0))
    radius_y=int(round(np.random.rand()*brain_dim[1]*0.01,0))
    
    x=np.random.randint(brain_dim[0]-radius_x)
    y=np.random.randint(brain_dim[1]-radius_y)
    
    return [x,y, radius_x, radius_y]


def create_activation_mask(brain_dim, center):
    activation_mask=np.zeros(brain_dim)
    
    x=center[0]
    y=center[1]
    
    radius_x=center[2]
    radius_y=center[3]
    
    for i in range(radius_x):
        for j in range(radius_y):
            activation_mask[x+i,y+j]=1
    
    return activation_mask



def activate_neurons(brain_connections,activation_mask):
    brain_dim=np.shape(brain_connections)
    brain_matrix=np.zeros([brain_dim[0],brain_dim[1]])
    
    for i in range(0,brain_dim[0]):
        for j in range(0,brain_dim[1]):
            if (brain_connections[i,j]==1 and activation_mask[i,j]==1):
                brain_matrix[i,j]=np.random.rand()
                
    return brain_matrix



def propagate_activation(activation_mask, propagation_distance, center):
    brain_dim=np.shape(activation_mask)
    maximum_distance=np.sqrt(brain_dim[0]**2+brain_dim[1]**2)
    
    x=center[0]
    y=center[1]
    
    propagation_distance=propagation_distance+(0.15*np.random.rand()*maximum_distance)
    
    for i in range(brain_dim[0]):
        for j in range(brain_dim[1]):
            if np.sqrt(abs(x-i)**2+abs(y-j)**2)<propagation_distance:
                activation_mask[i,j]=1
                
    return [activation_mask, propagation_distance]
    
    
def isFiringDone(brain_connections, brain_matrix):
    return (np.sum(brain_connections)==np.sum(brain_matrix))


import random
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause        
import time

dim=50
brain_dim=[50,200]
matrix=np.zeros([dim, dim])
matrices=[]

iterations=200

############################ Create brain path connections #############################
brain_connections=[]

for i in range(10):
    brain_connections.append(create_brain_connections(brain_dim,0.15*np.random.rand()))


############################ Execution #############################

counter=0

brain_matrix=np.zeros(brain_dim)

for iter in range(0, iterations):
    
    if counter==0:
        center=select_center(brain_dim)
        activation_mask=create_activation_mask(brain_dim, center)
        brain_connection=brain_connections[np.random.randint(len(brain_connections))]
        propagation_distance=0
        
        brain_matrix=activate_neurons(brain_connection,activation_mask)
        brain_matrix=brain_matrix.clip(0,1)
        counter=counter+1
        
    else:
        [activation_mask,propagation_distance]=propagate_activation(activation_mask,
                                                                     propagation_distance,
                                                                     center)
        brain_matrix=brain_matrix+activate_neurons(brain_connection,activation_mask)
        brain_matrix=brain_matrix.clip(0,1)
        counter=counter+1
    
        
    if isFiringDone(brain_connection, brain_matrix):
        counter=0
        brain_matrix=np.zeros(brain_dim)
    
    matrices.append(brain_matrix)
    

    
############################ Plot over time #############################

# The plot over time of the brain matrices
fg = figure()
ax = fg.gca()    

# I used here "gray" colormap
h = ax.imshow(matrices[0], cmap="gray", vmin=0, vmax=1)  # set initial display dimensions


# time per each image (in seconds)
# you can change the speed of the animation concerning the value of this variable
# here is a simple way of you roughly determining (in seconds) the animation time: number of iterations * time_image
time_image=0.05

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






    
    
