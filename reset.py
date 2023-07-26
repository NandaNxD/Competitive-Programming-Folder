import shutil
fileName=input()

files=['a.cpp','b.cpp','c.cpp','d.cpp','e.cpp','f.cpp','g.cpp','h.cpp']
flag=0
for file in files:
    if(file[0]==fileName.capitalize()[0]):
        shutil.copy('template.txt',file)
        flag=1
        break
if(flag==0):
    for file in files:
        shutil.copy('template.txt',file)