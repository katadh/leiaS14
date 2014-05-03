def all_slots(linking):
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


def all_linked(linking):
        return all(map(lambda instance: 
                       is_filler(instance, linking) or is_filled(instance), 
                       linking))    
        

class Heuristics(object):
    relaxation = -1
    
    @classmethod
    def goodness(cls, linking):
        goodness = 1.0 * all_linked(linking)
        print 'Linking: {0}, goodness: {1}'.format(map(str, linking), goodness)
        return goodness
    
    @classmethod
    def best(cls, linkings):
        print 'Choosing the best linking...'
        return sorted(linkings, key = lambda l: cls.goodness(l))[0]