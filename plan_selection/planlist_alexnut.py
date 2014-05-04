plan_lexicon = [(set(['Person', 'ChangeLocation', 'Question', 'Location']), 'give_directions'),
                (set(['Being', 'RequestInfoLocation', 'Location']), 'give_directions'),
                (set(['Position', 'RequestInfoLocation', 'Person']), 'give_location'),
                (set(['Desire', 'Person', 'Observe', 'Location']), 'give_directions'),
                
                (set(['Being', 'Weather', 'Question']), 'give_forecast')]

plan_map = {'give_directions':(1,1,0,give_directions),
            'give_forecast':(1,1,0,give_forecast)}

plan_map_prereqs = {'give_directions':[[None, None, None]],
                    'give_forecast':[[None, None, None]]}
