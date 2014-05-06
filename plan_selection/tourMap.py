import Queue
import json

# POI = Point of Interest
class POI:
    def __init__(self, loc_name, loc_type, descrip, out, neighbrs):
        self.name = loc_name
        self.location_type = loc_type
        self.description = descrip
        # outside is a boolean indicating if the location is indoors
        # or outdoors
        self.outdoors = out
        self.neighbors = neighbrs

class Map:

    def __init__(self, graphfile):
        self.POI = {}
        jsondata = open(graphfile)
        graphdata = json.load(jsondata)

        for node in graphdata:
           name = node["name"]
           loc_type = node["type"]
           descrip = node["description"]
           out = node["outdoors"]
           neighbors = node["neighbors"]
           self.POI[name] = POI(name, loc_type, descrip, out, neighbors)


    def giveDirections(self, paths, end):
        path = [end]
        while paths[path[-1]] != '':
            path.append(paths[path[-1]])

        path.reverse()
        condensed_path = []

        prev_direction = ""
        for i in range(len(path) - 1):
            direction = [d[2] for d in self.POI[path[i]].neighbors if d[0] == path[i + 1]][0]
            if direction != prev_direction:
                condensed_path.append(direction)
                condensed_path.append(path[i + 1])
            else:
                condensed_path[-1] = path[i + 1]
            prev_direction = direction

        directions = ""
        for direction, location in zip( condensed_path[::2], condensed_path[1::2]):
            directions = directions + "go " + direction + " to the " + location + " then "
            
        directions = directions[:-6]

        return directions
            
        
    # start should be a string
    def findPaths(self, start):
        inf = float("inf")
        loc_list = []
        dist = {start : 0}
        parent = {start : ""}
        for name, location in self.POI.items():
            if name != start:
                dist[name] = inf
            loc_list.append([dist[name], location])

        while len(loc_list) > 0:
            location = loc_list.pop(loc_list.index(min(loc_list)))
            
            if dist[location[1].name] == inf:
                return {}
                
            for neighbor in location[1].neighbors:
                test_dist = dist[location[1].name] + neighbor[1]
                if test_dist < dist[neighbor[0]]:
                    dist[neighbor[0]] = test_dist
                    parent[neighbor[0]] = location[1].name
                    for i in range(len(loc_list)):
                        if loc_list[i][1].name == neighbor[0]:
                            loc_list[i][0] = test_dist
        return [parent, dist]
                    
                    
                    
            
            
        
        
