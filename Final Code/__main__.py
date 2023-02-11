##     main program  ##

## Import Libraries
import RPi.GPIO as GPIO
import time
import sys
import os
from dronekit import *

## Importing Classes
import CollectorClassV3
import CameraClass
import ErrorDetectionFinal
import FinalCV

#Removing warnings
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
    camera1=CameraClass.Camera()
    ComputerV=FinalCV.CV()
    ErrorFinder=ErrorDetectionFinal
    ErrorFinder.Reset()

    ## continuous loop
    while finished==False:
        cmd=vehicle.commands.next
##--------------------------------------------------------------
        if cmd==0:
            print('lift off')
##--------------------------------------------------------------
        elif cmd==1:
            print('drone flying to first sample')
##--------------------------------------------------------------
        elif cmd==2: #drone at first sample
            height=vehicle.location.global_relative_frame.alt
            #activating collector, camera and computervision
            collector1.ServoStart()
            try:
                pid = os.fork()
            except OSError:
                exit("Could not create a child process \n")

            if pid == 0:
                while collector1.CurrentSample ==1:
                    print("this is the child \n")
                    ErrorFinder.UpdateAll()
                exit()
            else:
                while collector1.CurrentSample ==1:
                    camera1.Capture()
                    x,y=ComputerV.Centre()
                    Movement(x,y)
                    
                
            #deactivating collector, camera and computervision
            collector1.Disconnect()
            height=2 #2 metres
            vehicle.location.global_relative_frame.alt=height
            vehicle.commands.next=3
            vehicle.commands.upload()
##--------------------------------------------------------------
        elif cmd==3:
            print('drone flying to second sample')
##--------------------------------------------------------------
        elif cmd==4: #drone at second sample
            vehicle.location.global_relative_frame.alt=height
            #activating collector, camera and computervision
            collector1.ServoStart()
            try:
                pid = os.fork()
            except OSError:
                exit("Could not create a child process \n")

            if pid == 0:
                while collector1.CurrentSample ==2:
                    print("this is the child \n")
                    ErrorFinder.UpdateAll()
                exit()
            else:
                while collector1.CurrentSample ==2:
                    camera1.Capture()
                    x,y=ComputerV.Centre()
                    Movement(x,y)

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
            try:
                pid = os.fork()
            except OSError:
                exit("Could not create a child process \n")

            if pid == 0:
                while collector1.CurrentSample ==2:
                    print("this is the child \n")
                    ErrorFinder.UpdateAll()
                exit()
            else:
                while collector1.CurrentSample ==2:
                    camera1.Capture()
                    x,y=ComputerV.Centre()
                    Movement(x,y)
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
            try:
                pid = os.fork()
            except OSError:
                exit("Could not create a child process \n")

            if pid == 0:
                while collector1.CurrentSample ==2:
                    print("this is the child \n")
                    ErrorFinder.UpdateAll()
                exit()
            else:
                while collector1.CurrentSample ==2:
                    camera1.Capture()
                    x,y=ComputerV.Centre()
                    Movement(x,y)
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
        
##--------------------------------------------------------------------
##            Movement 1   for first collector module
##--------------------------------------------------------------------

def Movement1(plantWidth, plantHeight):
    ##----------------------
    ##get plant centre
    ##get image width and height
    Original_width=1920
    Original_height=1080
    ##----------------------
    center_X = (Original_width/2)
    center_Y = (Original_height/2) - 3*(1786.571/height) #3 is 3cm from centre (change if necessary)
    ##
    while abs(differece_X) >= 5: # 5 pixels (change if necessary)
        difference_X=plantWidth-center_X 
        realWidth=1786.571/difference_X #distance  cm=cm*pixels/pixels
        #velocity=0.05 # 5cm/s
        duration=(abs(differece_X)/100)/0.05# time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_X_difference>=0:#right
            vehicle.send_ned_velocit(0,0.05,0,duration)
        elif Pixel_X_difference<=0:#left
            vehicle.send_ned_velocit(0,-0.05,0,duration)
    ##
    while abs(differece_Y) >= 5: # 5 pixels (change if necessary)
        difference_Y=plantHeight-center_Y
        realHeight=1786.571/difference_Y #distance  cm=cm*pixels/pixels
        velocity=0.05 # 5cm/s
        duration2=(abs(differece_Y)/100)/0.05 # time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_Y_difference>=0: #backward
            vehicle.send_ned_velocit(-0.05,0,0,duration2)
        elif Pixel_Y_difference<=0: #forward
            vehicle.send_ned_velocit(0.05,0,0,duration2)
    ##
    while abs(differece_X) <= 5 and abs(differece_Y) <= 5 and collector1.CurrentSample ==1:
        collector1.CheckSample()
        height=height-0.01
        print(height)
        vehicle.location.global_relative_frame.alt=height
        time.wait(1)

##--------------------------------------------------------------------
##            Movement 2 for second collector module
##--------------------------------------------------------------------

