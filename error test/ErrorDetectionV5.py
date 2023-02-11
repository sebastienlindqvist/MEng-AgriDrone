from datetime import datetime
import math
import time

from dronekit import *
class ErrorDetector:
    def __init__(self):
        self.cmd=9
        
##------------------------------------------------
##                      Updates
##---------------------------------------------------
    def UpdateAll(self):
        self.UpdateAttitude()
        self.UpdateVelocity()
        self.CheckErrors()
        #print("1")
        

    def UpdateAttitude(self):
        MaxAngle=35 # 35 Degrees
        MaxDuration=5 # 5 seconds
        r=vehicle.attitude.roll
        p=vehicle.attitude.pitch
        if abs(r) >= math.radians(MaxAngle):
            start_time = time.time()
            while abs(r)>=math.radians(MaxAngle):
                r=vehicle.attitude.roll
                print("r")
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Attitude_file=open("Error.txt",'a')
                Attitude_file.write(str(time.time())+"\n")
                Attitude_file.close()
        
        elif abs(p) >= math.radians(MaxAngle):
            start_time = time.time()
            while abs(p)>=math.radians(MaxAngle):
                p=vehicle.attitude.roll
                print("p")
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Attitude_file=open("Error.txt",'a')
                Attitude_file.write(str(time.time())+"\n")
                Attitude_file.close()
    
    def UpdateVelocity(self):
        vx,vy,vz = vehicle.velocity
        MaxVelocity=1 #5m/s  set to 1m/s for test
        MaxDuration=1 #5s    set to 1s for test
        if vx >= MaxVelocity or vx <=-MaxVelocity:
            start_time = time.time()
            while vx >= MaxVelocity or vx <=-MaxVelocity:
                vx,_,_ = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                #current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(str(time.time())+"\n")
                Velocity_file.close()

        elif vy >= MaxVelocity or vy <=-MaxVelocity:
            start_time = time.time()
            while vy >= MaxVelocity or vy <=-MaxVelocity:
                _,vy,_ = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                #current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(str(time.time())+"\n")
                Velocity_file.close()
            
        elif vz >= MaxVelocity or vz <=-MaxVelocity:
            start_time = time.time()
            while vz >= MaxVelocity or vz <=-MaxVelocity:
                _,_,vz = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                #current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(str(time.time())+"\n")
                Velocity_file.close()
##------------------------------------------------
##                      Error Checking
##---------------------------------------------------
    def CheckErrors(self):
        ## Setting Variables
        MinDifference=1 #1 second
        MaxDifference=600 #10 minutes
        Errors=0
        MaxErrors=5
        #Reading File
        Error_file = open("Error.txt", "r")
        list_of_Errors = Error_file.readlines()
        Error_file.close()
        
        #Checking the file        
        for i in range(len(list_of_Errors)-1,0,-1):
            ## if errors occur less often than 1 minute but  more often than 10 minutes from latest
            if float(list_of_Errors[i]) - float(list_of_Errors[i-1]) > MinDifference and float(list_of_Errors[len(list_of_Errors)-1])-float(list_of_Errors[i-1])<MaxDifference:
                Errors=Errors+1
            else:
                Errors=0
                
        #If there are too many Errors
        if Errors >= MaxErrors:
            print("max error reached")
            self.cmd=9 #drone skips and head to landing location
            self.ErrorReset()

    def SendErrors(self,original_cmd):
        if self.cmd ==9:
            return self.cmd
        else:
            return original_cmd
        
            

##------------------------------------------------
##                      Resets
##---------------------------------------------------

    def Reset(self):
        #self.VelReset()
        #self.AttReset()
        self.ErrorReset()

    def ErrorReset(self):
        open("Error.txt", 'w').close()

##------------------------------------------------
##                      Test code   remove this later
##---------------------------------------------------
vehicle = connect('/dev/serial0',baud=921600,wait_ready=True)
test=ErrorDetector()
test.Reset()
while True:
    test.UpdateAll()
