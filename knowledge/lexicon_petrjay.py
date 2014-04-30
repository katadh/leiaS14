from ontology_petrjay import *
import lexicon

class Lexicon(lexicon.Lexicon):
    lexicon = {
        'i': {
            'PRP': 
            [Milk]
            },
        'milk': { 
            'NN' : 
            [Milk]
            },
        'bad': {
            'JJ': 
            [Bad]
            },
        'buy': {
            'NN': 
            [Buy],
            'VBP': 
            [BuyEvent]
            },
        'fish': {
            'NN': 
            [Fish], 
            'VBP': 
            [FishEvent]
            },
        '?': {
            'Punc': 
            [QuestionEvent]
            },
        'go': {
            'VB': 
            [TravelEvent, 
             ChangeEvent]
            },
        'where': {
            'WRB': 
            [Aisle]
            },
        'chip': {
            'NNS': 
            [Chips]
            }
    }