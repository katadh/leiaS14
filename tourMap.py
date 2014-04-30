import Queue

# POI = Point of Interest
class tourPOI:
    def __init__(self, loc_name, descrip, out):
        self.name = loc_name
        self.description = descrip
        # outside is a boolean indicating if the location is indoors
        # or outdoors
        self.outdoors = out

class tourMap:
    def __init__(self, poi):
        # This should be a list of locations
        self.POI = poi

    # start and end should be strings
    # (the names of locations)
    def findPath(self, start, end):
        inf = float("inf")
        loc_list = []
        dist = {start : 0}
        parent = {start : ""}
        for location in self.POI:
            name = location.name
            if name != start:
                dist[name] = inf
                parent[name] = ""
            loc_list.append([dist[name], location])

        while q.empty() != True:
            location = loc_list.pop(loc_list.index(min(loc_list)))
            
            if dist[location] == inf:
                return []
                
            for neighbor in location[1].neighbors:
                test_dist = dist[location[1].name] + neighbor[1]
                if test_dist < dist[neighbor[0].name]:
                    dist[neighbor[0].name] = test_dist
                    prev[neighbor[0].name] = location[1].name
                    for i in range(len(loc_list)):
                        if loc_list[i][1] == neighbor[0].name:
                            loc_list[i][0] = test_dist
        return [dist, parent]
                    
                    
                    
            
            
        
        
