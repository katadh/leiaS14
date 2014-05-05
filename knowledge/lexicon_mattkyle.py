
from ontology_mattkyle import *

import lexicon

class Lexicon(lexicon.Lexicon):
    lexicon = {
        'i': {
            'PRP': 
            [Animal]
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
            #TODO: BUG WHEN SAY IT'S NOT EXACTLY VBP BUT VBZ
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
            },
		'delivery': {
			'NN':
			[Delivery]
			},
		'much': {
			'advmod':
			[Price]
			},
        'wine': {
            'NNS': 
            [Wines]
            }
		}
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)

        if senses:
            return senses
        #else:
            #lemma = args[0]
            #new_concept = ConceptType(lemma.capitalize(), (Concept,), {})
            
            #self.lexicon[lemma] = {}
            #self.lexicon[lemma]['NOPOS'] = [new_concept]
        
            #return [new_concept]
