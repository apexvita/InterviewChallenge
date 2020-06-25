
##########################################################################################
'''
NAME: APEKSHA NARESH MAGAR
Challenge for Software Developer
Question 2 : Calculate the surface of the building exposed to sunlight?
'''
###########################################################################################

#follwing is the function to calculate slope or angle
def slop(i, s):
    m = (s[1] - i[1]) / (s[0] - i[0])
    return (abs(m))

#following is the function to calculate buildings exposed part
def exposed(inp, s):
    l =len(inp)
    sums = 0
    if l == 1:
        sums = sums + abs(inp[0][0][0] - inp[0][2][0])
        sums = sums + abs(inp[0][0][1] - inp[0][2][1])
        return sums

    elif l == 2:
        if inp[0][0][0] > inp[1][0][0]:
            sums += abs(inp[1][0][1] - inp[1][1][1]) #calculate 1st small building front part exposed to sun
            slope = slop(inp[1][0], s)
            sums += slope * abs(inp[0][0][1] - inp[0][1][1])
        else:
            sums += abs(inp[0][0][1] - inp[0][1][1])
            slope = slop(inp[0][0], s)
            sums += slope * abs(inp[1][0][0] - inp[1][1][1]) #calculate 2nd building front part exposed to sun
        sums += abs(inp[0][0][0] - inp[0][2][0]) #calculate  1st small building top part exposed to sun
        sums += abs(inp[1][0][0] - inp[1][2][0]) #calculate  2nd building top part exposed to sun
        print(sums)
        return sums

inp = [[[4, 0], [4, -5], [7, -5], [7, 0]], [[0.4, -2], [0.4, -5,], [2.5, -5], [2.5, -2]]]
s = [-3.5, 1]
a = exposed(inp, s) #call exposed function and print value of a


