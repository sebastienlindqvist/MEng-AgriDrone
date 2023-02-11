# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print("Connecting to vehicle on: /dev/serial0")
vehicle = connect('/dev/serial0',baud=921600, wait_ready=True)
try:
    while True:
        #print(" Velocity: %s" % vehicle.velocity)
        print(" Attitude: %s" % vehicle.attitude)
        
except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
vehicle.close()
