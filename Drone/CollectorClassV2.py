###     Collector Class     ###
import RPi.GPIO as GPIO
import time

SoPins=[7,11,13,15] #pins for servos
SrPins=[16,18,22,24] #pins for IR break sensors

class Collector:
    def __init__(self):
        ##
        GPIO.setmode(GPIO.BOARD)
        # servosForCollector pin setup
        GPIO.setup(SoPins[0],GPIO.OUT)
        GPIO.setup(SoPins[1],GPIO.OUT)
        GPIO.setup(SoPins[2],GPIO.OUT)
        GPIO.setup(SoPins[3],GPIO.OUT)
        ## IRsensors Pin setp
        GPIO.setup(SrPins[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SrPins[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SrPins[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(SrPins[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        ## Variables
        self.duty=7
        self.CurrentSample = 1
        self.Servo1 = GPIO.PWM(SoPins[0],50)
        self.Servo2 = GPIO.PWM(SoPins[1],50)
        self.Servo3 = GPIO.PWM(SoPins[2],50)
        self.Servo4 = GPIO.PWM(SoPins[3],50)
        self.Sensor1 = SrPins[0]
        self.Sensor2 = SrPins[1]
        self.Sensor3 = SrPins[2]
        self.Sensor4 = SrPins[3]

    def ServoStart(self):
        self.Servo1.start(0)
        self.Servo2.start(0)
        self.Servo3.start(0)
        self.Servo4.start(0)
        time.sleep(3)
        
    def ChangeSample(self):
        self.CurrentSample=self.CurrentSample+1

    def CheckSample(self):
        if self.CurrentSample==1 and GPIO.input(self.Sensor1)==GPIO.HIGH:
            self.Servo1.ChangeDutyCycle(self.duty)
            time.sleep(0.3)
            self.Servo1.ChangeDutyCycle(0)
            time.sleep(0.7)
            self.Servo1.ChangeDutyCycle(2)
            time.sleep(0.3)
            self.Servo1.ChangeDutyCycle(0)
            self.ChangeSample()
        elif self.CurrentSample==2 and GPIO.input(self.Sensor2)==GPIO.HIGH:
            self.Servo2.ChangeDutyCycle(self.duty)
            time.sleep(0.3)
            self.Servo2.ChangeDutyCycle(0)
            time.sleep(0.7)
            self.Servo2.ChangeDutyCycle(2)
            time.sleep(0.3)
            self.Servo2.ChangeDutyCycle(0)
            self.ChangeSample()
        elif self.CurrentSample==3 and GPIO.input(self.Sensor3)==GPIO.HIGH:
            self.Servo3.ChangeDutyCycle(self.duty)
            time.sleep(0.3)
            self.Servo3.ChangeDutyCycle(0)
            time.sleep(0.7)
            self.Servo3.ChangeDutyCycle(2)
            time.sleep(0.3)
            self.Servo3.ChangeDutyCycle(0)
            self.ChangeSample()
        elif self.CurrentSample==4 and GPIO.input(self.Sensor4)==GPIO.HIGH:
            self.Servo4.ChangeDutyCycle(self.duty)
            time.sleep(0.3)
            self.Servo4.ChangeDutyCycle(0)
            time.sleep(0.7)
            self.Servo4.ChangeDutyCycle(2)
            time.sleep(0.3)
            self.Servo4.ChangeDutyCycle(0)
            self.ChangeSample()

    def Disconnect(self):
        self.Servo1.stop()
        self.Servo2.stop()
        self.Servo3.stop()
        self.Servo4.stop()
        GPIO.cleanup()
        print ("Goodbye")
