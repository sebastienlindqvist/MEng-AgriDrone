###      Camera Class ###
from picamera import PiCamera

class Camera:
    def __init__(self):
        self.destination='/home/pi/Desktop/Final Code/Image Folder/image.jpg'

    def Capture(self):
        self.camera = PiCamera()
        self.camera.capture(self.destination)
