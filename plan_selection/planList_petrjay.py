def ask_define_location(tmr):
    print 'You seem to be spending quite some time here. What is this place?'
    # expect DefineEvent next

plan_lexicon = [(set(['StayEvent', 'Location']), 'ask_define_location')]
plan_map = {'ask_define_location':(1, 1, 0, ask_define_location)}
plan_map_prereqs = {'ask_define_location': [['', '', None]]}



