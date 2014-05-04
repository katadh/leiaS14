from knowledge.ontology_petrjay import *
import knowledge.Facts as fr

current_location = None


def observe(tmr):
    print 'observe:'
    global current_location
    
    if tmr and grab_instance(AgentWakeEvent, tmr):
        current_location = grab_instance(AgentWakeEvent, tmr).where
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
    print 'storing define'
    print define    
    fr.store(define)  
    fr.store(current_location)
    
    print 'You seem to be spending quite some time here. What is this place?'
    
    
def on_move(tmr):
    print 'on_move'
    global current_location
    current_location = grab_instance(MoveEvent, tmr).to    
    
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
    print 'on_define'
    define = grab_instance(DefineEvent, tmr)
    base = define.base.filler
    definition = define.definition.filler
    
    new_location = ConceptType(definition.__class__.__name__, (base.__class__,), {})
    
    new_location.longitude = base.longitude
    new_location.latitude = base.latitude
    new_location.stay = base.stay
    
    fr.store(new_location)
    print 'forgetting define'
    print define
    fr.forget(define)
    print 'base'
    print base
    fr.forget(base)
    
    
### HELPER
def grab_instance(cls, tmr):
    try:
        return filter(lambda i: isinstance(i, cls),
                      tmr)[0]
    except:
        return None
    


plan_lexicon = [(set(['AgentWakeEvent']), 'observe'),
                (set(['MoveEvent']), 'on_move'), 
                (set(['DefineEvent']), 'on_define')]

plan_map = {'observe':(1, -1, 0, observe),
            'on_define':(0, 1, 0, on_define),
            'on_move':(0, 1, 0, on_move)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'on_define': [[None, None, None]],
                    'on_move': [[None, None, None]]}



