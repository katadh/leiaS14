import planManager as PLANMANAGER


if __name__ == "__main__":
	pm = PLANMANAGER.planManager()
	TMR = ["Instance of Request Info"]
	pm.updatePlanQueue(TMR)
	time = 0	
	while len(pm.plans) > 0:
		pm.updatePlanQueue(0)

