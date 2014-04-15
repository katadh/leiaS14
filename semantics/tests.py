from concept import Concept
from slot import Slot
from semantics import *
from itertools import chain
from pprint import pprint

Animal = Concept('Animal', None, {})

Fish = Concept('Fish', Animal, {})

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

print 'Possible sense combinations:'
pprint(map(lambda c: map(str, c), permutesenses('I buy fish'.split(), lex)))

print 'Possible slot linking combinations for the FishEvent concept:'
pprint(map(str, chain(*do(Instance(FishEvent), [Animal, Fish], BuyEvent.slots.keys()))))

#pprint(link_linear(map(Instance, [BuyEvent, Fish, Buy, Animal])))