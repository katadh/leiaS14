import plan
import planManager
import planList_petrjay

class PlanManager(planManager.planManager):
    
    def __init__(self):
        super(PlanManager, self).__init__()
        
        # so that our custom plan list is used
        planManager.PlanList = planList_petrjay
        plan.PlanList = planList_petrjay