from knowledge.ontology_petrjay import *
import knowledge.Facts as fr

current_location = None


def observe(tmr):
    global current_location
    
    if tmr:
        current_location = grab_instance('AgentWakeEvent', tmr).where
    else: 
        current_location.stay += 1
        
    print 'Staying at {0} ({1}, {2}) for {3} turns'.format(current_location, 
                                                           current_location.longitude, 
                                                           current_location.latitude, 
                                                           current_location.stay)
    if current_location.stay > 3:
        ask_define_location([current_location])


### NOT A PLAN
def ask_define_location(tmr):
    global current_location
    
    # expect DefineEvent next
    define = DefineEvent()
    define.base = current_location
    
    # store in short-term
    fr.store(define)  
    fr.store(current_location)
    
    print 'You seem to be spending quite some time here. What is this place?'
    
    
def on_move(tmr):
    global current_location
    current_location = grab_instance('Location', tmr).to    
    
    print 'Moved to {0} ({1}, {2}])'.format(current_location, 
                                            current_location.longitude, 
                                            current_location.latitude)
    
    loc_matches = filter(lambda loc: 
                         loc.longitude == current_location.longitude and loc.latitude == current_location.latitude, 
                         fr.kblookup('Location'))
    
    if (loc_matches):
        current_location = loc_matches[0]
        print 'Aha! Checking-in at {0}'.format(current_location)


def on_define(tmr):
    define = grab_instance('DefineEvent', tmr)
    base = define.base
    definition = define.definition
    
    new_location = ConceptType(definition.__class__.__name__, (base.__class__,), {})
    
    new_location.longitude = base.longitude
    new_location.latitude = base.latitude
    new_location.stay = base.stay
    
    fr.store(new_location)
    fr.forget(define)
    fr.forget(base)
    
    
### HELPER
def grab_instance(cls_name, tmr):
    return filter(lambda i: isinstance(i, cls_name),
                  tmr)[0]
    


plan_lexicon = [(set(['AgentWakeEvent', 'Location']), 'observe'),
                (set(['MoveEvent', 'Location']), 'on_move'), 
                (set(['DefineEvent']), 'on_define')]

plan_map = {'observe':(1, -1, 0, observe),
            'on_define':(0, 1, 0, on_define),
            'on_move':(0, 1, 0, on_move)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'on_define': [[None, None, None]],
                    'on_move': [[None, None, None]]}



