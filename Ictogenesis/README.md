# The algorithm of Epilepsy: merging theatre with Epilepsy
# Ictogenesis - Electrical brain activity simulations

Code based on cellular automaton.
The brain is represented here by a matrix (you decide its size and shape). Each cell of the matrix is one neuron with two possible states (on or off, 1 or 0).


This code contains 5 different executions (main_A, main_B, main_C, main_D, main_E):
  - [main_A](/Ictogenesis/Version_2/main_A.py) : different rates of interictal epileptiform activity. [Video.](https://drive.google.com/file/d/1GrujfcpgaKinw4ZVt5u3908idWjr7Row/view?usp=sharing)
  - [main_B](/Ictogenesis/Version_2/main_B.py) : interictal epileptiform activity and a focal seizure, with no propagation to other regions. [Video.](https://drive.google.com/file/d/1GzZ15YSVt_b8UlgLw3vmHx5kbwwT526P/view?usp=sharing)
  - [main_C](/Ictogenesis/Version_2/main_C.py) : interictal epileptiform activity and a focal seizure, with quick propagation to two other regions. [Video.](https://drive.google.com/file/d/1H0fqQqBNrI5RZqXprM7AlDtY6s3OWGlW/view?usp=sharing)
  - [main_D](/Ictogenesis/Version_2/main_D.py) : interictal epileptiform activity and a generalized seizure (huge epileptogenic zone). [Video.](https://drive.google.com/file/d/1H0kPTmlvodrSZkaOhhRXQHK5Ua72YT6h/view?usp=sharing)
  - [main_E](/Ictogenesis/Version_2/main_E.py) : interictal epileptiform activity and a generalized seizure (three different epileptic zones are triggered simultaneously). [Video.](https://drive.google.com/file/d/1H5E5bSicxxNLY8P5OnBF_7LQBvHh_Agf/view?usp=sharing)
  
In the respective code files, you will find more details, including the onset time of each electrical activity.



## CONTEXT:

 The [2.0 version](/Ictogenesis/Version_2/) is a more refined version of the [1.0 version](/Ictogenesis/Version_1/) and contains an abstraction layer.
 This layer concerns the electrical activity of the brain.
 
 This activity can be:
  1. a seizure: an electrical discharge that generates extensive and intense electrical activity;
  2. interictal epileptiform discharge: discharges that generate small "bursts" of electrical activity that cannot trigger seizures.
                
   
 ## Limitations of this approach:
       
   Interictal epileptiform discharges provide an important clue regarding the epileptogenic focus.
            
   In this code, I have decided to create seizures and interictal epileptiform discharges independently to fill better and explore the visual space.
   We can make this code more scientifically accurate by:
                  using the same centre for both epileptiform discharges and seizures.
            
        
   Also: interictal epileptiform discharges have a short duration.
          Their duration varies from paper to paper, but they have a medium duration of 90-300ms.
          Here they have about 500ms so that they can be more easily visualized. 
