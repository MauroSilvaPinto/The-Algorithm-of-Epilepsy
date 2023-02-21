"""
DESCRIPTION


The class discharge.
This class allows the construction of discharge instances.


Each seizure discharge is an electrical burst that rapidly grows and leads to a seizure
    (or is already a secondary burst due to the seizure propagation).
From a sudden burst, there is a rapid increase and subsequent brain activity that holds for 30s - 120s.

An instance of this object has the following attributes:    
    
    - type_discharge: (string, "seizure" or "interictal_epileptiform")
        The type of discharge it concerns: a seizure, or interictal_epileptiform.
        
        (In practical terms, what differs a seizure discharge from an interictal_epileptiform one is:
            the input focus_size is smaller in the interictal epileptiform discharge
            the input onset_prob_neuron is smaller in the interictal epileptiform discharge
            the p_switch function over iteration is different for a seizure discharge or for a interictal epileptiform one.)
            
    
    - brain (np.matrix[brain_shape] with binary values (0,1)):
        The brain matrix where the seizure discharge will begin, run, and end
        
    - focus_size ([integer, integer]):
        the size of the region of the beginning of the seizure disharge.
        
    - center ([integer, integer]):
         a reference coordinate for the seizure discharge beginning zone
        
    - onset_prob_neuron (float between 0-1):
        the probability of an neuron initially bursting in the beggining
        of the seizure_discharge zone 
         
    - p_switch(float between 0-1):
        The p_switch value is the probability that a given neuron will be triggered
        when at least 2 neighbouring neurons are activated.
         
    - iteration (integer):
        an iteration counter to help understanding the seizure evolution.
        this iteration is fundamental to modify the p_switch value over the execution iterations
    
    - p_switches ([float(0-1), float(0-1), ... , float(0-1)]):
        a list of all p_switch values over the different iterations.
        By storing the p_switch values in this list, we can plot the p_switch value function over time
        to understand the physiology behind this electricty potencial / brain susceptibility to seizures
        
        
FUNCTIONS

Each instance of a seizure_discharge object has two main functions:
        
    i) start : trigger a seizure discharge
    
    ii) run: run the execution of the algorithm for electrical activity over time
    
    
    
The remaining functions are not meant to be called in the main code.
These are called inside the main functions.


Note: by having an attribute that determines the type of discharge (seizure, interictal_epileptiform),
we can add more types of discharges where we simply need to design more p_switch functions over time
and find the remaining appropriate input values.
        
"""

import numpy as np
import math


