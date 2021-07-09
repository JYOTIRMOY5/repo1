import os
import subprocess
a=os.listdir()
#print("list is ",a)
e=0
for e in range(len(a)):
    if(e<len(a)):
        #print(a[e])
        e=e+1
os.chdir('C:\\Users\\JYOTIRMOY NATH\\Desktop\\GIT\\UAT_NEW\\repo1')
m=os.listdir()
#print(m)
print(subprocess.run(["git", "pull","origin","UAT_NEW"]))
