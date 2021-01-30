import shutil
import os

name = input("Enter the path of folder which s to be copied :")
destination = input("Enter where the copied folder has to be pasted :")
name1 = name+'/'
files = os.listdir(name1)
print(files)

for file in files:
    des = destination +'/'
    source = name1+file
    shutil.copy(source,des)

print("It Worked")