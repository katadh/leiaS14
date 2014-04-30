from ontology import *

#TODO: Create a script to read from a text file all of the lexicon entries.

#This is actually really nasty and hardcoding the lexicon like this is tedious. 

       
lexicon = {
    'I': {
        'PRP': [Animal]
        },
    'milk': { 
        'NN' : [Milk]
        },
    'bad': {
        'JJ': [Bad]
        },
    'buy': {
        'NN': [Buy],
        'VBP': [BuyEvent]
        },
    'fish': {
        'NN': [Fish], 
        'VBP': [FishEvent]
        },
    '?': {
        'Punc': [QuestionEvent]
        },
    'go': {
        'VB': [TravelEvent, ChangeEvent]
        },
    'where': {
        'WRB': [Aisle]
        },
    'chip': {
        'NNS': [Chips]
        }
}
#'where' : [location slot]}


def senses(*args):
    lemma = args[0].lower()
    
    if lemma in lexicon.keys():
        pos = args[1] if len(args) > 1 else None
        
        if pos and pos in lexicon[lemma].keys():
            return lexicon[lemma][pos]
        else: 
            return reduce(lambda s1, s2: s1 + s2,
                          [lexicon[lemma][pos] 
                           for pos in lexicon[lemma].keys()])
