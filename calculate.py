import math
def calculatePher(sideList):
    pher=sideList[0]+sideList[1]+sideList[2]
    return pher
def calculateAreaNormal(sideList):
    area=sideList[0]*sideList[1]/2
    return area
def calculateAreaHeron(sideList):
    s=(sideList[0]+sideList[1]+sideList[2])/2
    area=math.sqrt(s*(s-sideList[0])*(s-sideList[1])*(s-sideList[2]))
    return area   
def calculateCircle(sideList):
    kerulet=2*sideList[0]*math.pi  
    return kerulet
def calculateCircleNormal(sideList):
    terulet=math.sqrt(sideList[0])*math.pi
    return terulet    
