list = [5, 4, 3, 2, 1]


# method 1 -> append();
list.append(6)
print(list)


# method 2 -> sort();
list.sort()
print(list)


# method 3 -> sort in descending order
list.sort(reverse=True)
print(list)


# method 4 -> reverse method
list.reverse()
print(list)


# method 5 -> index(num)
print(list.index(1))


# method 6 -> count()
print(list.count(1))


# method 7 -> copy()
list2 = list.copy()
print(list2)


# method 8->insert();
list.insert(1, "hello")
print(list)


# method 9 -> extend();
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# method 10 ->  addition
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
