import sys
from parse import *
from pprint import pprint
from semantics.semantics import *

"The top-level processing pipeline"

def leia(sentence):
    tagged_words = analyzeSentence(sentence)
    #tagged_words = [Word('I', 'I', 'PRP', None),
                    #Word('buy', 'buy', 'bla', None),
                    #Word('fish', 'fish', 'NN', None)]
        
    candidate_tmrs = tmr(tagged_words)  
    
    #pprint(map(lambda tmr:
               #map(str, tmr),
               #candidate_tmrs))
    
    return candidate_tmrs
    

if __name__ == "__main__":
    sentence = sys.argv[1] if len(sys.argv) > 1 else None
    
    if sentence:
        leia(sentence)

### Where are the chips?
### TMR:
### reguest-info:
###   theme: chips
###            location: ?

### Solutions:

### macro:
### Where (be) <concept> ?
### request-info:
###   theme: <concept>
###            location: ?

### proto-concept:
### Where
### <concept>:
###    location: ?

### slot-concept
### location:
###   theme: <concept>
###   aisle: ?