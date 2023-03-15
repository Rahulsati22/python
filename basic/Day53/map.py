def cube(x):
    return x*x*x


print(cube(2))
li = [1, 2, 3, 4, 5, 6, 7]

print(li)
# boaring way
for index, element in enumerate(li):
    li[index] = cube(element)

print(li)

# shortcut method to do above procedure
ans = list(map(lambda x: x * x * x, li))
print(ans)


# map is a higher order function
