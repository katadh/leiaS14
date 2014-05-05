from ontology_petrjay import *
import knowledge.Facts as fr
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
            [BeingEvent]
            },
        'work' : {
            'NN' :
            [Workplace],
            'VBP' :
            [WorkActivity]
        }, 
        'do' : {
            'VBP':
            [Activity]
        },
        'what' : {
            'WRB' :
            [What]
        },
        'where' : {
            'WRB' :
            [Where]
        },
        'when' : {
            'WRB' :
            [When]
        },
        '?': {
            'Punc': 
            [Question]
        },
        'lunch' : {
            'NN' : 
            [Meal]
        }
    }
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)

        if not fr.kblookup('DefineEvent'):
            return senses
        else:
            lemma = args[0]
            new_concept = ConceptType(lemma.capitalize(), (Concept,), {})
            
            self.lexicon[lemma] = {}
            self.lexicon[lemma]['NOPOS'] = [new_concept]
        
            return [new_concept]