import haromszog
import checker
import calculate

def triangle():
   
    
    chooseOk=True
    choose=haromszog.getInt("Kerület[1] Terület N[2] Terület H[3]\n kör terület[4] kerület[5]\nválassz: ")
    while(chooseOk):
        sideList=[]
        if(choose==1):
            while(not checker.checkTriangle(sideList)):
                sideList=setList()
            chooseOk=False
            pher=calculate.calculatePher(sideList)
            print("A háromszög kerülete: {} cm".format(pher))
        elif(choose==3):
            while(not checker.checkTriangle(sideList)):
                sideList=setList()
            chooseOk=False
            pher=calculate.calculateAreaHeron(sideList)
            print("A háromszög területe Héron képlettel: {} cm2".format(pher))
        elif(choose==2):
            chooseOk=False
            sideList.append(haromszog.getFloat("Alap: "))    
            sideList.append(haromszog.getFloat("Magasság: "))
            area=calculate.calculateAreaNormal(sideList)
            print("A területe: {} cm2".format(area))  
        elif(choose==4):
            choose=False
            sideList.append(haromszog.getFloat("Sugár: "))
            kerulet=calculate.calculateCircle(sideList)
            print("A kör kerülete: {}".format(kerulet))
        elif(choose==5):
            choose=False
            sideList.append(haromszog.getFloat("Sugár: "))
            terulet=calculate.calculateCircleNormal(sideList)
            print("A kör területe: {}".format(terulet))
        else: 
            choose=haromszog.getInt("Kerület[1] Terület N[2] Terület H[3]\n kör terület[4] kerület[5]\nválassz: ")

def setList():
    sideList=[]

    for i in range(0,3):
        sideList.append(haromszog.getFloat("{}.oldal: ".format(i+1)))      
    return sideList 


triangle()





