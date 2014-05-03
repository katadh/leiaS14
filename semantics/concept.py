from slot import Slot


"This is a base class for all concepts specified in knowledge.ontology"
class Concept(object):
    
    def init_slots(self):
        # so that the initial slot object is not shared by all instances
        class_slots = self.class_slots()
        for slotname in class_slots.keys():
            vars(self)[slotname] = Slot(class_slots[slotname].filler_class)
    
    
    @classmethod
    def class_slots(cls):
        class_slots = filter(lambda (k, v): isinstance(v, Slot), 
                             vars(cls).items())
        
        for base in cls.__bases__:
            if not base is object:
                class_slots = class_slots + base.class_slots().items()
           
        return dict(class_slots)
    
    
    def slots(self):
        return dict(map(lambda class_slot: 
                        (class_slot, vars(self)[class_slot]), 
                        self.class_slots().keys()))  
    
    
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
    
    @classmethod
    def taxonomic_distance(cls, other_class):
        if cls == other_class:
            return 0
        # TODO: yep, inefficient
        if cls.at_least(other_class):
            return 1 + cls.__bases__[0].taxonomic_distance(other_class)
            
            
                
        
        
    def __str__(self):
        return '{0}-{1}: {{{2}}}'.format(self.__class__.__name__, 
                                         id(self), 
                                         ", ".join(map(lambda slotname: 
                                                       '{0}: {1}'.format(slotname, 
                                                                         str(self.slots()[slotname])), 
                                                       self.slots())))   