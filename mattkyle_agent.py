import sys
import select
import time
from leia import leia
from knowledge.lexicon_mattkyle import Lexicon
from knowledge.Facts import *
from plan_selection.planManager_mattkyle import planManager

read_list = [sys.stdin]
timeout = 0.3


if __name__ == "__main__":
	#Primary listening loop
	lexicon = Lexicon()
	pm = planManager()
	global read_list
	dead = False
	while(not dead):
		while read_list:
			ready = select.select(read_list, [], [], timeout)[0]
			if not ready:
				pm.updatePlanQueue(0)
			else:
				for file in ready:
					line = file.readline()
					if not line:
						read_list.remove(file)
					elif line.rstrip():
						if line.lower() == "die agent die!":
							print "Goodbye cruel world!"
							dead = true
							break
						else:
							print "The input was", line
							leia(line, lexicon, pm)
