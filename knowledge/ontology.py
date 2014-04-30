import sys
sys.path.insert(0, '..')

from semantics.concept import Concept
from semantics.slot import Slot


"We agreed with Kyle that class declarations shall represent concepts while a class instance corresponds to a concept instance"

### The hierarchy is organized in a depth-first fashion, please keep it all neat

### roughly, JJ
class Quality(Concept):
    pass

class Good(Quality):
    pass

class Bad(Quality):
    pass


### roughly, NN
class Thing(Concept):
    pass

class Animal(Thing):
    pass

class Fish(Animal):
    pass

class Person(Animal):
    name = 'Bob'

class Product(Thing):
    quality = Slot(Quality)
    
class Milk(Product):
    pass
    
    
### roughly, VB
class Event(Concept):
    pass

class ChangeEvent(Event):
    theme = Slot(Thing)
    result = Slot(Quality)

class TravelEvent(Event):
    pass





### it is a legacy concept for debug purposes
class Buy(Concept):
    # TODO: potential bug - the same slot object will be used for all instances,
    # although in the linking code concepts get deeply cloned rather than instantiated
    theme = Slot(Animal)



















 
    
class Event(Concept):
    theme = Slot(Fish)
    agent = Slot(Animal)

    
class BuyEvent(Event):
    pass


class FishEvent(Event):
    theme = Slot(Fish)
    
    
class QuestionEvent(Event):
    pass
