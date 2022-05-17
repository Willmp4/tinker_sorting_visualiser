import time

# Importing colors from colors.py
from colours import *

def selectionSort(alist, drawData, timeTick):

    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        

        for location in range(1,fillslot+1):
            
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
            drawData(alist, [RED if x == location or x == fillslot+1 or x == positionOfMax  else BLUE for x in range(len(alist))] )
        
        temp = alist[fillslot]
        
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
        
        time.sleep(timeTick)
        
    
        
    
