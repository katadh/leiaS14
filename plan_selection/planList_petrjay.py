from knowledge.ontology_petrjay import *
import knowledge.Facts as fr

current_location = None

### is called when nothing happens
def observe(tmr):
    print 'observe:'
    global current_location
    
    wake = grab_instance(AgentWakeEvent, tmr)
    
    if wake:
        current_location = wake.where.filler
        fr.store(current_location)
    else: 
        current_location.stay += 1
        
    print 'Staying at {0} ({1}, {2}) for {3} turns'.format(current_location, 
                                                           current_location.longitude, 
                                                           current_location.latitude, 
                                                           current_location.stay)
    if current_location.stay > 3 and current_location.__class__ == Location:
        print 'You seem to be spending quite some time here.'
        ask_define_location([current_location])


### NOT A PLAN
def ask_define_location(tmr):
    global current_location
    
    # expect DefineEvent next
    define = DefineEvent()
    define.base.fill(current_location)
    
    # store in short-term
    print 'storing define'
    print define    
    fr.store(define, True)
    
    print 'What is this place called?'
    
    
def on_move(tmr):
    print 'on_move'
    global current_location
    
    current_location = grab_instance(MoveEvent, tmr).to.filler    
    
    print 'Moved to {0} ({1}, {2}])'.format(current_location, 
                                            current_location.longitude, 
                                            current_location.latitude)
    
    loc_matches = filter(lambda loc: 
                         loc.longitude == current_location.longitude and loc.latitude == current_location.latitude, 
                         fr.kblookup('Location'))
    
    if (loc_matches):
        current_location = loc_matches[0]
        print 'Aha! Checking-in at {0}'.format(current_location)
        
    else:
        fr.store(current_location)
        
        
def on_whereis(tmr):
    print 'on_where_is'
    global current_location
    print 'You are at ({0}, {1}), %username%.'.format(current_location.longitude, current_location.latitude)
    print 'I don\'t know what this place is.' if current_location.__class__ is Location else 'It\'a {0}.'.format(current_location.__class__.__name__)


def on_define(tmr):
    print 'on_define'
    definition = grab_instance(DefineEvent, tmr).definition.filler
    define = fr.kblookup('DefineEvent')[0]
    base = define.base.filler
    
    
    if definition.at_least(Location):
        global current_location

        definition.longitude = base.longitude
        definition.latitude = base.latitude
        definition.stay = base.stay
        
        current_location = definition
 
    
    fr.store(definition)
    print 'forgetting define'
    
    fr.forget(define.base.filler)
    fr.forget(define)
    
    
    
### HELPER
def grab_instance(cls, tmr):
    try:
        return filter(lambda i: isinstance(i, cls),
                      tmr)[0]
    except:
        return None
    

    


plan_lexicon = [(set(['AgentWakeEvent']), 'observe'),
                (set(['MoveEvent']), 'on_move'), 
                (set(['Where', 'BeingEvent']), 'on_whereis'),
                (set(['DefineEvent']), 'on_define')]

plan_map = {'observe':(1, -1, 0, observe),
            'on_define':(0, 1, 0, on_define),
            'on_move':(0, 1, 0, on_move),
            'on_whereis':(0, 1, 0, on_whereis)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'on_define': [[None, None, None]],
                    'on_move': [[None, None, None]],
                    'on_whereis' : [[None, None, None]]}



