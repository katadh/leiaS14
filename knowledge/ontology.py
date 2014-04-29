import sys
sys.path.insert(0, '..')

from semantics.concept import Concept
from semantics.slot import Slot


"We agreed with Kyle that class declarations shall represent concepts while a class instance corresponds to a concept instance"


class Thing(Concept):
    pass

#class Event(Concept):
    #pass

#class TravelEvent(Event):
    #pass

#class ChangeEvent(Event):
    #pass



#class Product(Thing):
    #pass


#class Milk(Product):
    #pass




class Animal(Thing):
    pass


class Person(Animal):
    name = 'Bob'


class Fish(Animal):
    pass


class Buy(Concept):
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
