from instance import Instance
import copy

# can use dependencies as heuristic of where to start from


"generates all possible combinations of how specified instances can be linked via their slots"
# wanna have BuyEvent theme = Fish, agent = I
def link(concepts, instances):
    if len(concepts) == 0:
        return [[]]
    
    i = Instance(concepts[0])
    print i.slots
    return [i if i.slots[s].fill(f) else [[]]
     for f in link(concepts[1:], instances + [i])
     for s in i.slots] if len(i.slots) > 1 else [i]


"generates all possible combinations of token-to-sense mapping"
def permutesenses(tokens):
    if len(tokens) == 0:
        return [[]]
            
    return [[sense] + senses
            for senses in permutesenses(tokens[1:])
            for sense in lex[tokens[0]]]
    
    
def branch(original, slotname, fillerconcept):
    print 'branch %r' % str(fillerconcept)
    clone = copy.deepcopy(original)
    clone.slots[slotname] = fillerconcept
    
    return clone

def exclude(collection, element):
    collection.remove(element)
    return collection
    
def do(instance, unassigned_concepts, unfilled_slotnames, level = 0):
    
    print 'do'
    print level
    print instance
    print unassigned_concepts
    print unfilled_slotnames
    
    if len(unassigned_concepts) == 0 or len(unfilled_slotnames) == 0:
        return instance
    
    return [do(branch(instance, unfilled_slotnames[0], c), exclude(copy.copy(unassigned_concepts), c), copy.copy(unfilled_slotnames)[1:], level +1)
            for c in unassigned_concepts]
        
     