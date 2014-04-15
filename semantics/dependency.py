class Dependency(object):
    type = None
    governor = None
    dependent = None
    
    def __init__(self, gov, type, dep):
        self.type = type
        self.governor = gov
        self.dependent = dep
        
    def __str__(self):
        return ' -> '.join([self.governor, self.type, self.dependent])
    
deps = [Dependency("buy", "nsubj", "I"),
        Dependency("buy", "dobj", "fish")]

#print map(str, deps)