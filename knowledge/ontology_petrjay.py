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
    def __str__(self):
        return super(Location, self).__str__() + ' at ({0}, {1})'.format(self.longitude, self.latitude)
        
class Workplace(Location):
    def __init__(self):
        self.init_slots()
        
class Residence(Location):
    def __init__(self):
        self.init_slots()
        
class Time(SpaceTime):
    start = 0
    end = 0
    def __init__(self):
        self.init_slots()
    def __str__(self):
        normalize = lambda h: h if h > 9 else "0" + str(h)
        return '{0}:{1} to {2}:{3}'.format(normalize(self.start / 4), 
                                           normalize(self.start % 4 * 15),
                                           normalize(self.end / 4), 
                                           normalize(self.end % 4 * 15)) if self.end > self.start else ' at {0}:{1}'.format(normalize(self.start / 4), 
                                                                                                                           normalize(self.start % 4 * 15))
        
        
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
    location = Slot(Location)
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

        
class Life(Event):
    def __init__(self):
        self.init_slots()
               
class Activity(Event):
    location = Slot(Location)
    time = Slot(Time)
    participant = Slot(Person)
    def __init__(self):
        self.init_slots() 
        
class LeisureActivity(Activity):
    def __init__(self):
        self.init_slots()

class QuotidienActivity(Activity):
    def __init__(self):
        self.init_slots()
        
# Activity
class Meal(Activity):
    def __init__(self):
        self.init_slots()
        
class WorkActivity(Activity):
    def __init__(self):
        self.init_slots()     
       
class TravelActivity(Activity):
    def __init__(self):
        self.init_slots()  
        
class Question(Concept):
    theme = Slot(SpaceTime)
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
        
class What(Activity, Wh):
    def __init__(self):
            self.init_slots()
        
class Which(SpaceTime, Wh):
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
    

    