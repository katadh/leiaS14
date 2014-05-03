from linking import * 
from heuristics import *
from pprint import pprint
import knowledge.lexicon

# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

# TODO: doesn't do any candidate selection yet
def tmr(tagged_words, lexicon = knowledge.lexicon.Lexicon()):
    tagged_words = filter(lambda tw: lexicon.senses(tw.lemma),
                          tagged_words)
    
    print 'Interpreting tokens: {0}'.format(map(lambda tw: tw.lemma, tagged_words))
    
    linking_candidates = []
    
    while True:
        for concepts in lexicon.permute_senses(tagged_words):
            print 'Possible linkings for senses:'
            pprint(map(str, concepts))
            
            sense_linkings = findAllLinking(concepts)
            linking_candidates += sense_linkings
            
            pprint(map(lambda linking: 
                       map(str, linking), 
                       sense_linkings))
            
        if len(linking_candidates) < 1:
            print 'No linkings could be generated. Relaxing...'
            Heuristics.relaxation += 1
            continue
        break
    
    best_linking = Heuristics.best(linking_candidates)
    print 'Best meaning: {0}'.format(map(str, best_linking))
    
    return best_linking