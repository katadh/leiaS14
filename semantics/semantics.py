from linking import * 
from pruning import *
from relaxation import *
from pprint import pprint
import knowledge.lexicon

# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

# TODO: doesn't do any candidate selection yet
def tmr(tagged_words, Lexicon = knowledge.lexicon.Lexicon):
    tagged_words = filter(lambda tw: Lexicon.senses(tw.lemma),
                          tagged_words)
    
    print 'Interpreting tokens: {0}'.format(map(lambda tw: tw.lemma, tagged_words))
    
    linking_candidates = []
    
    #while len(linking_candidates) < 1:
            #relax() if len(linking_candidates) == 0 else prune()  
        #relaxation += 1
        
    for concepts in Lexicon.permute_senses(tagged_words):
        print 'Possible linkings for senses:'
        pprint(map(str, concepts))
        
        sense_linkings = findAllLinking(concepts)
        linking_candidates += sense_linkings
        
        pprint(map(lambda linking: 
                   map(str, linking), 
                   sense_linkings))
        
        #linking_candidates = prune_partially_linked(linking_candidates)
            
    return linking_candidates



    
        






