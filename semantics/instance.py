from typed import Typed
from copy import deepcopy

class Instance(Typed):
    slots = {}
    
    
    def __init__(self, concept): 
        self.type = concept
        self.slots = concept.slots
        
        #print str(self)
    
        
    def filled(self):
        
        #print 'filled' + ' ' + ' '.join(map(lambda s: 'True' if s.filler else 'False', self.slots.values())) + ' ' + 'True' if reduce(lambda s1, s2: s1.filler and s2.filler, self.slots.values()) else 'False'
        
        return reduce(lambda s1, s2: s1.filler and s2.filler, self.slots.values()) if len(self.slots) > 0 else True 
    
    
    def __str__(self):
        return '{0}-{1}: {{{2}}}'.format(str(self.type), id(self), ", ".join(map(lambda s: '{0}: {1}'.format(s, str(self.slots[s])), 
                                                                                                   self.slots)))