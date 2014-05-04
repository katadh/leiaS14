import plan
import planManager
import planList_petrjay as PlanList

class PlanManager(planManager.planManager):
    
    def __init__(self):
        super(PlanManager, self).__init__()
        
        # so that our custom plan list is used
        planManager.PlanList = PlanList
        plan.PlanList = PlanList
        
    def planSelect(self, TMR):
	#return_plan == None is essentially the "do nothing" plan
	return_plan = None
	current_max = 0
	TMR_set = set()
	for instance in TMR:
		TMR_set.add(str(instance).split('-')[0])
	print "TMR set is", TMR_set
	for p in PlanList.plan_lexicon:
	    if len(TMR_set.intersection(p[0])) == len(TMR_set):
		r = PlanList.plan_map[p[1]]
		return_plan = plan.plan(r[0],r[1],r[2],False,p[1])
		return return_plan
	    if len(TMR_set.intersection(p[0])) > current_max:
		current_max = len(TMR_set.intersection(p[0]))
		r = PlanList.plan_map[p[1]]
		return_plan = plan.plan(r[0],r[1],r[2],False,p[1])	    
	if current_max == 0:
	    print "I don't know what to to with that TMR! I'm going to hide in the corner!"
	return return_plan    