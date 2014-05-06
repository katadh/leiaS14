import sys
sys.path.append("../")
from knowledge.Facts import kblookup, store
from knowledge.ontology_mattkyle import *
import inspect
import time


def determineLocation(TMR):
	#Determine the theme of the location query
	theme = None
	quality = "Any"
	for concept in TMR:
		s = str(concept).split("-")
		if s[0] == "Good" or s[0] == "Bad" or s[0] == "Best":
			quality = s[0]
		elif s[0] != "Aisle" and s[0] != "QuestionEvent":
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
		#pref_i represents the best index with bias (in order) preferred_product, quality, and (maybe) price
		pref_i = 0
		pref_found = True
		while not kb_return[pref_i].preferred_product:
			pref_i += 1
			if pref_i == len(kb_return):
				pref_i = 0
				pref_found = False
				break

		if quality != "Any":
			while ((not kb_return[pref_i].preferred_product) == pref_found) or (kb_return[pref_i].quality.filler.__class__.__name__ != quality):
				pref_i += 1
				if pref_i == len(kb_return):
					pref_i = 0
					if not pref_found:
						print "We do not have any {0} {1}".format(quality, theme)
						return
					else:
						pref_found = False
			aisle = kb_return[pref_i].location.filler.name
			print "The {0} {1} are in aisle {2}".format(quality, theme, aisle)
		else:
			aisle = kb_return[pref_i].location.filler.name
			#return/print the location associated with this theme
			print "The {0} are in aisle {1}".format(theme, aisle)

def determinePrice(TMR):
	theme = None
	quality = "Any"
	for concept in TMR:
		s = str(concept).split("-")
		if s[0] == "Good" or s[0] == "Bad" or s[0] == "Best":
			quality = s[0]
		elif s[0] != "Price" and s[0] != "QuestionEvent":
			theme = s[0]
	if theme == None:
		print "This TMR is confusing, I'm not saying anything."
		return
	kb_return = kblookup(theme)
	

	if len(kb_return) == 0:
		print "We do not currently have {0}".format(theme)
	else:
		#pref_i represents the best index with bias (in order) preferred_product, quality, and (maybe) price
		pref_i = 0
		pref_found = True
		while not kb_return[pref_i].preferred_product:
			pref_i += 1
			if pref_i == len(kb_return):
				pref_i = 0
				pref_found = False
				break

		if quality != "Any":
			while ((not kb_return[pref_i].preferred_product) == pref_found) or (kb_return[pref_i].quality.filler.__class__.__name__ != quality):
				pref_i += 1
				if pref_i == len(kb_return):
					pref_i = 0
					if not pref_found:
						print "We do not have any {0} {1}".format(quality, theme)
						return
					else:
						pref_found = False
			price = kb_return[pref_i].price.filler.value
			print "The {0} {1} cost {2}".format(quality, theme, price)
		else:
			price = kb_return[pref_i].price.filler.value
			print "The {0} cost {1}".format(theme, price)
	
	"""
	print kb_return
	price = 0

	print "THe {0} cost {1}".format(theme, price)
	"""

def stockShelves(TMR):
	if TMR == 0: return
	print "I'm stocking the shelves..."
	time.sleep(1)

	theme = None
	for concept in TMR:
		s = concept.__class__.__name__
		if s[0] != "Animal" and s[0] != "Delivery" and s[0] != "Quality":
			theme = concept
	if theme == None:
		print "This TMR is confusing, I'm not saying anything."
		return

	concept.location = Slot(Aisle)
	concept.price = Slot(Price)
	concept.preferred_product = True
	cost = Price()
	name = theme.__class__.__name__
	aisles = kblookup("Aisle")
	target_aisle = "six"

	if name == "Chips":
		cost.value = "$2.00"
		target_aisle = 'three'
	elif name == "Wines":
		if concept.quality.filler.__class__.__name__ == "Good":
			cost.value = "$5.00"
			target_aisle = 'four'
		elif concept.quality.filler.__class__.__name__ == "Bad":
			cost.value = "$2.00"
			target_aisle = 'five'
		elif concept.quality.filler.__class__.__name__ == "Best":
			cost.value = "$10.00"
			target_aisle = 'four'
		else:
			cost.value = "$3.00"
			target_aisle = 'six'
	else:
		cost.value = "$3.00"
		target_aisle = 'six'

	concept.price.fill(cost)
	for a in aisles:
		if a.name == target_aisle:
			concept.location.fill(a)
			break

	store(concept)
	print "The delivery of", name, "is put away in aisle", target_aisle


def checkout(TMR):
	items = raw_input("What items are you purchasing?")
	item_list = items.split()
	total = 0.0
	for item in item_list:
		if item == "and":
			continue
		else:
			kb_return = kblookup(item)
			if len(kb_return) == 0:
				continue
			total += float(kb_return[0].price.filler.value.strip("$"))
	raw_input("That will be {0}".format(total))
	print "Have a nice day!"

def repeat(TMR):
	print TMR

#Prerequisites are represented internally as triples (in a list)
#Can't use tuples because they don't support assignment
#The first element is a string describing the prerequsisites needed
#The second is the name of the prereq for lookup
#The third is a slot for the plan manager to fill with the appropriate lookup if necessary
plan_map_prereqs = {"repeat":[["knowledge", "food", None]],
					"determineLocation":[],
					"stockShelves":[],
					"determinePrice":[],
					"checkout":[]}



#In this map, the tuples have the following format
#The first will be the default priority for this plan
#The second is the time to complete the plan
#The third is the starting progress made (always 0)
#The fourth is the function that will serve as the "executeOneTimestep" function
plan_map = {"repeat":(4,10,0,repeat),
			"determineLocation":(3,1,0,determineLocation),
			"stockShelves":(4,10,0,stockShelves),
			"determinePrice":(3,1,0,determinePrice),
			"checkout":(2,1,0,checkout)}


plan_lexicon = [(set(['Aisle', 'QuestionEvent']),"determineLocation"),
				(set(['Delivery', 'Animal']),"stockShelves"),
				(set(['Price','QuestionEvent']),"determinePrice"),
				(set(['Checkout','Animal']),"checkout")]
