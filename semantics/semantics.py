from instance import Instance
from copy import copy, deepcopy
from itertools import chain


"generates all possible combinations of token-to-sense mapping"
def permutesenses(tokens, lexicon):
    if len(tokens) == 0:
        return [[]]
            
    return [[sense] + senses
            for senses in permutesenses(tokens[1:], lexicon)
            for sense in lexicon[tokens[0]]]


# can use dependencies as heuristic of where to start from


"generates all possible combinations of how specified instances can be linked via their slots"
def link(instances):
    if len(instances) == 0:
        return [[]]
    
    return [[do(i, exclude(copy(instances), i), i.slots.keys())] + link(exclude(copy(instances), i))
             for i in instances]


def link_each(instances):
    linkings = []
    
    for i in filter(lambda i: len(i.slots) > 0, 
                    instances):
        linkings.append(link_single(i, exclude(copy(instances), i), i.slots.keys()))
    
    return linkings

"generates all possible combinations of filler assignment the to given head instance's slots"
def link_single(head, filler_concepts, slotnames):
    if len(filler_concepts) == 0 or len(slotnames) == 0:
        return head
    
    return [link_single(branch(head, slotnames[0], Instance(fc)), 
                        exclude(copy(filler_concepts), fc), 
                        copy(slotnames)[1:])
            for fc in filler_concepts]


def branch(head, slotname, filler):
    
    #print 'branch %s' % filler
    
    clone = deepcopy(head)
    clone.slots[slotname].fill(filler)
    
    return clone


def exclude(collection, element):
    collection.remove(element)
    
    return collection
    


        
     