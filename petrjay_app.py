from knowledge.ontology_petrjay import *
from knowledge.lexicon_petrjay import Lexicon
from plan_selection.planManager_petrjay import PlanManager
from pprint import pprint
from leia import leia
import os


def move_tmr(position):
    move = MoveEvent()
    to = Location()
    
    move.to = to
    
    to.latitude = position[0]
    to.longitude = position[1]
    
    return [move, to]


if __name__ == "__main__":
    world_length = 5
    position = [world_length / 2, world_length / 2]
    direction = {'w' : (0, -1), 'a' : (1, -1), 's' : (0, +1), 'd' : (1, +1)}

    lexicon = Lexicon()
    planner = PlanManager()
    
    planner.updatePlanQueue([AgentWakeEvent()])
    
    ### clear screen
    os.system(['clear','cls'][os.name == 'nt'])
    
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
            planner.updatePlanQueue(move_tmr(position))
            
        elif input:
            leia(input, lexicon, planner)

        else:
            planner.updatePlanQueue(0)

            
        
            