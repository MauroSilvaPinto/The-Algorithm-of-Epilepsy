# Theatre and Epilepsy

Code based on cellular automaton.
The brain is one matrix (you decide its size and shape). Each cell of the matrix is one neuron and has two possible states (on or off, 1 or 0).


This code contains 5 different executions (main_A, main_B, main_C, main_D, main_E):
  - main_A : different rates of interictal epileptiform activity
  - main_B : interictal epileptiform activity and a focal seizure with no propagation to other regions
  - main_C : interictal epileptiform activity and a focal seizure with quick propagation to other two regions
  - main_D : interictal epileptiform activity and a generalised seizure (very big epileptic zone)
  - main_E : interictal epileptiform activity and a generalized seizure (three different epileptic zones are triggered simultaneously)
  
In the respective codes you will find more details, including the onset time of each electrical activity.



CONTEXTO:

 A versão 2.0 do código está mais cuidada e tem já uma pequena camada de abstracção. Esta camada diz respeito a actividade elétrica típica na epilepsia.
    
    Esta actividade pode ser de dois tipos: 
        i) crise (seizure): uma descarga de crise epiléptica que gera uma grande actividade eléctrica intensa (típica das crises)
        ii) descarga interictal epileptiform: descasrgas que geram pequenos "bursts" de actividade eléctrica
                mas que não chegam a despoletar uma crise. 
                
   
    Limitações desta abordagem:
        
        Na clínica, as descargas interictais epileptiformes dão-nos logo uma pista sobre a localização de onde se poderá gerar a crise.
        Ou seja: estas descargas interictais epileptiformes dão-se geralmente nos locais do cérebro que derão origem a crises.
            
        Aqui decidi tornar as duas actividades "independentes" para se poder também explorar uma abordagem que "preencha" todo o espaço visual,
        No entanto, é possível ter-se fidelidade científica nesse aspecto:
            basta usar o mesmo centro para as descargas epileptiformes e para as descargas de crises epilépticas.
            
        
        Ainda: descargas interictais epileptiformes têm uma duração muito curta.
        Varia de artigo para artigo mas penso terem cerca de 90-300 ms.
        Aqui têm cerca de 500 ms para mais facilmente serem visualisadas. 
