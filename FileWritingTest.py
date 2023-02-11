# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
#print("Connecting to vehicle on: /dev/serial0")
#vehicle = connect('/dev/serial0',baud=921600, wait_ready=True)

#while True:
    #print(" Heading: %s" % vehicle.heading)

#line
#file2write=open("filename.txt",'a')
#file2write.write("here goes the data \n")
#file2write.close()
#open('filename.txt', 'w').close()

a_file = open("filename.txt", "r")
list_of_lines = a_file.readlines()
list_of_lines[3] = "Line2\n"

a_file = open("filename.txt", "w")
a_file.writelines(list_of_lines)
a_file.close()

