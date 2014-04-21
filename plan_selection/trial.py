import planManager as PLANMANAGER


if __name__ == "__main__":
	pm = PLANMANAGER.planManager()
	pm.updatePlanQueue("repeat")
	time = 0
	while len(pm.plans) > 0:
		if time == 4:
			pm.updatePlanQueue("find_food")
		else:
			pm.updatePlanQueue(0)
		time += 1
		

