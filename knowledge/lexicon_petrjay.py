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

        if senses:
            return senses
        #else:
            #lemma = args[0]
            #new_concept = ConceptType(lemma.capitalize(), (Concept,), {})
            
            #self.lexicon[lemma] = {}
            #self.lexicon[lemma]['NOPOS'] = [new_concept]
        
            #return [new_concept]