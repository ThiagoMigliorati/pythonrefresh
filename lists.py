doubleMultiply = lambda x : x*2


l = [2,3,4,5,6,7]
double = [doubleMultiply(x) for x in l]

print(double)

doubleMap = list(map(lambda x : x*2, l))

print(doubleMap)