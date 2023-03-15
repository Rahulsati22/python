list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, element in enumerate(list):
    print(
        f"The index of the element is {index} and the value of the element is {element}")
    if (index == 3):
        print("Rahul sati is best in the world")

for index, element in enumerate(list, start=1):
    print(
        f"The index of the element is {index} and the value of the element is {element}")
    if (index == 3):
        print("Rahul sati is best in the world")
# enumerate function helps us to find the index of each and every element in the list and to show it
# enumerate function return a tuple containing element of list and its index
