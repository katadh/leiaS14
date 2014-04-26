import sys
from parse import *
from semantics.semantics import *

"The top-level processing pipeline"

def leia(sentence):
    #tagged_words = analyzeSentence(sentence)
    tagged_words = [Word('I', 'I', 'PRP', None),
                    Word('buy', 'buy', 'VB', None),
                    Word('fish', 'fish', 'NN', None)]
        
    linked_instances = tmr(tagged_words)  
    
    return linked_instances
    

if __name__ == "__main__":
    sentence = sys.argv[1] if len(sys.argv) > 1 else None
    
    if sentence:
        print leia(sentence)