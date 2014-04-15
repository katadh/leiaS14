from typed import Typed

""
class Slot(Typed):
    #remember to allow slot inheritance
    filler = None
    
    
    def __init__(self, type):
        self.type = type
    
    
    def fill(self, filler):
        
        print 'filling slot {0} with filler type: {1}, success: {2}'.format(str(self), str(filler.type), str(filler.type == self.type))
        
        if filler.type == self.type:
            self.filler = filler
            
            return True
        
        else:
            return False
    
    
    def __str__(self):
        return '{{type: {0}, filler: {1}}}'.format(str(self.type), str(self.filler))