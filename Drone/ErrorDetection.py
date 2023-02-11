



class ErrorDetector:
    def __init__(self):
        line1=0
        line2=0


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

    def GyroReset(self):
        open("Gyro.txt", 'w').close()
        file2write=open("Gyro.txt",'a')
        for i in range(100):
            file2write.write("0 \n")
        file2write.close()

    def AccReset(self):
        open("Gyro.txt", 'w').close()
        file2write=open("Gyro.txt",'a')
        for i in range(100):
            file2write.write("0 \n")
        file2write.close()
        
        #
        #  send messages to pixhawk


        
        # check acceleration
        # store value in file
        # check with previous 10 in file
        # if new value differs by 3 m/s^2
        # add to error detection file and time stamp


        # check gyroscope
        # store value in file
        # check with previous 10 in file
        # if new value differs by 100 degrees
        # add to error detection file and time stamp


        #check error detection file
        # how often are errors occuring
        # are the occuring often
        # if 5 errors are detected close enough
        # land or fly to home
