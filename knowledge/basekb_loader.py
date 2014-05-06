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
	h = Wines()
	i = Aisle()
	j = Aisle()

	c.name = 'three'
	d.name = 'four'
	i.name = 'five'
	j.name = 'six'
	e.value = "$2.00"
	g.value = "$5.00"
	f.preferred_product = True
	b.preferred_product = True

	a.location = Slot(Aisle)
	b.location = Slot(Aisle)
	a.price = Slot(Price)
	b.price = Slot(Price)
	f.location = Slot(Aisle)
	f.price = Slot(Price)
	h.location = Slot(Aisle)
	h.price = Slot(Price)

	a.location.fill(c)
	a.price.fill(e)
	b.location.fill(c)
	b.price.fill(g)
	f.location.fill(d)
	f.price.fill(g)
	f.quality.fill(Good())
	h.location.fill(i)
	h.price.fill(e)
	h.quality.fill(Bad())

	fr.store(a)
	fr.store(b)
	fr.store(c)
	fr.store(d)
	fr.store(f)
	fr.store(h)