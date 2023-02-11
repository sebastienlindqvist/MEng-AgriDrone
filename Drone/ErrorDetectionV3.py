from datetime import datetime
import math
import time

class ErrorDetector:
    def __init__(self):
        line1=0
##------------------------------------------------
##                      Updates
##---------------------------------------------------

    def UpdateGyro(self):
        #gyro= vehicle.heading
        
        gyro_file = open("Gyro.txt", "r")
        
        list_of_lines = gyro_file.readlines()
        list_of_lines[line1] = gyro
        
        gyro_file = open("Gyro.txt", "w")
        gyro_file.writelines(list_of_lines)
        gyro_file.close()

        ##
        line1=line1+1
        if line1==100:
            line1=0

    def UpdateAttitude(self):
        MaxAngle=35 # 35 Degrees
        MaxDuration=5 # 5 seconds
        # p,y,r=vehicle.attitude  #need to remove one with _
        if y >= math.radians(MaxAngle):
            start_time = time.time()
            while y>=math.radians(MaxAngle):
                # _,y,_=vehicle.attitude  #need to remove one with _
                print("y")
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Attitude_file=open("Error.txt",'a')
                current_time = now.strftime("%H:%M:%S")
                Attitude_file.write(current_time+"\n")
                Attitude_file.close()
        
        elif p >= math.radians(MaxAngle):
            start_time = time.time()
            while p>=math.radians(MaxAngle):
                # p,_,_=vehicle.attitude  #need to remove one with _
                print("p")
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Attitude_file=open("Error.txt",'a')
                current_time = now.strftime("%H:%M:%S")
                Attitude_file.write(current_time+"\n")
                Attitude_file.close()
            Attitude_file=open("Error.txt",'a')
            current_time = now.strftime("%H:%M:%S")
            Attitude_file.write(current_time+"\n")
            Attitude_file.close()

    
    def UpdateVelocity(self):
        # vx,vy,vz = vehicle.velocity
        MaxVelocity=5 #5m/s

        if vx >= MaxVelocity or vx <=-MaxVelocity:
            start_time = time.time()
            while vx >= MaxVelocity or vx <=-MaxVelocity:
                # vx,_,_ = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(current_time+"\n")
                Velocity_file.close()

        elif vy >= MaxVelocity or vy <=-MaxVelocity:
            start_time = time.time()
            while vy >= MaxVelocity or vy <=-MaxVelocity:
                # vx,_,_ = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(current_time+"\n")
                Velocity_file.close()
            
        elif vz >= MaxVelocity or vz <=-MaxVelocity:
            start_time = time.time()
            while vz >= MaxVelocity or vz <=-MaxVelocity:
                # vx,_,_ = vehicle.velocity
                print(vx)
            Duration=time.time()-start_time
            if Duration>= MaxDuration:
                Velocity_file=open("Error.txt",'a')
                current_time = now.strftime("%H:%M:%S")
                Velocity_file.write(current_time+"\n")
                Velocity_file.close()
##------------------------------------------------
##                      Error Checking
##---------------------------------------------------
    def CheckErrors(self, cmd):
        ## Setting Variables
        MinDifference=180 #3 minutes
        MaxDifference=600 #10 minutes
        Errors=0
        MaxErrors=5
        #Reading File
        Error_file = open("Error.txt", "r")
        list_of_Errors = Error_file.readlines()
        Error_file.close()
        
        #Checking the file        
        for i in range(len(list_of_Errors),1,-1):
            ## if errors occur less often than 10 minutes
            #if list_of_Errors[i] - list_of_Errors[i-1] > MaxDifference:
                #Errors=0
                #open("Error.txt", 'w').close()
                
            ## if errors occur more oftern than 3 minutes
            if list_of_Errors[i] - list_of_Errors[i-1] > MinDifference and list_of_Errors[len(list_of_Errors)]-list_of_Errors[i]<MaxDifference:
                Errors=Errors+1
            else:
                Errors=0
                
        #If there are too many Errors
        if Errors >= MaxErrors:
            cmd=9 #drone skips and head to landing location
            return cmd
        return cmd
            

##------------------------------------------------
##                      Resets
##---------------------------------------------------

    def Reset(self):
        self.GyroReset()
        self.VelReset()
        self.AttReset()
    
    def GyroReset(self):
        open("Gyro.txt", 'w').close()
        file2write=open("Gyro.txt",'a')
        for i in range(100):
            file2write.write("0 \n")
        file2write.close()

    def VelReset(self):
        open("Velo.txt", 'w').close()
        file2write=open("Velo.txt",'a')
        for i in range(100):
            file2write.write("0 \n")
        file2write.close()

    def AttReset(self):
        open("Attitude.txt", 'w').close()
        file2write=open("Attitude.txt",'a')
        for i in range(100):
            file2write.write("0 \n")
        file2write.close()
        
