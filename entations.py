#making this a def, since we don't use it so much
#x1 is the number we want to tetrate, and x2 is the maximum times we do it
#selfcount is in 1, since in 0 it would lead to an additional run of the calculus, and it would be (probably) wrong
#there is a print in comments if you want to see what is in between the numbers
def tetration(x1, x2):
    selfcount = 1
    result = x1
    while selfcount <= x2:
        result = x1**result
#        print(result)
        selfcount += 1
    else:
        return result

################################################################
#this function is a pentation, it's actually blocked since,    #
# 2 PENTATE 2 times equalls to 2 TETRATE 16 times, and my      #
# computer only supports up to 4 times but still mantaining it,#
# i cant think of a use to it already, but i think i will      #
# manage do to it sometime                                     #
################################################################
#def pentation(x1, x2):
#    selfcount = 1
#    result = x1
#    while selfcount <= x2:
#        result = pentation(x1, result)
#        print(result)
#        selfcount += 1
#    else:
#        return result


#a while loop to get some inputs from user
#its with ints, but i think it can work with floats too
#only tried with "int floats" like 2.0 or 3.1
while True:
    x1 = int(input("enter a number here: "))
    x2 = int(input("How many times we tetrate it: "))
    print(tetration(x1, x2))
    print("lets, do it again")