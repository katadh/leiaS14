from semantics.concept import Concept
from semantics.slot import Slot

def ConceptType(name, bases, slots):
    return type(name, bases, slots)

## NN

class Location(Concept):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument!=[]:
            self.name=argument[0]
            
     
class Person(Concept):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument!=[]:
            self.name=argument[0]

### VB

class Event(Concept):
    def __init__(self):
        self.init_slots()

class Observe(Event):
    theme = Slot(Location)
    def __init__(self):
        self.init_slot()
        
class Desire(Event):
    theme = Slot(Concept)
    agent = Slot(Person)
    def __init__(self):
        self.init_slot()
        
class Question(Event):
    theme = Slot(Event)
    agent = Slot(Person)
    def __init__(self):
        self.init_slots()

class RequestInfo(Event):
    theme = Slot(Location)
    agent = Slot(Person)
    def __init__(self):
        self.init_slots()

class Position(Location):
    def __init__(self):
        self.init_slots()
