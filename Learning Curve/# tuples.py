# tuples 
tup = (1 , 2, 3, 564, 45)
##tup = (1 ,) #tup tuple needs at least a comma after digit
##tup = (1) #int
print(type(tup))
tup
##tup[0] = 90 # can not assign value to this as tuple is fixed
print (type(tup), tup)
# print( tup [0])
# print( tup [1])
# print( tup [2])
# print( tup [4])
print(tup[-1]) 
print(tup[-2]) 
print(tup[-3]) 
print (tup [-4])
print (tup [-5])
print (len(tup))
# print(tup[34])# index out of range
if 564 in tup:
    print( "yes! , here sir" )

tup2 = tup[1:4]
print(tup2)
