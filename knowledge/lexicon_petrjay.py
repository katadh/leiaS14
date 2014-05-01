from ontology_petrjay import *

import lexicon

class Lexicon(lexicon.Lexicon):
    lexicon = {
        'i': {
            'PRP': 
            [Person]
            },
        'go' : {
            'VB':
            [TravelActivity]
        },
        'be': {
            'VB':
            [DefineEvent]
            },
        'work' : {
            'NN' :
            [Workplace]
        }
    }
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)
        lemma = args[0]
        
        return senses if senses else [type(lemma.capitalize(), (Concept,), {})]