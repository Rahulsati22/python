import time


def usingWhile():
    i = 0
    while (i < 5000):
        i = i + 1
    pass


def usingFor():
    for i in range(0, 5000):
        i = i + 1


# measuring time take by for loop
startTime = time.time()
usingFor()
endTime = time.time()
print(f"total time taken by for loop is {endTime - startTime}")

# measuring time taken by while loop
startTime = time.time()
usingWhile()
endTime = time.time()
print(f"the total time taken by while loop is {endTime - startTime}")

# while loop is taking more time than for loop
