from semantics.concept import Concept
from semantics.slot import Slot

def ConceptType(name, bases, slots):
    return type(name, bases, slots)

class Dummy(Concept):
    def __init__(self):
        self.init_slots()

## NN

class Thing(Concept):
    def __init__(self):
        self.init_slots()

class Location(Thing):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument!=[]:
            self.name=argument[0]

class Animal(Concept):
    def __init__(self):
        self.init_slots()
    
class Person(Animal):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument!=[]:
            self.name=argument[0]

class Weather(Thing):
    name = ""
    def __init__(self,argument=[]):
        self.init_slots()
        if argument!=[]:
            self.name=argument[0]

### VB

class Event(Concept):
    def __init__(self):
        self.init_slots()

class ChangeLocation(Event):
    theme = Slot(Location)
    def __init__(self):
        self.init_slots()

class Observe(Event):
    theme = Slot(Location)
    def __init__(self):
        self.init_slots()

class Know(Thing):
    theme = Slot(Concept)
    def __init__(self):
        self.init_slots()

class Desire(Event):
    theme = Slot(Event)
    agent = Slot(Person)
    def __init__(self):
        self.init_slots()
        
class Question(Event):
    theme = Slot(Event)
    def __init__(self):
        self.init_slots()

class RequestInfoLocation(Event):
    theme = Slot(Location)
    def __init__(self):
        self.init_slots()

class RequestInfoWeather(Event):
    theme = Slot(Weather)
    def __init__(self):
        self.init_slots()

class RequestInfo(Event):
    theme = Slot(Concept)
    def __init__(self):
        self.init_slots()

class Position(Location):
    theme = Slot(Person)
    def __init__(self):
        self.init_slots()

class Being(Event):
    theme = Slot(Thing)
    def __init__(self):
        self.init_slots()