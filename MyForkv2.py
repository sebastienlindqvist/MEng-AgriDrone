import os
import time
# Import DroneKit-Python
from dronekit import connect, VehicleMode

print("Connecting to vehicle on: /dev/serial0")
vehicle = connect('/dev/serial0',baud=921600, wait_ready=True)

try:
    pid = os.fork()
except OSError:
    exit("Could not create a child process \n")

if pid == 0:
    while True:
        print("this is the child \n")
        print(" Attitude: %s" % vehicle.attitude)
        time.sleep(3)
    
        
else:
    while True:
        print("this is the parent \n")
        print(" Velocity: %s" % vehicle.velocity)
        time.sleep(3)
