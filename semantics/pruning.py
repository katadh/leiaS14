def prune_partially_linked(linking_candidates):
    def all_slots(linking):
        return reduce(lambda s1, s2: 
                      s1 + s2,
                      map(lambda instance: 
                          instance.slots().values(),
                          linking))            


    def is_filler(instance, linking):
        return any(map(lambda slot: 
                       slot.filler == instance,
                   all_slots(filter(lambda other_instance: 
                                    other_instance != instance,
                                    linking))))
    
    
    def is_filled(instance):
        # do we want all slots filled or at least one?
        return any(map(lambda slot: 
                       slot.filler,
                       instance.slots().values()))
            
           
    
    return filter(lambda linking: 
                  all(map(lambda instance: 
                          is_filler(instance, linking) or is_filled(instance), 
                          linking)), 
                  linking_candidates)


pruning_methods = [prune_partially_linked]
def prune(linking_candidates, strength = 0):
    pass