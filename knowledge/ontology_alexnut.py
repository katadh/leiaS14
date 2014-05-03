from semantics.concept import Concept
from semantics.slot import Slot

def ConceptType(name, bases, slots):
    return type(name, bases, slots)


## NN

class Building(Concept):
    def __init__(self):
        self.init_slots()
     
class DiningHall(Building):
    
    def __init__(self):
        self.init_slots() 

class Dorm(Building):
    def __init__(self):
        self.init_slots()

class AcademicBuilding(Building):
    def __init__(self):
        self.init_slots()