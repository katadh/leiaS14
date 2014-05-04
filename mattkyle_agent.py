import time
import signal
from leia import leia
from knowledge.lexicon_mattkyle import Lexicon
from knowledge.Facts import *
from plan_selection.planManager_mattkyle import planManager

TIMEOUT = 1 

def interrupted(signum, frame):
	return

signal.signal(signal.SIGALRM, interrupted)


def input():
	return_val = None
	try:
		return_val = raw_input()
		return return_val
	except:
		return return_val

if __name__ == "__main__":
	#Primary listening loop
	input_ = None
	lexicon = Lexicon()
	pm = planManager()
	while(1):
		signal.alarm(TIMEOUT)
		input_ = input()
		#Get input but don't wait forever
		if input_.lower() == "die agent die!":
			print "Goodbye cruel world!"
			break
		elif input_ == None:
			pm.updatePlanQueue(0)
		else:
			leia(input_, lexicon, pm)
		
