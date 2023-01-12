#trying to make my own set of math, but it's being a bit hard
#tryed sometimes making my own "add" function but still nothing popped up
#i'm having problems with the "carryes"
#while i'm working on this, i made a multiply function
def mult(x, y):
    selfcount = 1
    result = x
    while selfcount < y:
        result = x+result
        selfcount += 1
    else:
        return result

#and a power function
def power(x, y):
    selfcount = 1
    result = x
    while selfcount < y:
        result = mult(x, result)
        selfcount += 1
    else:
        return result

      
#this is to see what i made, mult is working fine
#sincerily, it's not as different as the "tetration" and "pentation"
print(power(4, 4))
