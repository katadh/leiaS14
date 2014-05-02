current_location = None
stay_duration = 0

def observe(tmr):
    global stay_duration
    print 'stay duration: {0}'.format(stay_duration)
    stay_duration += 1

def ask_define_location(tmr):
    print 'You seem to be spending quite some time here. What is this place?'
    # expect DefineEvent next
    
def on_move(tmr):
    print 'Oh, I see you moved: {0}'.format(tmr[0])


plan_lexicon = [(set(['AgentWakeEvent']), 'observe'),
                (set(['StayEvent', 'Location']), 'ask_define_location'),
                (set(['MoveEvent', 'Location']), 'on_move')]

plan_map = {'observe':(0, -1, 0, observe),
            'ask_define_location':(1, 1, 0, ask_define_location),
            'on_move':(1, 1, 0, on_move)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'ask_define_location': [[None, None, None]],
                    'on_move': [[None, None, None]]}



