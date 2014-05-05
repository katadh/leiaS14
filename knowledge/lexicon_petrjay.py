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
            [BeingEvent, ProtoEvent]
        },
        'do' : {
            'VBP':
            [ProtoEvent]
            },        
        'work' : {
            'NN' :
            [Workplace],
            'VBP' :
            [WorkActivity]
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
        },
        'place' : {
            'NN' :
            [Location]
        },
        'home' : {
            'NN':
            [Residence]
        }, 
        'laundry' : {
            'NN':
            [QuotidienActivity]
        }
    }
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)

        if not fr.kblookup('DefineEvent'):
            return senses
        else:
            lemma = args[0]
            new_concept = ConceptType(lemma.capitalize(), (fr.kblookup('DefineEvent')[0].base.filler.__class__,), {})
            
            self.lexicon[lemma] = {}
            self.lexicon[lemma]['NOPOS'] = [new_concept]
        
            return [new_concept]