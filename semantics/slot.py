from relaxation import *

""
class Slot(object):
    filler_class = None
    filler = None
    #remember to allow slot inheritance
    
    
    def __init__(self, filler_class):
        self.filler_class = filler_class
    
    
    def fill(self, filler):
        
        #print 'filling slot {0} with filler type: {1}, success: {2}'.format(str(self), str(filler.type), str(filler.type == self.type))
        
        if filler.at_least(self.filler_class):
            self.filler = filler
            
            return True
        
        else:
            return False
            
    
    def __str__(self):
        return '{{filler_class: {0}, filler: {1}}}'.format(str(self.filler_class), str(self.filler))