# is compare location of objects
# == compare value of objects

a = 10
b = a
print(a is b)  # ans->True
print(a == b)  # ans->True

a = 10
b = 20
print(a is b)  # ans->False
print(a == b)  # ans->False

# a and b is pointing to same memory location
a = 10
b = 10
print(a is b)  # ans->True
print(a == b)  # ans->True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # ans->False
print(a == b)  # ans->True


# jo cheez change nhi ho skti python usko share krta hai like tuple[(1,2,3)] and constants[1,2,3]
# jo cheez change ho skti hai python usko share nhi krta like list[[1,2,3]]
