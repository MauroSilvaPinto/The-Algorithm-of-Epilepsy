'''
   This simulation:
       
       lasts 1 minute approximately 18 seconds (250 iterations)
       contains only interictal epileptiform activity.
       
       From iterations 0-50:
           no activity
           
       From iterations  50-100:
           a rate of one interictal epileptform discharge per each 10 iterations
           (np.linspace(50,100,6))
        
       From iterations  100-150:
           a rate of one interictal epileptiform discharge per each 5 iterations
           (np.linspace(100,150,11))
           
       From iterations  150-200:
           a rate of one interictal epileptiform discharge per each 3 iterations 
           (np.linspace(150,198,17))
    
        From iterations 200-250:
            a rate of one interictal epileptiform discharge per each 1 iteration 
            (np.linspace(200,250,51))
            
        From iterations  250-300:
            no activity
            
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
n_iterations=300

# in the brain of a patient with epilepsy, there is a series of epileptic trypical activity:
# 1) brain einterictal epileptiform discharges and 2) seizure discharges
# these are all stored in this array
brain_discharges=[]

# lets keep track of the time
start=time.time()


############################ Dischargers Parameters #############################

# INTERICTAL EPILEPTIFORM ACTIVITY

# the timing of the bursts onset
epileptiform_bursts_onset_timing=np.concatenate((np.linspace(50,100,6),np.linspace(100,150,11),
                                    np.linspace(150,198,17),np.linspace(200,250,51))).astype(int)

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
    
    
        
        
        
        
        
    
        
