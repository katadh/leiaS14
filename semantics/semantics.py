from linking import * 
from pprint import pprint
import knowledge.lexicon
import heuristics

# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from
def tmr(tagged_words, lexicon = knowledge.lexicon.Lexicon(), Heuristics = heuristics.Heuristics):
    Heuristics.relaxation = 3
    tagged_words = filter(lambda tw: lexicon.senses(tw.lemma),
                          tagged_words)

    
    print 'Interpreting tokens: {0}'.format(map(lambda tw: tw.lemma, tagged_words))
    
    linking_candidates = []
    # Planner handles 0-TMR better than None
    best_linking = None
    
    while Heuristics.relaxation <= Heuristics.max_relaxation:
        for concepts in lexicon.sense_assignments(tagged_words):
            print 'Possible linkings for senses:'
            
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