#this is to see wich is faster, self coded multiplication or python multiplication
import time
from datetime import timedelta

#my try in multiplication, it is just a adaptation of tetration
def multiplication(x1, x2):
    selfcount = 1
    result = x1
    while selfcount < x2:
        result = x1+result
#        print(result)
        selfcount += 1
    else:
        return result
        
#i created a def just to change how many times it tests the speed
def howmanytries(tries):
    for i in range(tries):
        print(f"try number {i+1} of {tries}")
        #this, is the testing of my own script above of multiplication
        start1 = time.time()
        result1 = multiplication(2,2)
        print(result1)
        end1 = time.time()
        #this next part was get from here: https://stackoverflow.com/questions/27779677/how-to-format-elapsed-time-from-seconds-to-hours-minutes-seconds-and-milliseco wanser of Cesar L.
        elapsed1 = end1-start1
        print("Elapsed time: " + time.strftime("%H:%M:%S.{}".format(str(elapsed1 % 1)[2:])[:15], time.gmtime(elapsed1)))
        
        #this is an approach where i create a space in memory and then allocate a value there and then get it again to show to someone
        start2 = time.time()
        result2 = 2*2
        print(result2)
        end2 = time.time()
        elapsed2 = end2-start2
        print("Elapsed time: " + time.strftime("%H:%M:%S.{}".format(str(elapsed2 % 1)[2:])[:15], time.gmtime(elapsed2)))
        
        #this one i do it on the fly printing
        start3 = time.time()
        print(2*2)
        end3 = time.time()
        elapsed3 = end3-start3
        print("Elapsed time: " + time.strftime("%H:%M:%S.{}".format(str(elapsed3 % 1)[2:])[:15], time.gmtime(elapsed3)))
        
        #here i allocate a space in the memory before and then the timer starts
        result4 = 0
        start4 = time.time()
        result4 = multiplication(2,2)
        print(result4)
        end4 = time.time()
        #this next part was get from here: https://stackoverflow.com/questions/27779677/how-to-format-elapsed-time-from-seconds-to-hours-minutes-seconds-and-milliseco wanser of Cesar L.
        elapsed4 = end4-start4
        print("Elapsed time: " + time.strftime("%H:%M:%S.{}".format(str(elapsed4 % 1)[2:])[:15], time.gmtime(elapsed4)))
        
#call our test
howmanytries(2)
