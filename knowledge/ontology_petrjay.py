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
        
        
### roughly, VB
class Event(SpaceTime):
    def __init__(self):
        self.init_slots()
        

        
class BeingEvent(Event):
    agent = Slot(SpaceTime)
    
    def __init__(self):
        self.init_slots()
        
class ProtoEvent(Event):
    object = Slot(Event)
    
    def __init__(self):
        self.init_slots()

        
class Life(Event):
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

#class StayEvent(Event):
    #at = Slot(Location)
    
    #def __init__(self):
        #self.init_slots()
        
class DefineEvent(Event):
    base = Slot(Concept)
    definition = Slot(Concept)
    
    def __init__(self):
        self.init_slots()
        

        
class Activity(Event):
    location = Slot(Location)
    #start_time = 0
    #end_time = 0
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
        

        
class Meal(Activity):
    def __init__(self):
        self.init_slots()
        
class WorkActivity(Activity):
    #job = ''
    #priority = 0
    #employer = Slot(Organization)
    def __init__(self):
        self.init_slots()     
    
    
class TravelActivity(Activity):
    Activity.location = None
    #origin = Slot(Location)
    destination = Slot(Location)
    #means = Slot(Transport)
    
    def __init__(self):
        self.init_slots()  
      
class Questionable(Concept):
    pass
        
class Question(Concept):
    theme = Slot(Questionable)
    
    def __init__(self):
        self.init_slots()

class What(Questionable):
    object = Slot(SpaceTime)
    
    def __init__(self):
            self.init_slots()    
    
    

class Where(Questionable):
    place_of = Slot(Event)
    
    def __init__(self):
        self.init_slots()

class When(Questionable):
    time_of = Slot(Event)
    
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
    

    