from ontology import *

### This is the base static lexicon class
### Do not touch it - our app-specific custom lexicons should inherit 
### the access methods from it so that the semantics don't break
### and override the actual lexicon variable.
### Each custom lexicon will import its own ontology.
class Lexicon(object):
    #TODO: Create a script to read from a text file all of the lexicon entries.
    
    #This is actually really nasty and hardcoding the lexicon like this is tedious. 
    #Whoever wrote the above: you are responsible for setting up a nice database interface, yo.    
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
            }
    }

    def senses(self, *args):
        lemma = args[0].lower()
        
        if lemma in self.lexicon.keys():
            pos = args[1] if len(args) > 1 else None
            
            if pos and pos in self.lexicon[lemma].keys():
                return self.lexicon[lemma][pos]
            else: 
                return reduce(lambda s1, s2: s1 + s2,
                              [self.lexicon[lemma][pos] 
                               for pos in self.lexicon[lemma].keys()])
            
            
    ### Generates all possible combinations of token-to-sense mapping
    def permute_senses(self, tagged_words):
        if len(tagged_words) == 0:
            return [[]]
                
        return [[sense] + concepts
                for concepts in self.permute_senses(tagged_words[1:])
                for sense in self.senses(tagged_words[0].lemma,
                                         tagged_words[0].pos)]    
    
    def sense_assignments(self, tagged_words):
        return self.permute_senses(tagged_words)
