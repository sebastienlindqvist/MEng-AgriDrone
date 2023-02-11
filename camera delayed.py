from picamera import PiCamera
from time import sleep

camera = PiCamera()
for i in range(20):
    ans=input('please press enter when ready')
    #sleep(10)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
    print('captured')
camera.stop_preview()
