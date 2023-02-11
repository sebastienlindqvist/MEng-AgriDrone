##     main program  ##

## Import Libraries
import RPi.GPIO as GPIO
import time
import sys
from dronekit import *

## Importing Classes
import CollectorClassV3
import CameraClass
GPIO.setwarnings(False)

def main():
    ##variables
    finished=False
    height=2
    ## connecting to drone via serial wire
    vehicle = connect('/dev/serial0',baud=921600,wait_ready=True)
    
    
    ## making objects
    collector1=CollectorClassV3.Collector()
    collector1.Clear()

    ## continuous loop
    while finished==False:
        cmd=vehicle.commands.next

##--------------------------------------------------------------
        if cmd==0:
            print('drone taking off')
##--------------------------------------------------------------
        elif cmd==1:
            print('drone flying to first sample')
##--------------------------------------------------------------      
        elif cmd==2:
            print('drone at first sample')
            vehicle.location.global_relative_frame.alt=height

            print('activating collector, camera and computervision')
            collector1.ServoStart()
            ##--------------------------------------------------------------
            ##     write moving above plant here
            ##
            ##  rotate to look north
            heading=vehicle.heading
            while heading < 3 or heading > 297:
                if heading > 180:
                    heading=vehicle.heading
                    difference=360-heading
                    vehicle.attitude.yaw=difference
                elif heading < 180:
                    vehicle.attitude.yaw=-heading

            ##
            ##
            ##
            ## vehicle.goto(long, latt, altt)        
            ##--------------------------------------------------------------
            while collector1.CurrentSample ==1:
                collector1.CheckSample()
                height=height-0.1
                print(height)
                vehicle.location.global_relative_frame.alt=height
                time.wait(1)
            print('deactivating collector, camera and computervision')
            collector1.Disconnect()
            height=2
            vehicle.location.global_relative_frame.alt=height
            vehicle.commands.next=3
            vehicle.commands.upload()
##--------------------------------------------------------------
        elif cmd==3:
            print('drone flying to second sample')
##--------------------------------------------------------------
        elif cmd==4:
            print('drone at second sample')
            vehicle.location.global_relative_frame.alt=height

            print('activating collector, camera and computervision')
            collector1.ServoStart()
            ##--------------------------------------------------------------
            ##     write moving above plant here
            ##
            ##--------------------------------------------------------------
            while collector1.CurrentSample ==2:
                collector1.CheckSample()
                height=height-0.1
                print(height)
                vehicle.location.global_relative_frame.alt=height
                time.wait(1)
            print('deactivating collector, camera and computervision')
            collector1.Disconnect()
            height=2
            vehicle.location.global_relative_frame.alt=height
            vehicle.commands.next=5
            vehicle.commands.upload()
##--------------------------------------------------------------
        elif cmd==5:
            print('drone flying to third sample')

##--------------------------------------------------------------
        elif cmd==6:
            print('drone at third sample')
            vehicle.location.global_relative_frame.alt=height

            print('activating collector, camera and computervision')
            collector1.ServoStart()
            ##--------------------------------------------------------------
            ##     write moving above plant here
            ##
            ##--------------------------------------------------------------
            while collector1.CurrentSample ==3:
                collector1.CheckSample()
                height=height-0.1
                print(height)
                vehicle.location.global_relative_frame.alt=height
                time.wait(1)
            print('deactivating collector, camera and computervision')
            collector1.Disconnect()
            height=2
            vehicle.location.global_relative_frame.alt=height
            vehicle.commands.next=7
            vehicle.commands.upload()
##--------------------------------------------------------------
        elif cmd==7:
            print('drone flying to fourth sample')
##--------------------------------------------------------------
        elif cmd==8:
            print('drone at fourth sample')
            vehicle.location.global_relative_frame.alt=height

            print('activating collector, camera and computervision')
            collector1.ServoStart()
            ##--------------------------------------------------------------
            ##     write moving above plant here
            ##
            ##--------------------------------------------------------------
            while collector1.CurrentSample ==4:
                collector1.CheckSample()
                height=height-0.1
                print(height)
                vehicle.location.global_relative_frame.alt=height
                time.wait(1)
            print('deactivating collector, camera and computervision')
            collector1.Disconnect()
            height=2
            vehicle.location.global_relative_frame.alt=height
            vehicle.commands.next=9
            vehicle.commands.upload()
##--------------------------------------------------------------
        elif cmd==9:
            print('drone flying to landing ')
##--------------------------------------------------------------
        elif cmd==10:
            print('drone landed')
            finished=True
        
    ## Camera
    camera1=CameraClass.Camera()
    camera1.Capture()
    print("test")
    ##collector code
    
    #collector1.ServoStart()
    #while collector1.CurrentSample != 5:
        
        #collector1.CheckSample()
    #collector1.Disconnect()



if __name__ == '__main__':
    main()
