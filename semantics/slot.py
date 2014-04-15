from typed import Typed

""
class Slot(Typed):
    #remember to allow slot inheritance
    filler = None
    
    
    def __init__(self, type):
        self.type = type
    
    
    def fill(self, filler):
        
        print 'fill ' + str(filler.type) + ' ' + str(self.type) + ' ' + str(filler.type == self.type)
        
        if filler.type == self.type:
            self.filler = filler
            
            return True
        
        else:
            return False
    
    
    def __str__(self):
        return str(self.type)