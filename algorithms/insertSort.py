import time
from colours import *

def insertion_sort(array, drawData, timeTick):
    for slot in range(1, len(array)): 
        value = array[slot]
        test_slot = slot - 1
        while test_slot > -1 and array[test_slot] > value:
            array[test_slot + 1] = array[test_slot]
            test_slot = test_slot - 1
            drawData(array, [RED if x == test_slot-1 or x == slot+1 else BLUE for x in range(len(array))] )
        array[test_slot + 1] = value
        time.sleep(timeTick)

    