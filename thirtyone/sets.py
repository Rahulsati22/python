'''
sets are unordered collection of data-items.They store multiple items in a single variable .Set items are separated by commas and enclosed within curly brackets.Sets are unchangeable, meaning you cannot change items of the set once they are created . Sets do not contains duplicate items.
'''
s = {2,4,2,6}
print(s);
print(type(s));#<class 'set'>


s={};
print(type(s));#<class 'dict'>


s=set();
print(type(s));#<class 'set'>


s = {"carla", "rahul", 1.2, 1.5, 10,"rahul","rahul"};
print(s);

for i in s:
    print(i, end=" ");