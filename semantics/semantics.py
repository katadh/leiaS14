from knowledge.lexicon import senses
from linking import * 
from pruning import *
from relaxation import *
from pprint import pprint

# TODO: relax to superclass
# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

# TODO: doesn't do any candidate selection yet
def tmr(tagged_words):
    tagged_words = filter(lambda tw: senses(tw.lemma),
                          tagged_words)
    
    linking_candidates = []
    
    while len(linking_candidates) < 1:
            #relax() if len(linking_candidates) == 0 else prune()  
        #relaxation += 1
        
        for concepts in permute_senses(tagged_words):
            #print 'Possible linkings for senses {0}:'.format(map(str, concepts))
            
            sense_linkings = findAllLinking(concepts)
            linking_candidates += sense_linkings
            
            #pprint(map(lambda linking: 
                       #map(str, linking), 
                       #sense_linkings))
            
            linking_candidates = prune_partially_linked(linking_candidates)
            
    return linking_candidates



    
        






