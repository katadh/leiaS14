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

def load(fName = ""):
    if file == "": return
    kbf = open(fName, 'r')
    lines = kbf.readlines()
    kbf.close()
    inst_map = {}
    requests = {}
    for l in lines:
        l = l.strip()
        if l[0] == '#': continue
        l = l.split('\t')
        
        concept_name = l.pop(0)
        index = int(l.pop(0))
        new_inst = globals()[concept_name]()

        while len(l) != 0:
            #pop open parentheses
            l.pop(0)
            slot = l.pop(0)
            if slot[0] == '%':
                var = l.pop(0)
                if slot[1] == 'b':
                    setattr(new_inst, slot[2:], var == 'True')
                elif slot[1] == 'f':
                    setattr(new_inst, slot[2:], float(var))
                elif slot[1] == 's':
                    setattr(new_inst, slot[2:], var)
            else:
                f_index = int(l.pop(0))
                if f_index not in inst_map:
                    if f_index not in requests: requests[f_index] = []
                    requests[f_index].append((index, slot))
                else:
                    setattr(new_inst, slot, inst_map[f_index])
            l.pop(0)
            
        inst_map[index] = new_inst
        if index in requests:
            for i, attr in requests[index]:
                setattr(inst_map[i], attr, inst_map[index])
            del requests[index]

    for k, v in inst_map.items():
        base_store(v)
        
def forget(inst):
    classes = inspect.getmro(inst.__class__)
    for c in classes:
        name = c.__name__
        if name not in local_TMRs: continue
        else:   local_TMRs[name].remove(inst)


def kblookup(kbitem):
    hits = []
    if kbitem in local_TMRs:  hits.extend(local_TMRs[kbitem])
    if kbitem in base_TMRs: hits.extend(base_TMRs[kbitem])
    return hits
