import tourMap
from knowledge.ontology_alexnut import *

def give_directions(TMR):
    tmap = tourMap.Map("plan_selection/graph.json")

    loc = grab_instance(Location, TMR).name
    current_loc = get_current_location()

    print tmap.giveDirections(current_loc, loc)

def give_location(TMR):
    loc = get_current_location()
    response = "You are currently at " + loc
    print response

def get_current_location():
    return "Union"

def grab_instance(cls, tmr):
    try:
        return filter(lambda i: isinstance(i, cls),
                      tmr)[0]
    except:
        return None

def give_forecast(TMR):
    print "good"

def give_information(TMR):
    print "here is some info"

plan_lexicon = [(set(['Person', 'ChangeLocation', 'Question', 'Location']), 'give_directions'),
                (set(['Being', 'RequestInfoLocation', 'Location']), 'give_directions'),
                (set(['Position', 'RequestInfoLocation', 'Person']), 'give_location'),
                (set(['Desire', 'Person', 'Observe', 'Location']), 'give_directions'),
                (set(['Desire', 'Person', 'Know', 'Location']), 'give_information'),
                (set(['Being', 'Weather', 'Question']), 'give_forecast')]

plan_map = {'give_directions':(1, 1, 0, give_directions),
            'give_forecast':(1, 1, 0, give_forecast),
            'give_information':(1, 1, 0, give_information),
            'give_location':(1, 1, 0, give_location)}

plan_map_prereqs = {'give_directions':[[None, None, None]],
                    'give_forecast':[[None, None, None]],
                    'give_inforamtion':[[None, None, None]],
                    'give_location':[[None, None, None]]}

