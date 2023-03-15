# variables in python

# means memory mein 1 ko store krdo aur jha par bhi 1 hai us location ke address ko a mein daldo


a = 1
b = 2
c = 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
d = "Harry"
e = 1.22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
f = None
g = True
complexNum = complex(1, 2)
print(complexNum)

print(a, b, c, d)
print(a + b)

# print(c + d); not possible

print(type(a), type(b), type(c), type(d), type(
    e), type(f), type(complexNum), type(g))
# <class 'int'> <class 'int'> <class 'int'> <class 'str'> <class 'float'>  <class 'NoneType'> <class 'complex'> <class 'bool'>


# list is a collection of different data types and it is mutable(can changed)
list = [1, 2, 3, 4, 5, [1, 23, 4, 5], "rahul", "ayush", ["rahul"]]
print(type(list))
# <class 'list'>
print(list)


#tuple us also a list but it is immutable(cannot changed)
list2 = (1,3,2,(1,23,4,5),"rahul");
print(type(list2));
print(list2);
#<class 'tuple'>


#map->it is collection of key value pairs
dict1 = {"name" : "sakshi",
         "age" : 20,
         "canDrive" : True}
print(type(dict1));
print(dict1);
#<class 'dict'>


#every thing is object in python