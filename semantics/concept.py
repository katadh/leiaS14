from semantics.slot import Slot


"This is a base class for all concepts specified in knowledge.ontology"
class Concept(object):
    
    
    @classmethod
    def slots(cls):
        return dict(filter(lambda (k, v): isinstance(v, Slot), vars(cls).items()))
    
    
    def filled(self):
        return reduce(lambda s1, s2: s1.filler and s2.filler, 
                      self.slots()) if len(self.slots()) > 0 else True 
        
        
    def __str__(self):
        return '{0}-{1}: {{{2}}}'.format(str(self.__class__.__name__), 
                                         id(self), 
                                         ", ".join(map(lambda slotname: '{0}: {1}'.format(slotname, 
                                                                                          str(self.slots()[slotname])), 
                                                       self.slots())))   