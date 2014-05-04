from knowledge.ontology_petrjay import *
import knowledge.Facts as fr

current_location = None

def observe(tmr):
    global current_location
    
    if tmr:
        current_location = filter(lambda i: isinstance(i, AgentWakeEvent),
                                  tmr)[0].where
    else: 
        current_location.stay += 1
        
    print 'Staying at {0} ({1}, {2}) for {3} turns'.format(current_location, 
                                                           current_location.longitude, 
                                                           current_location.latitude, 
                                                           current_location.stay)
    if current_location.stay > 3:
        ask_define_location([current_location])

def ask_define_location(tmr):
    global current_location
    
    # expect DefineEvent next
    define = DefineEvent()
    define.base = current_location
    fr.store(define)  
    print 'You seem to be spending quite some time here. What is this place?'
    print fr.kblookup('DefineEvent')
    
    
def on_move(tmr):
    global current_location
    current_location = filter(lambda i: isinstance(i, MoveEvent),
                              tmr)[0].to    
    
    print 'Moved to {0} ({1}, {2}])'.format(current_location, 
                                            current_location.longitude, 
                                            current_location.latitude)
    


plan_lexicon = [(set(['AgentWakeEvent', 'Location']), 'observe'),
                (set(['MoveEvent', 'Location']), 'on_move')]

plan_map = {'observe':(1, -1, 0, observe),
            'ask_define_location':(0, 1, 0, ask_define_location),
            'on_move':(0, 1, 0, on_move)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'ask_define_location': [[None, None, None]],
                    'on_move': [[None, None, None]]}



