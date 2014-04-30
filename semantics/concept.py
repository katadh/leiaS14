from slot import Slot
from relaxation import *


"This is a base class for all concepts specified in knowledge.ontology"
class Concept(object):
    
    
    @classmethod
    def slots(cls):
        slots = filter(lambda (k, v): isinstance(v, Slot), vars(cls).items())
        
        for base in cls.__bases__:
            if not base is object:
                slots = slots + base.slots().items()
           
        return dict(slots)   
    
    
    def filled(self):
        return reduce(lambda s1, s2: s1.filler and s2.filler, 
                      self.slots()) if len(self.slots()) > 0 else True 
    
    @classmethod
    def at_least(cls, other_class): 
        if cls == other_class:
            return True
        
        if cls == Concept:
            return False
        
        for base in cls.__bases__:
            if base.at_least(other_class):
                return True
            
        return False
                
        
        
    def __str__(self):
        return '{0}-{1}: {{{2}}}'.format(str(self.__class__.__name__), 
                                         id(self), 
                                         ", ".join(map(lambda slotname: '{0}: {1}'.format(slotname, 
                                                                                          str(self.slots()[slotname])), 
                                                       self.slots())))   