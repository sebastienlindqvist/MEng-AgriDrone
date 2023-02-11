from dronekit import *
import time
#vehicle = connect('/dev/serial0',baud=921600,wait_ready=True)

#while True:
    #a=vehicle.attitude.pitch
    #vx,_,_= vehicle.velocity
    #time.sleep(3)
    #print(a)
    #print(vx)
    #print(float(str(time.time())))


MinDifference=60 #1 minute
MaxDifference=600 #10 minutes
Errors=0

Error_file = open("Error.txt", "r")
list_of_Errors = Error_file.readlines()
Error_file.close()
#print(len(list_of_Errors)  )      
for i in range (len(list_of_Errors)-1,0,-1):
    #print(i+1)
    #print(i)
    if float(list_of_Errors[i]) - float(list_of_Errors[i-1]) > MinDifference and float(list_of_Errors[len(list_of_Errors)-1])-float(list_of_Errors[i-1])<MaxDifference:
        Errors=Errors+1
    #print(list_of_Errors[len(list_of_Errors)-1])
    #print(list_of_Errors[i-1])
    #if float(list_of_Errors[len(list_of_Errors)-1])-float(list_of_Errors[i-1])<MaxDifference:
        #Errors=Errors+1
    #else:
        #Errors=0
print(Errors)
