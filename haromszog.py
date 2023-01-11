import re
def getString(inText):
    text=input(inText)

    return text
def getInt(inText):
    ok=False
    while not ok:
        numberStr=input(inText)
        if(re.match("^[0-9]*$", numberStr)):
            number=int(numberStr)
            return number
        else:
            print("Hibás adat!")    
def getFloat(inText):
    ok=False
    while not ok:
        numberStr=input(inText)
        if(re.match("^[0-9]*$", numberStr)):
            number=float(numberStr)
            return number
        else:
            print("Hibás adat!")    

   