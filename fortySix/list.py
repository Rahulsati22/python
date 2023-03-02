import os

list = os.listdir("../python")

# it will print all the files present in the python folder
for i in list:
    print(i, end=" ")
    print(os.listdir(i), end=" ")

print(os.getcwd())
os.chdir('fortySix')
print(os.getcwd())
print(os.listdir('../fortySix'))
