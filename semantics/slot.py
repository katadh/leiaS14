from heuristics import * 

""
class Slot(object):
    filler_class = None
    filler = None
    #remember to allow slot inheritance
    
    
    def __init__(self, filler_class):
        self.filler_class = filler_class
    
    
    def fill(self, filler):
        if filler.at_least(self.filler_class) and filler.taxonomic_distance(self.filler_class) <= Heuristics.relaxation:
            self.filler = filler
            
            return True
        
        else:
            return False
            
    
    def __str__(self):
        return '{{filler_class: {0}, filler: {1}-{2}}}'.format(self.filler_class.__name__, 
                                                           self.filler.__class__.__name__, 
                                                           id(self.filler))