from ontology_petrjay import *
import knowledge.Facts as fr
import lexicon

"Basically pulls a primed instance from FR and all its filler instances recursively"
def recover_context(concepts, instance = None):
    if instance:
        return ([instance.__class__] if not filter(lambda c: 
                                                   c.at_least(instance.__class__), 
                                                   concepts) else []) + sum([recover_context(concepts, filler) 
                                                                             for filler in filter(lambda f: f,
                                                                                                  map(lambda s: s.filler,
                                                                                                      instance.slots().values()))], 
                                                                            [])
    else:
        matches = fr.kblookup('DefineEvent')
        if matches and not filter(lambda c: c.at_least(DefineEvent),
                                  concepts):
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
            [BeingEvent, ProtoEvent, DefineEvent]
        },
        'call': {
            'VBP' :
            [DefineEvent]
        },
        'do' : {
            'VBP':
            [ProtoEvent, Activity]
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
        },
        'it' : {
            'PRP' :
            [Concept]
        },
        'a' : {
            'DET' :
            []
        },
        'the' : {
            'DET' :
            []
        },
        'can' : {
            'VBP' :
            [Question]
        },
    }
    
    def senses(self, *args):
        senses = super(Lexicon, self).senses(*args)
        
        matches = fr.kblookup('DefineEvent')

        if senses != None or not matches:
            return senses
        else:
            lemma = args[0]
            define = matches[0]
            
            
            if lemma == 'it' or lemma == 'this':
                return [define.base.filler.__class__]
            if not define.definition.filler and lemma != '.':
           
                new_concept = ConceptType(lemma.capitalize(), (define.base.filler.__class__,), {})
                define.definition.filler = new_concept()
                
                self.lexicon[lemma] = {}
                self.lexicon[lemma]['NOPOS'] = [new_concept]
            
                return [new_concept]
        
    
    
    def sense_assignments(self, tagged_words):
        permute_senses = self.permute_senses(tagged_words)
        
        for concepts in permute_senses:
            concepts += recover_context(concepts)
            
        return permute_senses