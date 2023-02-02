'''
   This simulation:
       
       lasts 1 minute approximately 60 seconds (850 iterations * 0.07s per image)
       
       contains interictal epileptiform activity at the beginning
       and then a generalised seizure with multiregions being simultaneously triggered
       
       From iterations 0-50:
           a rate of one interictal epileptiform discharge per each 5 iterations
           (np.linspace(0,50,11))
           
       In iteration 50:
          a seizure discharge will burst in coordinates [200,50]
          a seizure discharge will also burst in coordinates [100, 150]
          a seizure discharge will also burst in coordinates [120, 40]
          a seizure discharge will also burst in coordinates [200, 150]
          a seizure discharge will also burst in coordinates [50, 50]
          a seizure discharge will also burst in coordinates [200, 200]
          
       In iteration 650:
           the electrical activity will start to gradually decrease
           
PS: I choose here the coordinates of the discharges instead of generating random ones
for you to see that it is possible to manually select their position         
'''

############################ Imports #############################

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, draw, pause        

import numpy as np
import time

from discharge import discharge

############################ Inputs and Variables #############################

# brain_dimensions
brain_dim=[250, 250]

# Define the initial state of the brain as a 2D matrix (all 0's, so all neurons are off)
brain_matrix = np.zeros((brain_dim[0], brain_dim[1]), dtype=int)

# Initialize a list to store the brain state at each iteration
brain_matrices = []

# number of iterations
n_iterations=850

# in the brain of a patient with epilepsy, there is a series of epileptic trypical activity:
# 1) brain einterictal epileptiform discharges and 2) seizure discharges
# these are all stored in this array
brain_discharges=[]

# lets keep track of the time
start=time.time()



############################ Dischargers Parameters #############################

# INTERICTAL EPILEPTIFORM ACTIVITY

# the timing of the bursts onset
epileptiform_bursts_onset_timing=np.linspace(0,45,10).astype(int)

# you can play with these values as you like
# shape dimensions of the initial bursts
# in the moment of creating a burst, this represents a bag of shapes
# from where I randomnly choose one.
epileptiform_burst_shapes=[[1,25],[25,1],[2, 10],[10, 2]]

# you can play with these values as you like
# neuron excitability of the initial bursts
# in the moment of creating a burst, this represents a bag of neuron_prob_onset
# from where I randomnly choose one.
epileptiform_prob_onset_neurons=np.linspace(0.25,0.35,16)


# SEIZURE ACTIVITY

# the timing of the bursts onset
seizure_bursts_onset_timing=[50, 50, 50, 50, 50, 50]

# you can play with these values as you like
# shape dimensions of the initial seizure burst
# in the moment of creating a burst, this represents a bag of shapes
# from where I randomnly choose one.
seizure_burst_shapes=[[5,5],[4,8],[8,4],[3,4],[4,9]]

# you can play with these values as you like
# neuron excitability of the initial seizure discharge
# in the moment of creating a seizure burst, this represents a bag of neuron_prob_onset
# from where I randomnly choose one.
seizure_prob_onset_neurons=np.linspace(0.50,0.80,31)

# the coordinates from where the three seizure discharges will burst
seizure_burst_coordinates=[[200, 50],
                           [100, 150],
                           [120,40],
                           [200, 150],
                           [50, 50],
                           [200, 200]]

# a counter to see in which seizure burst we are during execution
seizure_burst_counter=0

############################ Execution #############################

# Loop for the number of iterations
for i in range(n_iterations):
        
    # the brain state of the current iteration
    new_brain=np.zeros((brain_dim[0], brain_dim[1]), dtype=int)
    
    # running the iteration of each epileptogenic focus
    for brain_discharge in brain_discharges:
        brain_discharge.run()
        
        # delete the finished discharges to spare computational cost
        if brain_discharge.isDischargeEnded():
            brain_discharges.remove(brain_discharge)
        
        
   # an epileptfiform discharge starts at...
    if i in epileptiform_bursts_onset_timing:
        
       # create a discharge. this discharge is created selecting randomnly options from
       # epileptiform_burst_shapes and epileptiform_prob_onset_neurons lists
       discharge_i=discharge('interictal_epileptiform',
                             epileptiform_prob_onset_neurons[np.random.randint(len(epileptiform_prob_onset_neurons))],
                             epileptiform_burst_shapes[np.random.randint(len(epileptiform_burst_shapes))],
                             brain_dim)
       discharge_i.start()
       brain_discharges.append(discharge_i)
       
       
   # a seizure  discharge starts at...    
    if i in seizure_bursts_onset_timing:
       
       # this occurs to deal with several burst occurring simultaneously in the same iteration
       for j in range(0,seizure_bursts_onset_timing.count(i)):
           # create a discharge. this discharge is created selecting randomnly options from
           # epileptiform_burst_shapes and epileptiform_prob_onset_neurons lists
           discharge_i=discharge('seizure',
                                 seizure_prob_onset_neurons[np.random.randint(len(seizure_prob_onset_neurons))],
                                 seizure_burst_shapes[np.random.randint(len(seizure_burst_shapes))],
                                 brain_dim,
                                 center=seizure_burst_coordinates[seizure_burst_counter])
           
           discharge_i.start()
           brain_discharges.append(discharge_i)
           
           #update the counter. this is useful for the seizure center
           seizure_burst_counter=seizure_burst_counter+1
       
        
    # obtaining the brain map accounting for all seizures
    for brain_discharge in brain_discharges:
        new_brain=new_brain+brain_discharge.brain
    
    # truncate activity because maximum activity = 1
    new_brain[new_brain > 1] = 1
    
    # save the brain state
    brain_matrices.append(new_brain)

# end of the execution   
end=time.time()

# printing the execution time
print("Execution lasted: "+str(end-start)+" seconds")


############################ Plot over time #############################

# The plot over time of the brain matrices
fg = figure()
ax = fg.gca()    

# I used here "gray" colormap
h = ax.imshow(brain_matrices[0], cmap="gray", vmin=0, vmax=1)  # set initial display dimensions


# time per each image (in seconds)
# you can change the speed of the animation concerning the value of this variable
# here is a simple way of you roughly determining (in seconds) the animation time: number of iterations * time_image
time_image=0.07

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



############################ Plot of one p-switch  #############################
       
# In this case, I am plotting the p_switch function over time
# from the first stored brain_discharge
discharge=discharge_i

fg = figure()
ax = fg.gca()    

plt.plot(discharge.p_switches)
plt.title('P_switch value')
plt.xlabel('Iterations')
plt.ylim([0,1])
plt.show()    
    
    
        
        
        
        
        
    
        
