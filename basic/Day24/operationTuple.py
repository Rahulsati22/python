'''
we cannot change tuples 
if you want to change tuple then convert it into a list and change it
and then again convert it to tuple again

we can concatenate two tuples directly means not changing them to list
'''
nums = (1, 2, 3, 4, 5)
temp = list(nums)
temp.append(10)
temp.append(20)
temp.pop()
nums = tuple(temp)
print(nums)


temp1 = (1, 2, 3)
temp2 = (4, 5, 6)
temp1 = temp1 + temp2
print(temp1)


temp1 = (1, 2, 1, 1, 1, 1)
print(temp1.count(1))


# this method will write the first index of 1 in the temp
print(temp1.index(1))

print(temp1.index(1,1));

print(len(temp1));