from semantics.concept import Concept
from semantics.slot import Slot

def ConceptType(name, bases, slots):
    return type(name, bases, slots)

class SpaceTime(Concept):
    pass


### roughly, NN
class Thing(SpaceTime):
    def __init__(self):
        self.init_slots()
        
class Person(Thing):
    name = 'Bob'
    #age = 0
    #gender = ''
    #residence = Slot(Residence)
    #workplace = Slot(Workplace)
    ##spouse = Slot(Person)    
    
    def __init__(self):
        self.init_slots() 
         
class Location(Thing):
    longitude = 0
    latitude = 0
    stay = 0
    #visits = 0
    #notes = ''
    
    def __init__(self):
        self.init_slots()
        
class Workplace(Location):
    def __init__(self):
        self.init_slots()
        
class Residence(Location):
    def __init__(self):
        self.init_slots()
        
#class Transport(Thing):
    #speed = 0
    #cost = 0
    
    
#class Organization(Thing):
    #branch = Slot(Location)
    #employee = Slot(Person)
    #owner = Slot(Person)
    
class Time(SpaceTime):
    start = 0
    end = 0
        
        
### roughly, VB
class Event(SpaceTime):
    def __init__(self):
        self.init_slots()
        
class AgentWakeEvent(Event):
    where = Slot(Location)
    def __init__(self):
        self.init_slots()
        
class MoveEvent(Event):
    to = Slot(Location)
    def __init__(self):
        self.init_slots()
                
class BeingEvent(Event):
    agent = Slot(SpaceTime)   
    def __init__(self):
        self.init_slots()
        
### Quite meta things
class ProtoEvent(Event):
    object = Slot(Event)
    def __init__(self):
        self.init_slots()
        
class DefineEvent(Event):
    base = Slot(Concept)
    definition = Slot(Concept)
    def __init__(self):
        self.init_slots()
        
class Definition(Concept):
    definition = Slot(Location)
    def __init__(self):
        self.init_slots()
###

        
class Life(Event):
    def __init__(self):
        self.init_slots()
               
class Activity(Event):
    location = Slot(Location)
    time = Slot(Time)
    participant = Slot(Person)
    #period = None
    #note = ''
    
    def __init__(self):
        self.init_slots() 
        
class LeisureActivity(Activity):
    def __init__(self):
        self.init_slots()

class QuotidienActivity(Activity):
    def __init__(self):
        self.init_slots()
        

# Activity
class Meal(Event):
    def __init__(self):
        self.init_slots()
        
class WorkActivity(Activity):
    #job = ''
    #priority = 0
    #employer = Slot(Organization)
    def __init__(self):
        self.init_slots()     
    
    
class TravelActivity(Activity):
    ### TODO: if go stopped working uncomment these two
    #Activity.location = None
    #destination = Slot(Location)
    
    #origin = Slot(Location)
    #means = Slot(Transport)
    
    def __init__(self):
        self.init_slots()  
      
class Questionable(Concept):
    pass
        
class Question(Concept):
    theme = Slot(SpaceTime)
    #subject = Slot(Concept)
    #object = Slot(Concept)
    
    def __init__(self):
        self.init_slots()

class What(Questionable):
    object = Slot(SpaceTime)
    
    def __init__(self):
            self.init_slots()    
    
class Wh(Concept):
    pass

class Where(Location, Wh):
    def __init__(self):
        self.init_slots()

class When(Time, Wh):
    def __init__(self):
        self.init_slots()
               


    

    
#class Communication(Event):
    #agent = Slot(Person)
    #theme = Slot(Concept)
    #patient = Slot(Person)
    
#class Informing(Communication):
    #pass

#class Inquiry(Communication):
    #pass

#class AgentTask(WorkActivity):
    #patient = Slot(Person)
    
#class RemindTask(AgentTask):
    #message = ''

#class Command(Communication):
    #theme = Slot(AgentTask)
    

    