import sys
sys.path.append("../")
from knowledge.Facts import kblookup
import time


def determineLocation(TMR):
	#Determine the theme of the location query
	theme = None
	for concept in TMR:
		s = str(concept).split("-")
		if s[0] != "Aisle" and s[0] != "QuestionEvent":
			theme = s[0]
	#Look for this theme
	if theme == None:
		print "This TMR is confusing, I'm not saying anything."
		return
	kb_return = kblookup(theme)

	print kb_return
	if len(kb_return) == 0:
		print "We do not currently have {0}".format(theme)
	else:
		aisle = kb_return[0].location.filler.name
		#return/print the location associated with this theme
		print "The {0} are in aisle {1}".format(theme, aisle)

def determinePrice(TMR):
	theme = None
	for concept in TMR:
		s = str(concept).split("-")
		if s[0] != "Price" and s[0] != "QuestionEvent":
			theme = s[0]
	if theme == None:
		print "This TMR is confusing, I'm not sayinig anything."
		return
	kb_return = kblookup(theme)
	
	print kb_return
	price = 0

	print "THe {0} cost {1}".format(theme, price)

def stockShelves(TMR):
	print "I'm stocking the shelves..."
	time.sleep(1)
	
		

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
plan_map_prereqs = {"repeat":[["knowledge", "food", None]],
					"find_food":[["knowledge", "food", None]],
					"determineLocation":[],
					"stockShelves":[]}



#In this map, the tuples have the following format
#The first will be the default priority for this plan
#The second is the time to complete the plan
#The third is the starting progress made (always 0)
#The fourth is the function that will serve as the "executeOneTimestep" function
plan_map = {"repeat":(4,10,0,repeat), "find_food":(3,1,0,find_food), 
			"determineLocation":(3,1,0,determineLocation),
			"stockShelves":(4,10,0,stockShelves)}


plan_lexicon = [(set(['Aisle', 'Chips', 'QuestionEvent']),"determineLocation"),(set(['Delivery', 'Animal']),"stockShelves")]
