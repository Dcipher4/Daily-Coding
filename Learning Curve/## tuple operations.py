    ## tuple operations
##tuple.count(element) - #The count() method of Tuple returns the 
#number of times the given element appears in the tuple.

# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)

# ##tuple.index(element, start, end)
# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple.index(3)
# print('First occurrence of 3 is', res)

tuple1 = (0, 0, 2, 3, 5, 7, 7, 8, 90, 90, 21, 23, 34, 4, 1, 2, 3, 4, 5, 6, 7, 12, 2, 2, 2, 2)
res = tuple1.count(2)
print("Count of 2 in tuple1 is: ", res)

tuple2 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res2 = tuple1 + tuple2
print("combined list of tuples: ", res2)
res3 = res2.count(2)
print(res)