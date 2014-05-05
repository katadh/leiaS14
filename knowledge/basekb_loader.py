#This file acts as a work around for our issue of conflicting our base knowledge with use of Facts.py

from ontology_mattkyle import *
import Facts as fr

def load():
	a = Chips()
	b = Chips()
	c = Aisle()
	c.name = 'three'
	d = Aisle()
	d.name = 'four'
	a.location = Slot(Aisle)
	b.location = Slot(Aisle)
	a.location.fill(c)
	b.location.fill(c)
	fr.store(a)
	fr.store(b)
	fr.store(c)
	fr.store(d)