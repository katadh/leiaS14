import inspect
from ontology import *

local_TMRs = {}
base_TMRs = {}

def base_store(inst):
    classes = inspect.getmro(inst.__class__)
    for c in classes:
        name = c.__name__
        if name == "Concept" or name == "object": continue
        if name not in base_TMRs: base_TMRs[name] = []
        base_TMRs[name].append(inst)

def store(inst, sTerm = False):
    classes = inspect.getmro(inst.__class__)
    for c in classes:
        name = c.__name__
        if name == "Concept" or name == "object": continue
        if name not in local_TMRs: local_TMRs[name] = []
        if(sTerm):  local_TMRs[name].insert(0,inst)
        else:   local_TMRs[name].append(inst)
        
def forget(inst):
    if inspect.isclass(inst):
        if inst.__name__ not in local_TMRs: return False
        inst = local_TMRs[inst.__name__][0]
    classes = inspect.getmro(inst.__class__)
    for c in classes:
        name = c.__name__
        if name not in local_TMRs: continue
        else:   
            try:
                local_TMRs[name].remove(inst)
            except ValueError:
                return False
    return True



def kblookup(kbitem):
    hits = []
    if kbitem in local_TMRs:  hits.extend(local_TMRs[kbitem])
    if kbitem in base_TMRs: hits.extend(base_TMRs[kbitem])
    return hits
