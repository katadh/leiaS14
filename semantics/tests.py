from concept import Concept
from slot import Slot
from semantics import *
from itertools import chain
from pprint import pprint

Animal = Concept('Animal', None, {})

Fish = Concept('Fish', Animal, {})
Fish.slots["owner"] = Slot(Animal)
#Whale = Concept('Fish',Animal, {})

Buy = Concept('Buy', None, {})
Buy.slots['theme'] = Slot(Animal)

Event = Concept('Event', None, {})

FishEvent = Concept('FishEvent', Event, {})
FishEvent.slots['theme'] = Slot(Fish)
FishEvent.slots['agent'] = Slot(Animal)

BuyEvent = Concept('BuyEvent', Event, {})
BuyEvent.slots['theme'] = Slot(Animal)
BuyEvent.slots['agent'] = Slot(Animal)

lex = {'I': [Animal],
       'buy' : [Buy, BuyEvent],
       'fish' : [Fish, FishEvent]}


sense_assignments = permutesenses('I buy fish'.split(), lex)

for sense in sense_assignments:
    temp =""
    for concept in sense:
        temp = temp+" "+ str(concept)
        for key in concept.slots:
            print key +" : " + str(concept.slots[key])
    print temp
    
print 'Possible sense assignment combinations:'
pprint(map(lambda senses: map(str, senses), 
           sense_assignments))
print "*** Here ***"

#sdf = fill_all_slot(Buy,[Instance(Animal),Instance(Fish)])

listOfAll = findAllLinking([Animal, FishEvent, Fish, Animal])

### just a print format
for i in listOfAll:
    temp = ""
    for j in i:
        temp =temp +" ["+ str(j) +"] \n"
    print temp
        
print "********"

single_instance_linkings = [link_single(Instance(Buy), [Animal, Fish], Buy.slots.keys())]
print
print 'Possible slot linking combinations for the FishEvent concept:'
pprint(map(str, 
           filter(lambda instance: instance.filled(), 
                  chain(*single_instance_linkings))))

#pprint(link_each(map(Instance, 
                     #[BuyEvent, Fish, Buy, Animal])))