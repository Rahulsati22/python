import shutil
# methods of shutil
# helps to copy one file to another
shutil.copy("shutil.py", "helper.py")
shutil.copy("./helper.py", "./helper2.py")
shutil.copy("shutiltut.py", "helper.py")
shutil.copy("shutiltut.py", "helper2.py")
# folder should not be already present
# copy one folder to another
shutil.copytree("./folder1", "./folder2")
# move one file from one place to another
shutil.move("./folder1/hello.txt", "./hello.txt")
# used to delete file or folder
shutil.rmtree("./folder1")
