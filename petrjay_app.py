from knowledge.lexicon_petrjay import Lexicon
from pprint import pprint
from leia import leia
import os

world_length = 5
position = [world_length / 2, world_length / 2]
direction = {'w' : (0, -1), 'a' : (1, -1), 's' : (0, +1), 'd' : (1, +1)}    

lexicon = Lexicon()

    
if __name__ == "__main__":
    while True:
        print 'Petr & Jay\'s \"Sovetnik\" Personal Assistant'
        
        ### the world is reset at every iteration
        world = [['_' for i in range(world_length)]
                 for j in range(world_length)]  
        
        ### then the user is placed
        world[position[0] % world_length][position[1] % world_length] = '*'
        
        ### TODO: and whatever known locations there are on the map
        
        pprint(world)
        
        input = raw_input("::")
        
        ### clear screen
        os.system(['clear','cls'][os.name == 'nt'])        
        
        ### move the user
        if input in direction.keys():
            position[direction[input][0]] += direction[input][1]
            
        elif input:
            leia(input, lexicon)
            
        
            