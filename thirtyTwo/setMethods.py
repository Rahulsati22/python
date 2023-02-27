s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# method 1
print(s1.union(s2))

# method 2
print(s1.intersection(s2))

# method 3
s1.update(s2)
print(s1)

# what is the difference between union and update
# union don't change the original set but update change the original set

# method 4
s1.intersection_update(s2)
print(s1)

# what is the difference between intersect and intersection_update
# intersection don't change the original set but intersection_update change the original set

# method 5
name1 = {"rahul", "ayush"}
name2 = {"rahul", "akshay"}
print(name1.difference(name2))
name1.difference_update(name2)
print(name1)


# method 6
print(name1.isdisjoint(name2))
name1 = {"ayush"}
name2 = {"akshay"}
print(name1.isdisjoint(name2))


# method 7
name1 = {1, 2, 3, 4, 5, 6, 7}
name2 = {5, 6, 7}
print(name1.issuperset(name2))


# method 8
print(name2.issubset(name1))


# method 9
# remove and discard are use to remove items from the set but the main difference is that if we try to remove some item that is not present in the set then it will give error while discard will no give error
name2.remove(7)
print(name2)
name2.discard(6)
print(name2)


# method 10
name1 = {"rahul", "ayush", "akshay"};
# removes a random value from the set
print(name1.pop());


# method 11
# to remove all the elements from the set
name1.clear();
print(name1);



# method 12
# to check whether an element is present in set or not