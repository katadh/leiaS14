from ontology import *

# TODO: Kyle, feel free to organize it in your way, e.g. using POS as an intermediate key

lex = {'I': [Animal],
       'buy' : [Buy, BuyEvent],
       'fish' : [Fish, FishEvent],
       '?' : [QuestionEvent]}

#TODO: Create a script to read from a text file all of the lexicon entries.

#This is actually really nasty and hardcoding the lexicon like this is tedious. 
#Regardless, the call is lexicon.lexicon[LEMMA][PoS]. This returns a list of concepts associated with the
#      provided lemma and pos.
       
lexicon = {'I': {'PRP': [Animal]},
           'buy': {'NN': [Buy],
                   'VB': [BuyEvent]},
           'fish': {'NN': [Fish], 
                    'VB': [FishEvent]}}


def senses(*args):
    ### by lemma or by lemma and pos
    return lex[args[0]] if len(args) == 1 else lexicon[args[0]][args[1]]

