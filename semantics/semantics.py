from instance import Instance
from copy import *

# can use dependencies as heuristic of where to start from


"generates all possible combinations of how specified instances can be linked via their slots"
# wanna have BuyEvent theme = Fish, agent = Animal
def link(instances):
    if len(instances) == 0:
        return [[]]
    
    return [[do(i, exclude(copy(instances), i), i.slots.keys())] + link(exclude(copy(instances), i))
             for i in instances]


def link_linear(instances):
    return [do(i, exclude(copy(instances), i), i.slots.keys())
            for i in instances]


"generates all possible combinations of token-to-sense mapping"
def permutesenses(tokens):
    if len(tokens) == 0:
        return [[]]
            
    return [[sense] + senses
            for senses in permutesenses(tokens[1:])
            for sense in lex[tokens[0]]]
    
    
def branch(head, slotname, filler):
    
    #print 'branch %s' % filler
    
    clone = deepcopy(head)
    clone.slots[slotname].fill(deepcopy(filler))
    
    return clone


def exclude(collection, element):
    collection.remove(element)
    
    return collection
    

"generates all possible combinations of filler assignment the to given head instance's slots"
def do(head, fillers, slotnames, level = 0):
    
    #print 'do'
    #print level
    #print head
    #print fillers
    #print slotnames
    
    if len(fillers) == 0 or len(slotnames) == 0:
        return head
    
    return [do(branch(head, slotnames[0], c), 
               exclude(copy(fillers), c), 
               copy(slotnames)[1:], 
               level + 1)
            for c in fillers]
        
     