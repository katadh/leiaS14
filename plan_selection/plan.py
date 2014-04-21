import PlanList


class plan:
	def __init__(self, priority = 0, time_to_complete = 0, current_progress = 0, prereq = False, script_name = ""):
		self.priority = priority
		self.time_to_complete = time_to_complete
		self.current_progress = current_progress
		self.script_name = script_name
		self.prerequisites = PlanList.plan_map_prereqs[self.script_name]
		self.prereq = prereq #refers to whether or not the plan is a prerequisite for another
		self.finished = False

	def __lt__(self, other):
		return self.priority < other.priority

	def executeOneTimestep(self, TMR):
		self.current_progress += 1
		if (self.current_progress == self.time_to_complete):
			self.finished = True
		return PlanList.plan_map[self.script_name][3](TMR)
		
	

