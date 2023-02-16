f=open("demofile.txt","r+")
import time
f.write("shiv")
for i in range(0,100):
    time.sleep(1)
    f.write("shiv")