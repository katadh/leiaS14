from ontology_alexnut import *

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
              'PRP': [ (Person,[""])]
             },
        'sage-dining-hall': { 
            'NN' : [ (Location,["Sage-Dining-Hall"]) ]
            },
        'commons':{
            'NN' : [ (Location,["Commons"]) ]
            },
        'amos-eaton':{
            'NN' : [ (Location,["Amos-Eaton"]) ]
            },
        'lally-building':{
            'NN' : [ (Location,["Lally-Building"]) ]
            },
        'dcc':{
            'NN' : [ (Location,["DCC"]) ]
            },
        'jec':{
            'NN' : [ (Location,["JEC"]) ]
            },
        'carnegie-hall':{
            'NN' : [ (Location,["Carnegie-Hall"]) ]
            },
        'union':{
            'NN' : [ (Location,["Union"]) ]
            },
        'vcc':{
            'NN' : [ (Location,["VCC"]) ]
            },
        'empac':{
            'NN' : [ (Location,["EMPAC"]) ]
            },
        'folsom-library':{
            'NN' : [ (Location,["Folson-Library"]) ]
            },
        'mueller-center':{
            'NN' : [ (Location,["Mueller-Center"]) ]
            },
        '86-field':{
            'NN' : [ (Location,["86-Field"]) ]
            },
        'bray':{
            'NN' : [ (Location,["Bray"]) ]
            },
        'quad':{
            'NN' : [ (Location,["Quad"]) ]
            },
        'dining':{
            'NN' : [ (Location,["dining"]) ]
            },
        'academic':{
            'NN' : [ (Location,["academic"]) ]
            },
        'social':{
            'NN' : [ (Location,["social"]) ]
            },
        'athletic':{
            'NN' : [ (Location,["athletic"]) ]
            },
        'library':{
            'NN' : [ (Location,["library"]) ]
            },
        'dorm':{
            'NN' : [ (Location,["dorm"]) ]
            },
        'how':{
            'WHB' : [ (RequestInfo,[]) ]
            },
        'where':{
            'WHB' : [ (RequestInfo,[]) ]
            },
        'see':{
            'VRB' : [ (Observe,[]) ]
            },
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

    def permute_argument(self, tagged_words):
        if len(tagged_words) == 0:
            return [[]]

        
