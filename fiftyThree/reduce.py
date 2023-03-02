# reduce is a higher order function
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
ans = reduce(lambda x, y: x + y, numbers)
print(ans)
