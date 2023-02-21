
import numpy as np
from matplotlib.pyplot import figure, draw, pause  




class structure:
    
    
    # Structures from Game of Life
    
    # glider
    def glider():
        matrix = np.array([
                        [0, 1, 0],
                        [0, 0, 1],
                        [1, 1, 1]], dtype=np.int8)  
        return matrix
    
    
    # blinker
    def blinker():
        matrix = np.array([
                        [0, 0, 0],
                        [1, 1, 1],
                        [0, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # toad
    def toad():
        matrix = np.array([
                [0, 1, 1, 1],
                [1, 1, 1, 0]], dtype=np.int8)
        return matrix
    
    
    # beacon 
    def beacon():
        matrix = np.array([
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 1]], dtype=np.int8)
        return matrix
    
    # pulsar
    def pulsar_chatgpt():
        matrix = np.array([
                [0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # loaf
    def loaf():
        matrix = np.array([
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 0, 1, 0]], dtype=np.int8)
        return matrix
    
    
    # boat
    def boat():
        matrix = np.array([
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 0]], dtype=np.int8)
        return matrix
                
    
    # lightweight spaceship
    def lwss():
        matrix = np.array([
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 1, 0]], dtype=np.int8)
        return matrix
    
    
    # middletweight spaceship
    def mwss():
        matrix = np.array([
                [0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # heavy-weight spaceship
    def hwss():
        matrix = np.array([
                [0, 0, 1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # die hard
    def diehard():
        matrix = np.array([
                [0, 0, 0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # beehive
    def beehive():
        matrix = np.array([
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 0]], dtype=np.int8)
        return matrix
        
    
    # evlutes to traffic lights oscilator model: a model by chatgpt
    def evol_to_traffic_lights():
        matrix = np.array([
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # an excitatory neuron according to chatgpt
    def excitatory_neuron_chatgpt():
        matrix = np.array([
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
        return matrix
                        
    
    # an inhibitory neuron by chatgpt
    def inhibitory_neuron_chatgpt():
        matrix = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # https://www.youtube.com/watch?v=S8xVfaKpcDE
    def methuselah_youtube():
        matrix = np.array([
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # Acorn Methuselah - 5206  gerações para estabilizar
    def acorn():
        matrix = np.array([
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # b_heptomino Methuselah - 5206  gerações para estabilizar
    def b_heptomino():
        matrix = np.array([
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1]], dtype=np.int8)
        return matrix
    
    
    # century methuselah 103 gerações
    def century():
        matrix = np.array([
            [0, 0, 1, 1],
            [1, 1, 1, 0],
            [0, 1, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # herschel methuselah 128 gerações
    def herschel():
        matrix = np.array([
            [0, 1, 1, 1],
            [0, 0, 1, 0],
            [1, 1, 1, 0]], dtype=np.int8)
        return matrix
    
    
    # pi_heptomino methuselah 173 gerações
    def pi_heptomino():
        matrix = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1]], dtype=np.int8)
        return matrix
    
    # r_heptomino methuselah 1103 gerações
    def r_heptomino():
        matrix = np.array([
            [0, 1, 1],
            [1, 1, 0],
            [0, 1, 0]], dtype=np.int8)
        return matrix
    
    # thunderbird methuselah 243 gerações
    def thunderbird():
        matrix = np.array([
            [1, 1, 1],
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]], dtype=np.int8)
        return matrix
    
    
    # queen bee methuselah 191 gerações
    def queen_bee():
        matrix = np.array([
            [1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0],], dtype=np.int8)
        return matrix
    
    
    # pulsar oscillator period 3
    def pulsar():
        matrix = np.array([
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]], dtype=np.int8)
        return matrix
    
    
    # a square of one's
    def cell_block(n=5):
        matrix = np.ones([n,n], dtype=np.int8)
        return matrix
    
    # a square of one's
    def line(n=5):
        matrix = np.ones([1, n], dtype=np.int8)
        return matrix
    
    
    
    #### Utils functions
    
    # place ramdomnly a structure inside a brain
    def place_randomnly_structure_into_matrix(structure,matrix):
        # get the sape of the structures
        shape_structure=np.shape(structure)
        shape_matrix=np.shape(matrix)
    
        #try to find a place to randomly place the structure
        number_attempts=100
        found_place=False
        for i in range (0,number_attempts):
            
            # generate center
            x = np.random.randint(0, shape_matrix[0]-shape_structure[0])
            y = np.random.randint(0, shape_matrix[1]-shape_structure[1])
            
            # verify if center+size is empty
            neighbors = (matrix[x:x+shape_structure[0], y:y+shape_structure[1]] == 1).sum()
            
            # if empty
            if neighbors==0:
                found_place=True
                break
            
        # is it possible to place?
        if found_place==True:
            # place structure
            matrix[x:x+shape_structure[0], y:y+shape_structure[1]]=structure
        else:
            print("structure_not_placed")
            
        return matrix
    
    
    # place a structure inside a brain in a given place
    def place_structure_into_matrix(structure,matrix,center):
        # get the sape of the structures
        shape_structure=np.shape(structure)
        
        x=center[0]
        y=center[1]
        
        # verify if center+size is empty
        neighbors = (matrix[x:x+shape_structure[0], y:y+shape_structure[1]] == 1).sum()
            
        # if empty
        if neighbors==0:
            matrix[x:x+shape_structure[0], y:y+shape_structure[1]]=structure
        else:
            print("structure_not_placed")
            
        return matrix
        
    
    # randomnly creates a structure from the developed ones
    def create_random_structure():
        # where the structure will be placed
        matrix=np.zeros([2,2])
        
        # list of all possible structures 
        list_structures=["glider", "blinker", "toad", "beacon", "pulsar",
                         "pulsar_chatgpt" "loaf", "boat", "lwss", 
                         "hwss", "diehard", "beehive","cell_block", "line"
                         "evol_to_traffic_lights", "excitatory_neuron_chatgpt",
                         "inhibitory_neuron_chatgpt", "methuselah_youtube",
                         "acorn", "b_heptomino", "pi_heptomino", "r_heptomino",
                         "century", "herschel", "thunderbird", "queen_bee"]
        
        # pick a random structure
        random_index=np.random.randint(len(list_structures))
        
        print(list_structures[random_index])
        
        if list_structures[random_index]=="glider":
            matrix=structure.glider()   
            
        elif list_structures[random_index]=="blinker":
            matrix=structure.blinker()
            
        elif list_structures[random_index]=="line":
            matrix=structure.line()
             
        elif list_structures[random_index]=="cell_block":
            matrix=structure.cell_block()
        
        elif list_structures[random_index]=="toad":
            matrix=structure.toad()
                
        elif list_structures[random_index]=="beacon":
            matrix=structure.beacon()
                
        elif list_structures[random_index]=="pulsar":
            matrix=structure.pulsar()
            
        elif list_structures[random_index]=="pulsar_chatgpt":
            matrix=structure.pulsar_chatgpt()
                
        elif list_structures[random_index]=="loaf":
            matrix=structure.loaf()
        
        elif list_structures[random_index]=="boat":
            matrix=structure.boat()
                
        elif list_structures[random_index]=="lwss":
            matrix=structure.lwss()
            
        elif list_structures[random_index]=="hwss":
            matrix=structure.hwss()
                
        elif list_structures[random_index]=="diehard":
            matrix=structure.diehard()
        
        elif list_structures[random_index]=="beehive":
            matrix=structure.beehive()
            
        elif list_structures[random_index]=="excitatory_neuron_chatgpt":
            matrix=structure.excitatory_neuron_chatgpt()
                
        elif list_structures[random_index]=="inhibitory_neuron_chatgpt":
            matrix=structure.inhibitory_neuron_chatgpt()
            
        elif list_structures[random_index]=="evol_to_traffic_lights":
            matrix=structure.evol_to_traffic_lights()
            
        elif list_structures[random_index]=="methuselah_youtube":
            matrix=structure.methuselah_youtube()
            
        elif list_structures[random_index]=="b_heptomino":
            matrix=structure.b_heptomino()
        
        elif list_structures[random_index]=="pi_heptomino":
            matrix=structure.pi_heptomino()
             
        elif list_structures[random_index]=="r_heptomino":
            matrix=structure.r_heptomino()
             
        elif list_structures[random_index]=="acorn":
            matrix=structure.acorn()
            
        elif list_structures[random_index]=="queen_bee":
            matrix=structure.queen_bee()
            
        elif list_structures[random_index]=="herschel":
            matrix=structure.herschel()
            
        elif list_structures[random_index]=="thunderbird":
            matrix=structure.thunderbird()
            
        elif list_structures[random_index]=="century":
            matrix=structure.century()
                
        
        return matrix
    
    

    # rotating the structure for 0, 90º, 180º or 270º
    def random_rotate_structure(matrix):
        
        # how many times will it rotate 90 degrees
        rotation=np.random.randint(4)
        
        # perform these rotations
        for i in range (0,rotation):
            matrix=np.rot90(matrix)
            
        return matrix
                         
        
    # print the brain matrix just for testing
    def print_brain(matrix):
        fg = figure()
        ax = fg.gca()    

        # I used here "gray" colormap
        ax.imshow(matrix, cmap="gray", vmin=0, vmax=1)
        
    
    
    
    
    def replace_still_blocks(brain_matrix):
        # search in the entire matrix
        
        # search left side
        for i in range(0,brain_matrix.shape[0]-2):
            square=brain_matrix[i:i+2,1:3]
            if np.sum(square)==4:
                # delete the square
                brain_matrix[i:i+3,0:3]
                brain_matrix[i:i+3,0:3]=np.zeros([3,3])
                piece=structure.glider()
                piece=structure.random_rotate_structure(piece)
                brain_matrix[i:i+3,0:3]=piece
                
                
        # search right side
        for i in range(0,brain_matrix.shape[0]-2):
            square=brain_matrix[i:i+2,brain_matrix.shape[1]-2:brain_matrix.shape[1]]
            if np.sum(square)==4:
                # delete the square
                brain_matrix[i:i+3,brain_matrix.shape[1]-3:brain_matrix.shape[1]]
                brain_matrix[i:i+3,brain_matrix.shape[1]-3:brain_matrix.shape[1]]=np.zeros([3,3])
                piece=structure.glider()
                piece=structure.random_rotate_structure(piece)
                brain_matrix[i:i+3,brain_matrix.shape[1]-3:brain_matrix.shape[1]]=piece
                    
                    
       # search top side
        for i in range(0,brain_matrix.shape[1]-2):
           square=brain_matrix[1:3,i:i+2]
           if np.sum(square)==4:
               # delete the square
               brain_matrix[0:3,i:i+3]
               brain_matrix[0:3,i:i+3]=np.zeros([3,3])
               piece=structure.glider()
               piece=structure.random_rotate_structure(piece)
               brain_matrix[0:3,i:i+3]=piece
               
               
        # search down side
        for i in range(0,brain_matrix.shape[1]-2):
            square=brain_matrix[brain_matrix.shape[0]-2:brain_matrix.shape[0],i:i+2]
            if np.sum(square)==4:
                # delete the square
                brain_matrix[brain_matrix.shape[0]-3:brain_matrix.shape[0],i:i+3]
                brain_matrix[brain_matrix.shape[0]-3:brain_matrix.shape[0],i:i+3]=np.zeros([3,3])
                piece=structure.glider()
                piece=structure.random_rotate_structure(piece)
                brain_matrix[brain_matrix.shape[0]-3:brain_matrix.shape[0],i:i+3]=piece
            

        # bottom up left corner
        square=brain_matrix[1:3,1:3]
        if np.sum(square):
            # delete the square
            brain_matrix[0:3,0:3]
           
            brain_matrix[0:3,0:3]=np.zeros([3,3])
            
            piece=structure.glider()
            piece=structure.random_rotate_structure(piece)
            brain_matrix[1:4,1:4]=piece 
            
        
        # bottom down right corner
        square=brain_matrix[brain_matrix.shape[0]-2:brain_matrix.shape[0],
                              brain_matrix.shape[1]-2:brain_matrix.shape[1]]
        if np.sum(square):
            # delete the square
            brain_matrix[brain_matrix.shape[0]-3:brain_matrix.shape[0],
                          brain_matrix.shape[1]-3:brain_matrix.shape[1]]
           
            brain_matrix[brain_matrix.shape[0]-3:brain_matrix.shape[0],
                          brain_matrix.shape[1]-3:brain_matrix.shape[1]]=np.zeros([3,3])
            
            piece=structure.glider()
            piece=structure.random_rotate_structure(piece)
            brain_matrix[brain_matrix.shape[0]-4:brain_matrix.shape[0]-1,
                          brain_matrix.shape[1]-4:brain_matrix.shape[1]-1]=piece
            
        
        # bottom up right corner
        square=brain_matrix[1:3,brain_matrix.shape[1]-2:brain_matrix.shape[1]]
        if np.sum(square):
              # delete the square
              brain_matrix[0:3,brain_matrix.shape[1]-3:brain_matrix.shape[1]]
            
              brain_matrix[0:3,brain_matrix.shape[1]-3:brain_matrix.shape[1]]=np.zeros([3,3])
             
              piece=structure.glider()
              piece=structure.random_rotate_structure(piece)
              brain_matrix[1:4,brain_matrix.shape[1]-4:brain_matrix.shape[1]-1]=piece 
        
       
        # bottom down left corner
        square=brain_matrix[brain_matrix.shape[1]-2:brain_matrix.shape[1],1:3]
        if np.sum(square):
              # delete the square
              brain_matrix[brain_matrix.shape[1]-3:brain_matrix.shape[1],0:3]
            
              brain_matrix[brain_matrix.shape[1]-3:brain_matrix.shape[1],0:3]=np.zeros([3,3])
             
              piece=structure.glider()
              piece=structure.random_rotate_structure(piece)
              brain_matrix[brain_matrix.shape[0]-4:brain_matrix.shape[0]-1,1:4]=piece
                
        
        return brain_matrix