from semantics.concept import Concept
from semantics.slot import Slot

class Event(Concept):
    pass

class Thing(Concept):
    pass

class Location(Thing):
    longitude = 0
    latitude = 0
    address = ''
    visits = 0
    notes = ''
    
class Workplace(Location):
    pass

class Residence(Location):
    pass
    
class Person(Thing):
    age = 0
    gender = ''
    residence = Slot(Residence)
    workplace = Slot(Workplace)
    #spouse = Slot(Person)
    
class Transport(Thing):
    speed = 0
    cost = 0
    
    
class Organization(Thing):
    branch = Slot(Location)
    employee = Slot(Person)
    owner = Slot(Person)
    
class Activity(Event):
    location = Slot(Location)
    start_time = 0
    end_time = 0
    participant = Slot(Person)
    period = None
    note = ''
    
class WorkActivity(Activity):
    job = ''
    priority = 0
    employer = Slot(Organization)
    
class LeisureActivity(Activity):
    pass

class QuotidienActivity(Activity):
    pass
    
class TravelActivity(Activity):
    origin = Slot(Location)
    destination = Slot(Location)
    means = Slot(Transport)
    
class Communication(Event):
    agent = Slot(Person)
    theme = Slot(Concept)
    patient = Slot(Person)
    
class Informing(Communication):
    pass

class Inquiry(Communication):
    pass

class AgentTask(WorkActivity):
    patient = Slot(Person)
    
class RemindTask(AgentTask):
    message = ''

class Command(Communication):
    theme = Slot(AgentTask)
    

    