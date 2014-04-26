import plan
import PlanList
from heapq import *

class planManager:
	def __init__(self):
		self.plans = []


	def planSelect(self, TMR):
		#return_plan == None is essentially the "do nothing" plan
		return_plan = None
		current_max = 0
		for instance in TMR:
			instance_copy = instance.split(":")
			if PlanList.plan_lexicon[instance_copy[0]] == None:
				continue
			else:
				r = PlanList.plan_map[PlanList.plan_lexicon[instance_copy[0]]]
				return_plan = plan.plan(r[0],r[1],r[2],False,PlanList.plan_lexicon[instance_copy[0]])
		return return_plan

	def updatePlanQueue(self, TMR):
		#Nothing to do in this case
		if TMR == 0 and len(self.plans)==0:
			return
		#Continue with current plan, guaranteed to be one if the previous condition wasn't met
		elif TMR == 0:
			self.plans[0].executeOneTimestep(TMR)
		#New plan, and other plans exist already
		else:
			new_plan = self.planSelect(TMR)
			if new_plan == None:
				return
			heappush(self.plans, new_plan)
			if (len(new_plan.prerequisites) > 0):
				for prereq in new_plan.prerequisites:
					if prereq[0] == "knowledge":
						prereq[2] = self.kblookup(prereq[1])
					if prereq[0] == "plan":
						pt = PlanList.plan_map[prereq[1]]
						prereq_plan = plan(new_plan.priority - 1,pt[1],0,True,prereq[1])
						heappush(self.plans, prereq_plan)
			self.plans[0].executeOneTimestep(TMR)
		if self.plans[0].finished:
			heappop(self.plans)


	def kblookup(self, kbitem):
		return 0
