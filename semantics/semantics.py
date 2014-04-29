from knowledge.lexicon import senses
from linking import * 
from pprint import pprint

# TODO: relax to superclass
# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

# TODO: doesn't do any candidate selection yet
def tmr(tagged_words):
    print 'before' + str(tagged_words)
    tagged_words = filter(lambda tw: senses(tw.lemma),
                          tagged_words)
    print 'after' + str(tagged_words)
    
    for concepts in permute_senses(tagged_words):
        #print 'Possible linkings for senses {0}:'.format(map(str, concepts))
        
        listOfAll = findAllLinking(concepts)
        
        #pprint(map(lambda linking: map(str, linking), listOfAll))
        #print
            
    return listOfAll


"generates all possible combinations of token-to-sense mapping"
def permute_senses(tagged_words):
    if len(tagged_words) == 0:
        return [[]]
            
    return [[sense] + concepts
            for concepts in permute_senses(tagged_words[1:])
            for sense in senses(tagged_words[0].lemma, 
                                tagged_words[0].pos)]



