import os

# this method is used to create a directory
if (not os.path.exists('sample directory2')):
    os.mkdir("sample directory2")

# this method is used to delete a directory
os.rmdir("sample directory2")

# create 100 folders using os.mkdir
for i in range(1, 101):
    os.mkdir(f"Day {i}")

# delete 100 folders using os.rmdir
for i in range(1, 101):
    os.rmdir(f"Day {i}")
