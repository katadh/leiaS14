#This file acts as a work around for our issue of conflicting our base knowledge with use of Facts.py

from ontology_mattkyle import *
import Facts as fr

def load():
	a = Chips()
	b = Chips()
	c = Aisle()
	d = Aisle()
	e = Price()
	g = Price()
	f = Wines()

	c.name = 'three'
	d.name = 'four'
	e.value = "$2.00"
	g.value = "$5.00"

	a.location = Slot(Aisle)
	b.location = Slot(Aisle)
	a.price = Slot(Price)
	b.price = Slot(Price)
	f.location = Slot(Aisle)
	f.price = Slot(Price)

	a.location.fill(c)
	a.price.fill(e)
	b.location.fill(c)
	b.price.fill(e)
	f.location.fill(d)
	f.price.fill(g)

	fr.store(a)
	fr.store(b)
	fr.store(c)
	fr.store(d)
	fr.store(f)