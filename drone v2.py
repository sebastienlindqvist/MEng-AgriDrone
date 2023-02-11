from dronekit import *
import time
import math

# Connect to the Vehicle.
print("Connecting to vehicle on: /dev/serial0")
vehicle = connect('/dev/serial0',baud=921600, wait_ready=True)

print(" Global Location: %s" % vehicle.location.global_frame)
print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print(" Local Location: %s" % vehicle.location.local_frame)
print(" Attitude: %s" % vehicle.attitude)
print(" Velocity: %s" % vehicle.velocity)
print(" GPS: %s" % vehicle.gps_0)

vehicle.send_ned_velocity(0,0,0,10)
#heading=vehicle.heading
while heading < 3 or heading > 297:
    if heading > 180:
        heading=vehicle.heading
        difference=360-heading
        vehicle.attitude.yaw=difference
    elif heading < 180:
        vehicle.attitude.yaw=-heading

print(" Attitude: %s" % vehicle.attitude)
print(" Heading: %s" % vehicle.heading)
# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
print("Completed")
