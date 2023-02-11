###     Collector Class     ###
import RPi.GPIO as GPIO
import time

class Collector:
    def __init__(self, SoPins, SrPins):
        self.SampleNum = 4
        self.CurrentSample = 1
        self.Servo1 = SoPins[0]
        self.Servo2 = SoPins[1]
        self.Servo3 = SoPins[2]
        self.Servo4 = SoPins[3]
        self.Sensor1 = SrPins[0]
        self.Sensor2 = SrPins[1]
        self.Sensor3 = SrPins[2]
        self.Sensor4 = SrPins[3]
        
    def ChangeSample(self):
        self.CurrentSample=+1

    def CheckSample(self):
        if self.CurrentSample==1 and self.Sensor1.input==True:
            self.Servo1
            ChangeSample()
        elif self.CurrentSample==2 and self.Sensor2.input==True:
            self.Servo2
            ChangeSample()
        elif self.CurrentSample==3 and self.Sensor3.input==True:
            self.Servo3
            ChangeSample()
        elif self.CurrentSample==4 and self.Sensor4.input==True:
            self.Servo4
            ChangeSample()
