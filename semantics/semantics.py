from linking import * 
from pprint import pprint
import knowledge.lexicon
import heuristics
import knowledge.Facts as fr
from concept import Concept


# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

"Basically pulls a primed instance from FR and all its filler instances recursively"
"Shouldn't do anything if you are not priming the FR with a 'DefineEvent'"
def recover_context(instance = None):
    if instance:
        return [instance.__class__] + sum([recover_context(filler) 
                                           for filler in filter(lambda f: f,
                                                                map(lambda s: s.filler,
                                                                    instance.slots().values()))], 
                                          [])
    else:
        matches = fr.kblookup('DefineEvent')
        if matches:
            define = matches[0]
            return filter(lambda c: 
                          c != define.base.filler.__class__, 
                          recover_context(define)) + [Concept] 
    return []
        
    

def tmr(tagged_words, lexicon = knowledge.lexicon.Lexicon(), Heuristics = heuristics.Heuristics):
    Heuristics.relaxation = 3
    tagged_words = filter(lambda tw: lexicon.senses(tw.lemma),
                          tagged_words)

    
    print 'Interpreting tokens: {0}'.format(map(lambda tw: tw.lemma, tagged_words))
    
    linking_candidates = []
    # Planner handles 0-TMR better than None
    best_linking = None
    
    while Heuristics.relaxation <= Heuristics.max_relaxation:
        for concepts in lexicon.permute_senses(tagged_words):
            print 'Possible linkings for senses:'
            
            ### DON'T WORRY - If you hadn't added them beforehand, they will not show up
            concepts += recover_context()
            
            pprint(map(lambda c: 
                       '{0} {1}'.format(c, 
                                        map(lambda (k, v): 
                                            '{0} : {1}'.format(k,v.filler_class.__name__), 
                                            c.class_slots().items())), 
                       concepts))     
            
            sense_linkings = findAllLinking(concepts)
            linking_candidates += sense_linkings
            
            pprint(map(lambda linking: 
                       map(str, linking), 
                       sense_linkings))
            
        best_linking = Heuristics.best(linking_candidates) if len(linking_candidates) > 0 else None
        
        if not best_linking or Heuristics.goodness(best_linking) < Heuristics.minimal_goodness:
            Heuristics.relaxation += 1
            print 'No good linkings could be generated. Relaxing... to {0}'.format(Heuristics.relaxation)
            print "\n----****----\n" 
            
            if best_linking:
                linking_candidates.remove(best_linking)   
                
            continue
        break
    
    if best_linking:
        print 'Best meaning:'
        pprint(map(str, best_linking))
    
    return best_linking