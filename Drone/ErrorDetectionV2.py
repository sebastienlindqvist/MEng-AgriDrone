from datetime import datetime
import math

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
        # p,y,r=vehicle.attitude  #need to remove one with _
        if y >= math.radians(35): # convert these to radians
            Attitude_file=open("Error.txt",'a')
            current_time = now.strftime("%H:%M:%S")
            Attitude_file.write(current_time+"\n")
            Attitude_file.close()
        elif p >= math.radians(35): # convert these to radians
            Attitude_file=open("Error.txt",'a')
            current_time = now.strftime("%H:%M:%S")
            Attitude_file.write(current_time+"\n")
            Attitude_file.close()

    
    def UpdateVelocity(self):
        # vx,vy,vz = vehicle.velocity
        MaxVelocity=5 #5m/s
        if vx >= MaxVelocity or vx <=-MaxVelocity:
            current_time = now.strftime("%H:%M:%S")
        if vy >= MaxVelocity or vy <=-MaxVelocity:
            current_time = now.strftime("%H:%M:%S")
        if vz >= MaxVelocity or vz <=-MaxVelocity:
            current_time = now.strftime("%H:%M:%S")
##------------------------------------------------
##                      Error Checking
##---------------------------------------------------
    def CheckErrors(self):
        Error_file = open("Error.txt", "r")
        list_of_Errors = Error_file.readlines()
        for i in range(100):
            if list_of_Errors[i]>0:
                print("hello")

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
        
