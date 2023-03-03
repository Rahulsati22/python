# what is the meaning of filter
# ek gandi cheez jati hai aur usse saaf hoke aati hai

# def filterFunction(val):
#     return val >= 4


l = [1, 2, 3, 4, 5, 6, 7]


newl = filter(lambda x : x >= 4, l)
print(list(newl))

# filter is a higher order function
