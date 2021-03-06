import sys
sys.path.insert(0, '..')

from semantics.concept import Concept
from semantics.slot import Slot


"We agreed with Kyle that class declarations shall represent concepts while a class instance corresponds to a concept instance"

### The hierarchy is organized in a depth-first fashion, please keep it all neat

### roughly, JJ
class Quality(Concept):
    def __init__(self):
        self.init_slots()

class Good(Quality):
    def __init__(self):
        self.init_slots()

class Bad(Quality):
    def __init__(self):
        self.init_slots()


### roughly, NN
class Thing(Concept):
    def __init__(self):
        self.init_slots()

class Animal(Thing):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument !=[]:
            self.name = argument[0]

class Fish(Animal):
    def __init__(self):
        self.init_slots()

class Person(Animal):
    name = 'Bob'
    
    def __init__(self):
        self.init_slots()    
    
class Product(Thing):
    def __init__(self):
        self.init_slots()
    
class Milk(Product):
    freshness = Slot(Quality)
    
    def __init__(self):
        self.init_slots()    

class Chips(Product):
    def __init__(self):
        self.init_slots()

class Aisle(Thing):
    location_of = Slot(Product)
    
    def __init__(self):
        self.init_slots()    
    
    
### roughly, VB
class Event(Concept):
    def __init__(self):
        self.init_slots()

class ChangeEvent(Event):
    theme = Slot(Thing)
    result = Slot(Quality)
    
    def __init__(self):
        self.init_slots()    

class QuestionEvent(Event):
    theme = Slot(Concept)
    
    def __init__(self):
        self.init_slots()    
    
class ActiveEvent(Event):
    agent = Slot(Thing)
    theme = Slot(Concept)
    
    def __init__(self):
        self.init_slots()    

class TravelEvent(ActiveEvent):
    def __init__(self):
        self.init_slots()

class BuyEvent(ActiveEvent):
    def __init__(self):
        self.init_slots()


class FishEvent(ActiveEvent):
    # THIS IS HOW YOU OVERRIDE A SLOT, RESPECTS TO NUT!!!
    ActiveEvent.theme = Slot(Fish) 
    
    def __init__(self):
        self.init_slots()    





### it is a legacy concept for debug purposes
class Buy(Concept):
    theme = Slot(Animal)
    
    def __init__(self):
        self.init_slots()    

    
#class Event(Concept):
    #theme = Slot(Fish)
    #agent = Slot(Animal)

    

    
    

