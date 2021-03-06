### These are just helpers, the actual heuristics are below
def all_slots(linking):
    if len(linking) == 0:
        return []    
    return reduce(lambda s1, s2: 
                  s1 + s2,
                  map(lambda instance: 
                      instance.slots().values(),
                      linking))   

def is_filled(instance):
    # do we want all slots filled or at least one?
    return any(map(lambda slot: 
                   slot.filler,
                   instance.slots().values()))

def is_filler(instance, linking):
    return any(map(lambda slot: 
                   slot.filler == instance,
               all_slots(filter(lambda other_instance: 
                                other_instance != instance,
                                linking))))

#### The actual heuristics 
def all_linked(linking):
        return all(map(lambda instance: 
                       is_filler(instance, linking) or is_filled(instance), 
                       linking))    
    
def filler_tightness(linking):
    slots = all_slots(linking)
    if len(slots) == 0:
        return 0
    return reduce(lambda t1, t2:
                  t1 + t2,
                  map(lambda s: 
                      1./ 2 ** s.filler.taxonomic_distance(s.filler_class),
                      slots)) / len(slots)

def cycles(linking):
    cycles = 0
    for i in linking:
        for s in i.slots().values():
            for s2 in s.filler.slots().values():
                if i == s2.filler:
                    cycles += 1   
    return cycles

def shared_fillers(linking):
    shared = 0
    for i1 in linking:
        for i2 in linking:
            if i1 != i2:
                for s1 in i1.slots().values():
                    for s2 in i2.slots().values():
                        if s1.filler == s2.filler:
                            shared += 1
    return shared
        

class Heuristics(object):
    relaxation = 3
    max_relaxation = 10
    minimal_goodness = .00000001
    
    weights = [1., 1., -1., -1.]
    feature_functions = [all_linked, filler_tightness, cycles, shared_fillers]
    
    @classmethod
    def goodness(cls, linking):
        goodness = 0.
        print '\n{0}'.format(map(str, linking))
        if len(linking) > 0:
            for (w, f) in zip(cls.weights, cls.feature_functions):
                value = f(linking)
                print '{0} = {1}, weight = {2}'.format(f.__name__, value, w)
                goodness += value * w
        
        print 'Goodness: {0}'.format(goodness)
        return goodness
    
    @classmethod
    def best(cls, linkings):
        print 'Choosing the best linking...'
        return sorted(linkings, 
                      key = lambda l: cls.goodness(l),
                      reverse = True)[0]