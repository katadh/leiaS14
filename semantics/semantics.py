from linking import * 
from pprint import pprint
import knowledge.lexicon
import heuristics
import knowledge.Facts as fr

# TODO: use tense information?
# TODO: can use dependencies as heuristic of where to start from

def tmr(tagged_words, lexicon = knowledge.lexicon.Lexicon(), Heuristics = heuristics.Heuristics):
    tagged_words = filter(lambda tw: lexicon.senses(tw.lemma),
                          tagged_words)

    
    print 'Interpreting tokens: {0}'.format(map(lambda tw: tw.lemma, tagged_words))
    
    linking_candidates = []
    
    while True:
        for concepts in lexicon.permute_senses(tagged_words):
            
            #if not filter(lambda c: 
                          #c.__class__.__name__ == 'DefineEvent',
                          #concepts):
            ### DON'T WORRY - If you hadn't added them beforehand, they will not show up
            concepts += map(lambda i: i.__class__, fr.kblookup('DefineEvent'))
            concepts += map(lambda i: i.__class__, fr.kblookup('Location'))
                
            
            
            print 'Possible linkings for senses:'
            pprint(map(str, concepts))
            
            sense_linkings = findAllLinking(concepts)
            linking_candidates += sense_linkings
            
            pprint(map(lambda linking: 
                       map(str, linking), 
                       sense_linkings))
            
       
        best_linking = Heuristics.best(linking_candidates) if len(linking_candidates) > 0 else None
            
        if not best_linking or Heuristics.goodness(best_linking) < Heuristics.minimal_goodness and Heuristics.relaxation < Heuristics.max_relaxation:
            Heuristics.relaxation += 1
            print 'No good linkings could be generated. Relaxing... to {0}'.format(Heuristics.relaxation)
            
            if best_linking:
                linking_candidates.remove(best_linking)   
                
            continue
        break
    
    print 'Best meaning:'
    pprint(map(str, best_linking))
    
    return best_linking