def Movement2(plantWidth, plantHeight):
    ##----------------------
    ##get plant centre
    ##get image width and height
    Original_width=1920
    Original_height=1080
    ##----------------------
    center_X = (Original_width/2) + 3*(1786.571/height) #3 is 3cm from centre (change if necessary)
    center_Y = (Original_height/2) 
    ##
    while abs(differece_X) >= 5: # 5 pixels (change if necessary)
        difference_X=plantWidth-center_X 
        realWidth=1786.571/difference_X #distance  cm=cm*pixels/pixels
        #velocity=0.05 # 5cm/s
        duration=(abs(differece_X)/100)/0.05# time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_X_difference>=0:#right
            vehicle.send_ned_velocit(0,0.05,0,duration)
        elif Pixel_X_difference<=0:#left
            vehicle.send_ned_velocit(0,-0.05,0,duration)
    ##
    while abs(differece_Y) >= 5: # 5 pixels (change if necessary)
        difference_Y=plantHeight-center_Y
        realHeight=1786.571/difference_Y #distance  cm=cm*pixels/pixels
        velocity=0.05 # 5cm/s
        duration2=(abs(differece_Y)/100)/0.05 # time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_Y_difference>=0: #backward
            vehicle.send_ned_velocit(-0.05,0,0,duration2)
        elif Pixel_Y_difference<=0: #forward
            vehicle.send_ned_velocit(0.05,0,0,duration2)
    ##
    while abs(differece_X) <= 5 and abs(differece_Y) <= 5 and collector1.CurrentSample ==2:
        collector1.CheckSample()
        height=height-0.01
        print(height)
        vehicle.location.global_relative_frame.alt=height
        time.wait(1)
##--------------------------------------------------------------------
##            Movement 3 for third collector module
##--------------------------------------------------------------------

def Movement3(plantWidth, plantHeight):
    ##----------------------
    ##get plant centre
    ##get image width and height
    Original_width=1920
    Original_height=1080
    ##----------------------
    center_X = (Original_width/2)
    center_Y = (Original_height/2)  + 3*(1786.571/height) #3 is 3cm from centre (change if necessary)
    ##
    while abs(differece_X) >= 5: # 5 pixels (change if necessary)
        difference_X=plantWidth-center_X 
        realWidth=1786.571/difference_X #distance  cm=cm*pixels/pixels
        #velocity=0.05 # 5cm/s
        duration=(abs(differece_X)/100)/0.05# time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_X_difference>=0:#right
            vehicle.send_ned_velocit(0,0.05,0,duration)
        elif Pixel_X_difference<=0:#left
            vehicle.send_ned_velocit(0,-0.05,0,duration)
    ##
    while abs(differece_Y) >= 5: # 5 pixels (change if necessary)
        difference_Y=plantHeight-center_Y
        realHeight=1786.571/difference_Y #distance  cm=cm*pixels/pixels
        velocity=0.05 # 5cm/s
        duration2=(abs(differece_Y)/100)/0.05 # time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_Y_difference>=0: #backward
            vehicle.send_ned_velocit(-0.05,0,0,duration2)
        elif Pixel_Y_difference<=0: #forward
            vehicle.send_ned_velocit(0.05,0,0,duration2)
    ##
    while abs(differece_X) <= 5 and abs(differece_Y) <= 5 and collector1.CurrentSample ==3:
        collector1.CheckSample()
        height=height-0.01
        print(height)
        vehicle.location.global_relative_frame.alt=height
        time.wait(1)
##--------------------------------------------------------------------
##            Movement 4 for fourth collector module
##--------------------------------------------------------------------

def Movement4(plantWidth, plantHeight):
    ##----------------------
    ##get plant centre
    ##get image width and height
    Original_width=1920
    Original_height=1080
    ##----------------------
    center_X = (Original_width/2)-3*(1786.571/height) #3 is 3cm from centre (change if necessary)
    center_Y = (Original_height/2)
    ##
    while abs(differece_X) >= 5: # 5 pixels (change if necessary)
        difference_X=plantWidth-center_X 
        realWidth=1786.571/difference_X #distance  cm=cm*pixels/pixels
        #velocity=0.05 # 5cm/s
        duration=(abs(differece_X)/100)/0.05# time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_X_difference>=0:#right
            vehicle.send_ned_velocit(0,0.05,0,duration)
        elif Pixel_X_difference<=0:#left
            vehicle.send_ned_velocit(0,-0.05,0,duration)
    ##
    while abs(differece_Y) >= 5: # 5 pixels (change if necessary)
        difference_Y=plantHeight-center_Y
        realHeight=1786.571/difference_Y #distance  cm=cm*pixels/pixels
        velocity=0.05 # 5cm/s
        duration2=(abs(differece_Y)/100)/0.05 # time (s)= distance (cm/100)/velocity (m/s)
        if Pixel_Y_difference>=0: #backward
            vehicle.send_ned_velocit(-0.05,0,0,duration2)
        elif Pixel_Y_difference<=0: #forward
            vehicle.send_ned_velocit(0.05,0,0,duration2)
    ##
    while abs(differece_X) <= 5 and abs(differece_Y) <= 5 and collector1.CurrentSample ==4:
        collector1.CheckSample()
        height=height-0.01
        print(height)
        vehicle.location.global_relative_frame.alt=height
        time.wait(1)

if __name__ == '__main__':
    main()
