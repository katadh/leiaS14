

def repeat(TMR):
	print TMR

def find_food(TMR):
	foods = ["chips", "salsa"]
	found = False
	#Replace with more sophisticated lookup in KB later
	#Will need to examine prereqs and import them from KB
	for f in foods:
		if foods == TMR: #can easily be replaced with more advanced search through a TMR
			print "We have that food"
	if not found:
		print "We don't have that food"
		return

#Prerequisites are represented internally as triples (in a list)
#Can't use tuples because they don't support assignment
#The first element is a string describing the prerequsisites needed
#The second is the name of the prereq for lookup
#The third is a slot for the plan manager to fill with the appropriate lookup if necessary
plan_map_prereqs = {"repeat":[["knowledge", "food", None]],"find_food":[["knowledge", "food", None]]}


#In this map, the tuples have the following format
#The first will be the default priority for this plan
#The second is the time to complete the plan
#The third is the starting progress made (always 0)
#The fourth is the function that will serve as the "executeOneTimestep" function
plan_map = {"repeat":(4,10,0,repeat), "find_food":(3,1,0,find_food)}


plan_lexicon = [(set(['Buy', 'Fish', 'Person']),"repeat")]
