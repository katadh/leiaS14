from concept import Concept
from slot import Slot
from semantics import *
import copy
import itertools
from pprint import pprint


Animal = Concept('Animal', None, {})

#print str(Animal) + ' slots ' + ' '.join(map(lambda s: str(s + ':' + str(Animal.slots[s])), Animal.slots))

Fish = Concept('Fish', Animal, {})

Buy = Concept('Buy', None, {})

#print Animal.slots == Buy.slots

Buy.slots['theme'] = Slot(Animal)

#print Animal.slots == Buy.slots

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

#print str(Animal) + ' slots ' + ' '.join(map(lambda s: str(s + ':' + str(Animal.slots[s])), Animal.slots))
#print str(Buy) + ' slots ' + ' '.join(map(lambda s: str(s + ':' + str(Buy.slots[s])), Buy.slots))
#print map(str, fit('I buy fish'.split(), []))


#print map(lambda c: map(str, c), permutesenses('I buy fish'.split()))
#print map(lambda c: map(str, c), link([BuyEvent, Animal, Fish], [[]]))
#print map(str, link([BuyEvent, Animal, Fish], [[]]))
#print map(lambda c: map(str, c), newFit('I buy fish'.split()))
#candidates = link(map(Instance, [BuyEvent, Fish, Animal]))
#print map(str, itertools.chain(*do(Instance(BuyEvent), [Animal, Fish], BuyEvent.slots.keys())))

pprint(link_linear(map(Instance, [BuyEvent, Fish, Buy, Animal])))