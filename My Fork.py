
import os
import time
#print("Process id before forking: {}".format(os.getpid()))
try:
    pid = os.fork()
except OSError:
    exit("Could not create a child process \n")
#print(pid)
#print(os.getpid())
if pid == 0:
    #print("In the child process that has the PID {} \n".format(os.getpid()))
    while True:
        print("this is the child \n")
        time.sleep(3)
    #exit()
        
else:
    while True:
        print("this is the parent \n")
        time.sleep(3)
#print("In the parent process after forking the child {} \n".format(pid))
#finished = os.waitpid(0, 0)
#print(finished)
