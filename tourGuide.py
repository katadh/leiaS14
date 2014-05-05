import parse
import leia
import time
import knowledge.lexicon_alexnut
import plan_selection.planManager_alexnut as plan

def startTourGuide():
    stan_parse = parse.syntaxParser()
    time.sleep(3)

    print "How can I help you?\n"
    while(1):
        text = raw_input("--> ")
        if text == "end":
            return
        leia.leia(text, planner=plan.planManager(), lexicon=knowledge.lexicon_alexnut.Lexicon(), sp=stan_parse)
        