class discharge:
    
    '''
    The constructor of the seizure_discharge object
    
    
    INPUTS:
        
        - type_discharge (string, "seizure" or "interictal_epileptiform")
        
        - onset_prob_neuron (input: float between 0-1):
    
        - focus_size (input: [integer, integer]):
            
        - brain_shape (input:[integer, integer]):
            the shape of the brain used here for this simulation
            (it must be the same as the main code)
            the brain willl start as a matrix of 0's
            
        - center ([integer, integer]):
            there is a default center: [-1, -1].
            if there is no input center, a random center will be chosen
    
    Iterations start at 0 for all instances.
    P_switches starts empty
    P_switch value starts at 0 (the initial value is never used)
   '''
    def __init__(self, type_discharge, onset_prob_neuron, focus_size, brain_shape, center=[-1,-1]):
        self.type_discharge=type_discharge
        
        self.onset_prob_neuron=onset_prob_neuron
        self.focus_size=focus_size
        self.p_switch=1
        self.brain=np.zeros((brain_shape[0], brain_shape[1]), dtype=int)
        
        if (center==[-1,-1]):# no input center was provided
            self.choose_random_center()
        else: # use the provided input center
            self.center=center
            
        self.iteration=0
        self.p_switches=[]
        
        
      
    # MAIN FUNCTION
    #
    # Starts the discharge:
        # triggers an discharge
        # sets the counter iteration to 1
    def start(self):
        self.discharge_beginning()
        self.iteration=self.iteration+1
    
    
    # MAIN FUNCTION
    #
    # Executes the discharge over each iteration:
        # the new p_switch is updated based on the current iteration
        # the electrical activity is calculated for this p_switch
        # we add a +1 value to the iteration counter
    #    
    # attention: this is only performed while the discharge has not ended
    #           this way, we spare computational time
    def run(self):
        if not self.isDischargeEnded():
            self.update_p_switch()
            self.activity_each_iteration()
            self.iteration=self.iteration+1
        
    
    
   
   # AUXILIAR FUNCTION
   #
   # verifies if the discharge has ended
   # 
   # returs true if there aren't neurons activated 
   # returns false if there are neurons activated  
    def isDischargeEnded(self):
        return (np.sum(self.brain)== 0)
    
    # choose epileptogenic focus center randomnly
    def choose_random_center(self):
        focus_x = np.random.randint(0, self.brain.shape[0]-self.focus_size[0])
        focus_y = np.random.randint(0, self.brain.shape[1]-self.focus_size[1])
        
        self.center=[focus_x, focus_y]
    
   
    
   # AUXILIAR FUNCTION
   #
   # chooses the discharge position randomnly
   # 
   # output: the center attribute will be changed to the obtained coordinates
    def discharge_beginning(self):
        # iterate all the matrix (lines and collumns)
        for i in range(self.center[0], self.center[0] + self.focus_size[0]):
            for j in range(self.center[1], self.center[1] + self.focus_size[1]):
                # firing each focus neuron according to a probability
                 if (np.random.rand() < self.onset_prob_neuron):
                     self.brain[i][j] = int(1)
     
    
    
    ###### Auxiliar functions for epileptogenic focus electric activity over time     
  
    def activity_each_iteration(self):
       # create a copy of the brain matrix to create the next generation brain state
       new_brain=self.brain.copy()
       
       # Loop through each neuron in the brain matrix
       for x in range(self.brain.shape[0]):
           for y in range(self.brain.shape[1]):
                # Get the number of neighboring neurons that are in the "on" state
                neighbors = (self.brain[x-1:x+2, y-1:y+2] == 1).sum() - self.brain[x, y]
    
                # Check if the neuron should switch its state based on the number of "on" neighboring neurons and the probability of switching (p_switch)
                if (neighbors >= 2) and (np.random.rand() < self.p_switch):
                    new_brain[x, y] = 1
                else:
                    new_brain[x, y] = 0
       
       # replace the brain matrix by the new one
       self.brain=new_brain
            
    
    # update the p_switch value for the current iteration
    # saves the current p_switch in a list of past p_switch values
    def update_p_switch(self):
        
        if self.type_discharge=="seizure":
            self.update_p_switch_seizure()
            
        elif self.type_discharge=="interictal_epileptiform":
            self.update_p_switch_epileptiform()
        
        # saving new p_switch value
        self.p_switches.append(self.p_switch)
        
        
        
     # update the p_switch value for the current iteration
     # saves the current p_switch in a list of past p_switch values
    def update_p_switch_seizure(self):
        
         p_switch_start=0.51
         
         # updating current p_switch value
         if(self.iteration>=1 and self.iteration<=4):
             self.p_switch=0.07*self.iteration+p_switch_start
     
         elif(self.iteration>=5 and self.iteration<=6):
             self.p_switch=0.95
             
         elif(self.iteration>=7 and self.p_switch>0.45):
             self.p_switch=self.p_switch-0.03  
             
         elif(self.iteration>=22 and self.iteration<=600 and self.p_switch<=0.45):
             self.p_switch=0.46+(math.cos(np.random.uniform(-math.pi, math.pi))*0.03)
             
         elif(self.iteration>600):
             self.p_switch=0.43+(math.cos(np.random.uniform(-math.pi, math.pi))*0.02)
             
             
     # update the p_switch value for the current iteration
     # saves the current p_switch in a list of past p_switch values
    def update_p_switch_epileptiform(self):
         
         p_switch_start=0.51
         
         # updating current p_switch value
         if(self.iteration>=1 and self.iteration<=3):
             self.p_switch=0.07*self.iteration+p_switch_start
     
         elif(self.iteration>=4 and self.p_switch>0.45):
             self.p_switch=self.p_switch-0.10 
             
         elif(self.iteration>5):
             self.p_switch=0.33+(math.cos(np.random.uniform(-math.pi, math.pi))*0.02)
             
            
    
            