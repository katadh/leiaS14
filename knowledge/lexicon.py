from ontology import *

#TODO: Create a script to read from a text file all of the lexicon entries.

#This is actually really nasty and hardcoding the lexicon like this is tedious. 
#Regardless, the call is lexicon.lexicon[LEMMA][PoS]. This returns a list of concepts associated with the
#      provided lemma and pos.
       
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
    # this is here temporarily, when Alex fixes lemmatization, I'll change it to "go"
    'gone': {
        'VB' :[TravelEvent, ChangeEvent]
    }
    
}
#'where' : [location slot]}


def senses(*args):
    lemma = args[0]
    
    if lemma in lexicon.keys():
        pos = args[1] if len(args) > 1 else None
        
        if pos and pos in lexicon[lemma].keys():
            return lexicon[lemma][pos]
        else: 
            return reduce(lambda s1, s2: s1 + s2,
                          [lexicon[lemma][pos] 
                           for pos in lexicon[lemma].keys()])
