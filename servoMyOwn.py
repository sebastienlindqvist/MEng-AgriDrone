# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 7 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
servo1 = GPIO.PWM(7,50) # Note 7 is pin, 50 = 50Hz pulse
servo2 = GPIO.PWM(11,50)
servo3 = GPIO.PWM(13,50)
servo4 = GPIO.PWM(15,50)


servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
time.sleep(3)

duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    servo3.ChangeDutyCycle(duty)
    servo4.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    servo3.ChangeDutyCycle(0)
    servo4.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1

# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(7)
servo3.ChangeDutyCycle(7)
servo4.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)
servo4.ChangeDutyCycle(0)
time.sleep(1.5)



#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
servo3.ChangeDutyCycle(2)
servo4.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)
servo3.ChangeDutyCycle(0)
servo4.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
servo2.stop()
servo3.stop()
servo4.stop()
GPIO.cleanup()
print ("Goodbye")
