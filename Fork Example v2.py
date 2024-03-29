
import os
 
print("Process id before forking: {}".format(os.getpid()))
 
try:
    pid = os.fork()
except OSError:
    exit("Could not create a child process \n")

if pid == 0:
    print("In the child process that has the PID {} \n".format(os.getpid()))
    exit()
 
print("In the parent process after forking the child {} \n".format(pid))
finished = os.waitpid(0, 0)
print(finished)
