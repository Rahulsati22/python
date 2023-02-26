# creating the tuple
tup = (1, 2, 3)

# printing the whole tupple and the type if the tupple
print(tup, type(tup))


# tup[0] = 10; --> this is not possible


# printing the tuple elements using name of the tuple and index
print(tup[0])
print(tup[1])
print(tup[2])


# all methods are same as list
if 2 in tup:
    print("Yes 2 is present in tupple")
else:
    print("No 2 is not present in tupple")


if 100 in tup:
    print("Yes 100 is present in tupple")
else:
    print("No 100 is not present in tupple")


'''
# tuple is almost similar to list and the only difference is that
you can change the list but you cannot change the tupple

# elements are separated by , and enclosed by rounded brackets

#tuples are ordered collection of data items

#when we don't want to chnge items of our collection we use tuple
'''
