from dronekit import *
import time

vehicle = connect('/dev/serial0',baud=921600,wait_ready=True)
#vehicle.simple_takeoff(10)
cmd=vehicle.commands.next
if cmd ==0:
    print('the next command is 0')
    vehicle.commands.next=1
    vehicle.commands.upload()
    print('command uploaded')
    time.sleep(2)
cmd=vehicle.commands.next
if cmd ==1:
    print('the next command is 1')
    vehicle.commands.next=2
    vehicle.commands.upload()
    print('command uploaded')
    time.sleep(2)
print(cmd)
vehicle.close()
