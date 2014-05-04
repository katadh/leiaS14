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
              'PRP': [ (Person,[])]
             },
        'sage_dining_hall': { 
            'NN' : [ (Location,["Sage_Dining_Hall"]) ]
            },
        'commons':{
            'NN' : [ (Location,["Commons"]) ]
            },
        'amos_eaton':{
            'NN' : [ (Location,["Amos_Eaton"]) ]
            },
        'lally_building':{
            'NN' : [ (Location,["Lally_Building"]) ]
            },
        'dcc':{
            'NN' : [ (Location,["DCC"]) ]
            },
        'jec':{
            'NN' : [ (Location,["JEC"]) ]
            },
        'carnegie_hall':{
            'NN' : [ (Location,["Carnegie_Hall"]) ]
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
        'folsom_library':{
            'NN' : [ (Location,["Folson_Library"]) ]
            },
        'mueller_center':{
            'NN' : [ (Location,["Mueller_Center"]) ]
            },
        '86_field':{
            'NN' : [ (Location,["86_Field"]) ]
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
            'WHB' : [ (Question,[]) ]
            },
        'where':{
            'WHB' : [ ( RequestInfoLocation ,[]) ]
            },
        'see':{
            'VRB' : [ (Observe,[]) ],
            'VB' : [ (Observe,[]) ]
            },
        'weather':{
            'NN' : [ (Weather,[])]
            },
        'be':{
            'VBP' : [ (Position,[]),(Being,[])]
            },
        'would':{
            'MD' : [ (Desire,[]) ]
            },
        'want':{
            'VBP' : [ (Desire,[])]
            },
        'get':{
            'VB' : [(ChangeLocation,[])]
            },
        'go':{
            'VB' : [(ChangeLocation,[])]
            },
        'move':{
            'VB' :[ (ChangeLocation,[])]
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

    def permute_argument(self, tagged_words):
        if len(tagged_words) == 0:
            return [[]]

        
