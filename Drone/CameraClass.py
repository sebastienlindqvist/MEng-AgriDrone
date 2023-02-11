###      Camera Class ###
from picamera import PiCamera
from time import sleep

class Camera:
    def __init__(self):
        self.destination='/home/pi/Desktop/image.jpg'

    def Capture(self):
        self.camera = PiCamera()
        print("test")
        #self.camera.start_preview()
        print("test")
        #sleep(5)
        #self.camera.stop_preview()
        self.camera.capture(self.destination)
