from itertools import chain

### access => generate permu of index to generate element of the access
def permu(sizeSlot,sizeFiller,distList=[],access=[]):
    if distList==[]:
        distList=[sizeFiller]*sizeSlot
    return helper(distList,used=[0]*(sizeFiller+1),access=access)


## Generate permu that allows repeat element
def productRule(distList=[]):
    return helper(distList,repeat=True)


def helper(permuList,repeat=False,size=0,used=[0]*100,current=[],access=[]):
    temp = []
    if size == len(permuList):
        return [current]
    for i in range(permuList[size]):
        if repeat:
            temp = temp + helper(permuList,repeat,size+1,used,current+[i])  
        elif used[i]==0:
            used[i]=1
            if access==[]:
                temp = temp +helper(permuList,repeat,size+1,used,current+[i])
            else:
                temp = temp + helper(permuList,repeat,size+1,used,current+[access[i]],access=access)
            used[i]=0
    return temp


### Generate a list of concept except itself
def getRestList(indexOut,size):
    temp = []
    for n in range(size+1):
        if n!=indexOut:
            temp.append(n)
    return temp


#Input = list of the concept 
#Output = list of all possible instance
def findAllLinking(listConcept):
    listInstance = []
    listPermu = []
    ### generate all the combination of the assignment 
    sizeFiller = len(listConcept)-1
    index = 0 
    for Con in listConcept:
        if type(Con) is tuple:
            Con = Con[0]
        currentList = getRestList(index,sizeFiller)
        sizeSlots = len(Con.class_slots())
        p = permu(sizeSlots,sizeFiller,access=currentList)
        listPermu += [p]
        index = index+1
    sizeList =[]
    for l in listPermu:
        sizeList.append(len(l))
    ### generate all combination of orders of assignment
    OrderList = productRule(sizeList)

    for i in OrderList:
        #Generate new set of Instance
        InstanceList =[]
        for j in listConcept:
            if type(j) == tuple:
                if j[1] == []:
                    temp = j[0]()
                else:
                    temp = j[0](j[1])
            else:
                temp = j()
                
            InstanceList.append(temp)
            
            
        status = True
        for j in range(len(InstanceList)):
            ind = 0
            for slot in InstanceList[j].slots():
                ### Example
                ### [ [[]] , [[0,2]],[2,0]], [[0,1], [1,0]] ]
                ### listPermu[j] -> get the list of permu of j instance
                ### i[j] -> get the number of the possible permu 
                ### ind -> get the slot to be filled
                indexIn = listPermu[j][i[j]][ind] 
                status = status and InstanceList[j].slots()[slot].fill(InstanceList[indexIn])
                ind = ind+1
        if status:
            listInstance.append(InstanceList)
    return listInstance
    
     