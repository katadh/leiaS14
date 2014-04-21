from semantics.linking import * 
from pprint import pprint

# TODO: relax to superclass
# TODO: use tense information?

# doesn't do any candidate selection yet
def tmr(lemmas):
    for senses in permutesenses(lemmas, lex):
        print 'Possible linkings for senses {0}:'.format(map(str, senses))
        
        listOfAll = findAllLinking(senses)
        
        pprint(map(lambda linking: map(str, linking), listOfAll))
        print
            
    return listOfAll
            
                        
#tmr('I buy fish'.split()) 
