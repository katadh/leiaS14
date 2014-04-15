from typed import Typed

class Instance(Typed):
    slots = {}
    def __init__(self, type): 
        self.type = type
        self.slots = type.slots
        
        print 'instance ' + str(self.type) + ' slots ' + ' '.join(map(lambda s: str(s + ':' + str(self.slots[s])), self.slots))
    
        
    def filled(self):
        
        #print 'filled' + ' ' + ' '.join(map(lambda s: 'True' if s.filler else 'False', self.slots.values())) + ' ' + 'True' if reduce(lambda s1, s2: s1.filler and s2.filler, self.slots.values()) else 'False'
        
        return reduce(lambda s1, s2: s1.filler and s2.filler, self.slots.values()) if len(self.slots) > 0 else True
    
    def __str__(self):
        return str(self.type) + ' : ' + ' '.join(map(lambda s: str(s + ':' + str(self.slots[s])), self.slots))