f=open("demofile.txt","r+")
f.write("samm")
import time
for i in range(0,100):
    time.sleep(1)
    f.write("sam")