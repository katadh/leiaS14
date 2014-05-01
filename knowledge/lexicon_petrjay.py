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
        'work' : {
            'NN' :
            [Workplace]
        }
    }