import sys
sys.path.insert(0, './plan_selection')
import planManager
from semantics.semantics import *
import leia


if __name__ == "__main__":
	pm = planManager.planManager()
	while (1):
		sentence = raw_input("Enter a sentence\n")
		try:
			if int(sentence) == 0:
				tmr = 0
		except:
			tmr = leia.leia(sentence)[0]
		pm.updatePlanQueue(tmr)
		print "I have {} plan(s) in my queue".format(len(pm.plans))
