from ontology_petrjay import *
import knowledge.Facts as fr
import lexicon

"Basically pulls a primed instance from FR and all its filler instances recursively"
def recover_context(concepts, instance = None):
    if instance:
        return [instance.__class__] + sum([recover_context(concepts, filler) 
                                           for filler in filter(lambda f: f,
                                                                map(lambda s: s.filler,
                                                                    instance.slots().values()))], 
                                          [])
    else:
        matches = fr.kblookup('DefineEvent')
        if matches:
            define = matches[0]
            return filter(lambda c: 
                          c != define.base.filler.__class__, 
                          recover_context(concepts, define)) + [Concept]         
        if filter(lambda c: c.at_least(Activity),
                  concepts):
            additional = []
            if not filter(lambda c: c.at_least(Location),
                          concepts):
                additional += [Location]
                
            if not filter(lambda c: c.at_least(Time),
                          concepts):
                additional += [Time]  
                
            if not filter(lambda c: c.at_least(Person),
                          concepts):
                additional += [Person]
                            
            return additional
    return []    

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
        'which' : {
            'WRB':
            [Which]
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
        #'home' : {
            #'NN':
            #[Residence]
        #}, 
        'laundry' : {
            'NN':
            [QuotidienActivity]
        },
        'cook' : {
            'VBP' :
            [QuotidienActivity]
        },
        'now' : {
            'ADV':
            [Time]
        }, 
        'here' : {
            'ADV' :
            [Location]
        }
    }
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)

        if senses or not fr.kblookup('DefineEvent'):
            return senses
        else:
            lemma = args[0]
            new_concept = ConceptType(lemma.capitalize(), (fr.kblookup('DefineEvent')[0].base.filler.__class__,), {})
            
            self.lexicon[lemma] = {}
            self.lexicon[lemma]['NOPOS'] = [new_concept]
        
            return [new_concept]
        
    
    
    def sense_assignments(self, tagged_words):
        permute_senses = self.permute_senses(tagged_words)
        
        for concepts in permute_senses:
            concepts += recover_context(concepts)
            
        return permute_senses