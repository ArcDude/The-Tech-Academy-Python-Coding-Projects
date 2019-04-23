

import os, time

path1 = "C:\\Users\\Schui\\Desktop\\project\\" # first part of the path

path2 = "Python\\" # second part of the path

path = os.path.join(path1, path2) # concatenating the two parts of the path

for file in os.listdir(path):
    if file.endswith(".txt"):
        print (os.path.join(path, file))
        print("Last modified: %s" % time.ctime(os.path.getmtime(path)))

 
