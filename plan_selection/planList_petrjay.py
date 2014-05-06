from knowledge.ontology_petrjay import *
import knowledge.Facts as fr
from pprint import pprint
import os

class Clock(object):
    quarters = 0
    
    def tick(self):
        self.quarters = (self.quarters + 1) % 96
        print self
        
    def __str__(self):
        normalize = lambda h: h if h > 9 else "0" + str(h)
        return '{0}:{1}'.format(normalize(self.quarters / 4), 
                                normalize(self.quarters % 4 * 15))
    
    
current_location = None
current_activity = None
clock = Clock()


        

### is called when nothing happens
def observe(tmr):
    global clock
    global current_location
    global current_activity
    
    wake = grab_instance(AgentWakeEvent, tmr)
    
    if wake:
        current_location = wake.where.filler
        fr.store(current_location)
    else: 
        current_location.stay += 1    
    refresh()
    clock.tick()
    print 'Staying at {0} for {1} quarters'.format(current_location, 
                                                   current_location.stay)
    # if idle at an unknown loc
    if current_location.stay > 3 and current_location.__class__ == Location:
        print 'You seem to be spending quite some time here.'
        ask_define_location([current_location])
        return
    
    # if idle with no known activity
    if current_location.stay > 7 and not current_activity:
        print 'I see you\'re doing something.'
        ask_define_activity([current_activity])
        return
    
    # if idle with a known activity for too long
    if current_location.stay > 96 and current_activity:
        print 'Wow, you seem really into it. Are you still doing {0}, %username%?'.format(current_activity)
        return    


### NOT A PLAN
def ask_define_location(tmr):
    global current_location
    
    # expect DefineEvent next
    if not fr.kblookup('DefineEvent'):
        define = DefineEvent()
        define.base.fill(current_location)
        
        # store in short-term   
        fr.store(define, True)
    
    print 'What is this place called?'
    
def ask_define_activity(tmr):
    global current_location
    global current_activity
    global clock
    
    activity = Activity()
    activity.time.fill(Time())
    activity.time.filler.start = clock.quarters
    activity.location.fill(current_location)
    activity.participant.fill(Person())
    
    if not fr.kblookup('DefineEvent'):
        define = DefineEvent()
        define.base.fill(activity)
    
        fr.store(define, True)      
    
    print 'What is that you are doing, %username%?'
    
def on_define(tmr):
    definition = grab_instance(DefineEvent, tmr).definition.filler
    define = fr.kblookup('DefineEvent')[0]
    base = define.base.filler
    
    if definition.at_least(Location):
        global current_location

        definition.longitude = base.longitude
        definition.latitude = base.latitude
        definition.stay = base.stay
        
        current_location = definition
        # need to remove because we already remember this location under a different concept
        fr.forget(define.base.filler)
        
    if definition.at_least(Activity):
        global current_activity
        
        definition.location = base.location
        
        current_activity = definition        
    
    fr.store(definition)
    fr.forget(define)
    
    refresh()
    
    
def on_move(tmr):
    global clock 
    global current_location
    global current_activity
    
    if current_activity:
        current_activity.time.filler.end = clock.quarters
        current_activity = None
    
    current_location = grab_instance(MoveEvent, tmr).to.filler 
    
    refresh()
    clock.tick()
    
    print 'Moved to {0}'.format(current_location)
    
    loc_matches = filter(lambda loc: 
                         loc.longitude == current_location.longitude and loc.latitude == current_location.latitude, 
                         fr.kblookup('Location'))
    
    if (loc_matches):
        current_location = loc_matches[0]
        print 'Aha! Checking-in at {0}'.format(current_location)
        
    else:
        fr.store(current_location)
        
        
def on_whereis(tmr):
    refresh()
    print 'on_where_is'
    global current_location
    print 'I don\'t know what this place is, %username%.' if current_location.__class__ is Location else 'You are at {0}, %username%.'.format(current_location.__class__.__name__)

def on_wh_question(tmr):
    global clock
    refresh()
    question = grab_instance(Question, tmr)
    theme = question.theme.filler
    
    while theme.__class__ == ProtoEvent:
        theme = theme.object.filler
        
    if theme.at_least(Activity):
        if theme.at_least(Wh):
            acts = fr.kblookup('Activity')
            if acts:
                a = sorted(acts, key=lambda a: abs(a.time.filler.start - clock.quarters))[0]
                print '{0} is coming up next {1}.'.format(a.__class__.__name__, a.time.filler)
            else: 
                print 'Either your agenda is clear or you are hiding something from me, %username%.'
                
            
        else:
            wh = filter(lambda f: f.at_least(Wh), 
                        map(lambda s: s.filler, 
                            theme.slots().values()))[0]
            
            if wh.at_least(Location):
                print 'You {0} at {1}, %username%.'.format(theme.__class__.__name__, 
                                                           ', and at '.join(map(lambda a: 
                                                                                str(a.location.filler),
                                                                                fr.kblookup(theme.__class__.__name__))))
            if wh.at_least(Time):
                print 'You {0} {1}, %username%.'.format(theme.__class__.__name__, 
                                                           ', and '.join(map(lambda a: 
                                                                             str(a.time.filler),
                                                                             fr.kblookup(theme.__class__.__name__))))        

    
    
    
### HELPERs
def grab_instance(cls, tmr):
    try:
        return filter(lambda i: isinstance(i, cls),
                      tmr)[0]
    except:
        return None
    
def refresh():
    os.system(['clear','cls'][os.name == 'nt'])
    print 'FR:'
    primed = map(str, fr.kblookup('DefineEvent'))
    if primed:
        print 'Primed:'
        pprint(primed)
    
    locs = map(str, fr.kblookup('Location'))
    if locs:    
        print 'Known Locations:'
        pprint(locs)
        
    acts = map(str, fr.kblookup('Activity'))
    if acts:
        print 'Known Activities:'
        pprint(acts)
        
    ppl = map(str, fr.kblookup('Person')) 
    if ppl:
        print 'Known Persons:'
        pprint(ppl)     
    
    


plan_lexicon = [(set(['AgentWakeEvent']), 'observe'),
                (set(['MoveEvent']), 'on_move'), 
                (set(['Where', 'BeingEvent']), 'on_whereis'),
                (set(['Question', 'Where', 'What', 'When']), 'on_wh_question'),
                (set(['DefineEvent']), 'on_define')]

plan_map = {'observe':(1, -1, 0, observe),
            'on_define':(0, 1, 0, on_define),
            'on_move':(0, 1, 0, on_move),
            'on_whereis':(0, 1, 0, on_whereis),
            'on_wh_question':(0, 1, 0, on_wh_question)}

plan_map_prereqs = {'observe':[[None, None, None]],
                    'on_define': [[None, None, None]],
                    'on_move': [[None, None, None]],
                    'on_whereis' : [[None, None, None]],
                    'on_wh_question' : [[None, None, None]]}



