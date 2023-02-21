# The algorithm of Epilepsy: merging theatre with Epilepsy
# Ictogenesis - Electrical brain activity simulations

Code based on cellular automaton.
The brain is one matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).


This code contains 5 different executions (main_A, main_B, main_C, main_D, main_E):
  - main_A : different rates of interictal epileptiform activity
  - main_B : interictal epileptiform activity and a focal seizure with no propagation to other regions
  - main_C : interictal epileptiform activity and a focal seizure with quick propagation to other two regions
  - main_D : interictal epileptiform activity and a generalized seizure (huge epileptogenic zone)
  - main_E : interictal epileptiform activity and a generalized seizure (three different epileptic zones are triggered simultaneously)
  
In the respective codes, you will find more details, including the onset time of each electrical activity.



CONTEXT:

 The 2.0 version is a more refined version of the 1.0 version and contains an abstraction layer.
 This layer concerns the electrical activity of the brain.
 
 This activity can be:
    i) a seizure: an electrical discharge that generates extensive and intense electrical activity;
    ii) interictal epileptiform discharge: discharges that generate small "bursts" of electrical activity that cannot trigger seizures.
                
   
 Limitations of this approach:
       
   Interictal epileptiform discharges provide an important clue regarding the epileptogenic focus.
            
   In this code, I have decided to create seizures and interictal epileptiform discharges independently to fill better and explore the visual space.
   We can make this code more scientifically accurate by:
                  using the same centre for both epileptiform discharges and seizures.
            
        
   Also: interictal epileptiform discharges have a short duration.
          Their duration varies from paper to paper, but they have a medium duration of 90-300ms.
          Here they have about 500ms so that they can be more easily visualized. 
