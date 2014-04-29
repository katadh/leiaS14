from ontology import *

# TODO: Kyle, feel free to organize it in your way, e.g. using POS as an intermediate key

lex = {'I': [Animal],
       'buy' : [Buy, BuyEvent],
       'fish' : [Fish, FishEvent],
       '?' : [QuestionEvent]}
       #'where' : [location slot]}

#TODO: Create a script to read from a text file all of the lexicon entries.

#This is actually really nasty and hardcoding the lexicon like this is tedious. 
#Regardless, the call is lexicon.lexicon[LEMMA][PoS]. This returns a list of concepts associated with the
#      provided lemma and pos.
       
lexicon = {'I': {'PRP': [Animal]},
           'buy': {'NN': [Buy],
                   'VBP': [BuyEvent]},
           'fish': {'NN': [Fish], 
                    'VBP': [FishEvent]}}


def senses(*args):
    lemma = args[0]
    pos = args[1] if len(args) > 1 else None
    
    if pos:
        return lexicon[lemma][pos]
    else: 
        return reduce(lambda s1, s2: s1 + s2,
                      [lexicon[lemma][pos] 
                       for pos in lexicon[lemma].keys()])
