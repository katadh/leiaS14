import sys
import parse
from pprint import pprint
from semantics.semantics import *
import knowledge.lexicon
from plan_selection.planManager import *

firstRun = False

"The top-level processing pipeline"
### Each application should supply its own lexicon class, otherwise the default one will be used.
def leia(sentence, 
         lexicon = knowledge.lexicon.Lexicon(), 
         planner = planManager(), 
         Heuristics = heuristics.Heuristics):
    
  
    global firstRun
    sp = parse.syntaxParser(21227, 21228, not firstRun)
    firstRun = False

    tagged_words = sp.analyzeSentence(sentence) 
    
    #print 'from syntax'
    #print map(lambda tw: [tw.fullword, tw.lemma, tw.pos, tw.ne], tagged_words)
    #tagged_words = [Word('I', 'I', 'PRP', None), Word('fish', 'fish', 'VBZ', None), Word('fish','fish','NN',None)]
    #tagged_words = [parse.Word('gog', 'gog', 'NN', None), parse.Word('location', 'location', 'NN', None)]
    #print 'hard coded'
    #print map(lambda tw: [tw.fullword, tw.lemma, tw.pos, tw.ne], tagged_words)   
    
    linked_instances = tmr(tagged_words, lexicon, Heuristics)
    
    planner.updatePlanQueue(linked_instances)
    

if __name__ == "__main__":
    sentence = sys.argv[1] if len(sys.argv) > 1 else None
    
    if sentence:
        leia(sentence)

### Where are the chips?
### TMR:
### reguest-info:
###   theme: chips
###            location: ?

### Solutions:

### macro:
### Where (be) <concept> ?
### request-info:
###   theme: <concept>
###            location: ?

### proto-concept:
### Where
### <concept>:
###    location: ?

### slot-concept
### location:
###   theme: <concept>
###   aisle: ?