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
                      slots))
        

class Heuristics(object):
    relaxation = 0
    max_relaxation = 10
    minimal_goodness = .00000001
    
    weights = [1., 1.]
    feature_functions = [all_linked, filler_tightness]
    
    @classmethod
    def goodness(cls, linking):
        goodness = 0.
        print 'Linking: {0}'.format(map(str, linking))
        if len(linking) > 0:
            for (w, f) in zip(cls.weights, cls.feature_functions):
                value = f(linking)
                print '{0} = {1}, weight = {2}'.format(f.__name__, value, w)
                goodness += value * w
        
        goodness = 1.0 * all_linked(linking) + 1.0 * filler_tightness(linking)
        print 'Goodness: {0}'.format(goodness)
        return goodness
    
    @classmethod
    def best(cls, linkings):
        print 'Choosing the best linking...'
        return sorted(linkings, 
                      key = lambda l: cls.goodness(l),
                      reverse = True)[0]