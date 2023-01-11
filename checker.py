def checkTriangle(sideList):
    ok= False
    if(sideList[0]+sideList[1]>sideList[2] and sideList[0]+sideList[2]>sideList[1] and sideList[1]+sideList[2]>sideList[0] and sideList[0]>0):
        return True   
    else:
        print("Nem háromszög!")
        return False    