from knowledge.lexicon import senses
from linking import * 
from pprint import pprint

# TODO: relax to superclass
# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

# TODO: doesn't do any candidate selection yet
def tmr(tagged_words):
    tagged_words = filter(lambda tw: senses(tw.lemma),
                          tagged_words)
    
    linking_candidates = []
    
    for concepts in permute_senses(tagged_words):
        #print 'Possible linkings for senses {0}:'.format(map(str, concepts))
        
        sense_linkings = findAllLinking(concepts)
        linking_candidates += sense_linkings
        
        #pprint(map(lambda linking: map(str, linking), sense_linkings))
        
    return prune_partially_linked(linking_candidates)


def prune_partially_linked(linking_candidates):
    def fully_linked(linking):
        def linked(instance, linking):
            def all_slots(linking):
                return reduce(lambda s1, s2: s1 + s2,
                              map(lambda i: i.slots().values(),
                                  linking))            

            def is_filler(instance, linking):
                return any(map(lambda s: s.filler == instance,
                           all_slots(filter(lambda i: not i == instance,
                                            linking))))
            def is_filled(instance):
                # do we want all slots filled or at least one?
                return any(map(lambda s: s.filler,
                               instance.slots().values()))
            
            return is_filler(instance, linking) or is_filled(instance)
        
        return all(map(lambda i: linked(i, linking), 
                       linking))
    
    return filter(fully_linked, linking_candidates)
    
        


"generates all possible combinations of token-to-sense mapping"
def permute_senses(tagged_words):
    if len(tagged_words) == 0:
        return [[]]
            
    return [[sense] + concepts
            for concepts in permute_senses(tagged_words[1:])
            for sense in senses(tagged_words[0].lemma,
                                tagged_words[0].pos)]



