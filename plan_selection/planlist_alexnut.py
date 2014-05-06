import tourMap
from knowledge.ontology_alexnut import *

def give_directions(TMR):
    buildingtypes = ["dining", "academic", "social", "athletic", "library", "dorm"]
    bad_weather = ["rainy", "bad"]
    tmap = tourMap.Map("plan_selection/graph.json")

    current_loc = get_current_location()
    [paths, dists] = tmap.findPaths(current_loc)

    loc = grab_instance(Location, TMR).name

    destination = loc
    if loc in buildingtypes:
        min_dist = float("inf")
        for poi in dists:
            if tmap.POI[poi].location_type == loc and dists[poi] < min_dist:
                min_dist = dists[poi]
                destination = poi

    print "You should " + tmap.giveDirections(paths, destination)

    if tmap.POI[destination].outdoors == True:
        weather = get_weather()
        if weather in bad_weather:
            print "However, I should warn you that the weather is supposed to be " + weather + " today."

def give_location(TMR):
    loc = get_current_location()
    response = "You are currently at the " + loc
    print response

def get_current_location():
    return "Union"

def request_desire():
    print "what do you want to see?"

def grab_instance(cls, tmr):
    try:
        return filter(lambda i: isinstance(i, cls),
                      tmr)[0]
    except:
        return None

def give_forecast(TMR):
    forecast = "The weather is supposed to be " + get_weather() + " today"
    print forecast

def get_weather():
    return "rainy"

def give_information(TMR):
    print "here is some info"

def get_time():
    return 12.5

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

