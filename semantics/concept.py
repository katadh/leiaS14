from typed import Typed


class Concept(Typed):
    name = None
    slots = None
    
    
    # can't use default slots initialization or the same structure will be shared among all instances
    def __init__(self, name, parent, slots):
        self.name = name
        self.type = parent
        self.slots = slots
        
        
    def __eq__(self, other):
        if isinstance(other, Concept):
            return self.name == other.name
        
        
    def __ne__(self, other):
        return not self.__eq__(other)            
        
        
    def __str__(self):
        return self.name