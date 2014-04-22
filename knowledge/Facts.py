import inspect
import ontology

TMRS = []

def kblookup(kbitem):
    hits = []
    for t in TMRS:
        classes = inspect.getmro(t.__class__)
        for c in classes:
            if c.__name__ == kbitem:
                hits.append(t)
                break
    return hits
