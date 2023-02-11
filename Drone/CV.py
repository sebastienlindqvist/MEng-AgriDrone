import cv2
from PIL import Image
import numpy as np
import argparse
import imutils

class CV:
    def __init__(self):
        #self.Green_range=[]
        self.Photo=0
        self.Photo_copy=0
        self.Photo_copy2=0
        
    def get_Photo(self):
        self.Photo=cv2.imread('/home/pi/Desktop/Drone/1.jpg')
        self.Photo_copy=np.copy(self.Photo)
    def Resize(self):
        #incase image is somehow smaller or larger than what camera provides
        self.Photo_copy=cv2.resize(self.Photo_copy,(1920,1080))

    def Resize2(self):
        #incase image is somehow smaller or larger than what camera provides
        self.Photo_copy=cv2.resize(self.Photo_copy,(960,540))
        
    def Gray(self):
        # COLOR_BGR2GRAY or COLOR_RGB2GRAY
        self.Photo_copy=cv2.cvtColor(self.Photo_copy,cv2.COLOR_BGR2GRAY)
        
    
    def HSV_green(self):
        green_centre=60
        sensitivity=35
        
        #Hue is 180 degrees of colour
        #Saturation is how much white there is
        #Value is how much colour compared to black there is
        ## mask of green (36,25 25) ~ (86, 255, 255)
        #green range is from 60 to 180 degrees - convert to 0 to 255
        
        hsv=cv2.GaussianBlur(self.Photo_copy, (13,13),0)
        hsv=cv2.cvtColor(hsv,cv2.COLOR_BGR2HSV)
        lower_green=np.array([green_centre-sensitivity,180,25])
        upper_green=np.array([green_centre+sensitivity,255,255])
        mask1=cv2.inRange(hsv, lower_green, upper_green)
        self.Photo_copy = cv2.bitwise_and(self.Photo_copy, self.Photo_copy, mask= mask1)

    def canny(self):
        self.Photo_copy=cv2.cvtColor(self.Photo_copy,cv2.COLOR_BGR2GRAY)
        self.Photo_copy=cv2.Canny(self.Photo_copy,10,100)

    def thresh(self):
        self.Photo_copy2=cv2.cvtColor(self.Photo_copy,cv2.COLOR_BGR2GRAY)
        self.Photo_copy2=cv2.threshold(self.Photo_copy2,50,255,cv2.THRESH_BINARY)[1]
        
    def contours(self):
        #self.Photo_copy2=0
        cnts=cv2.findContours(self.Photo_copy2.copy(), cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            if cv2.contourArea(c)>1:
            # compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # draw the contour and center of the shape on the image
                cv2.drawContours(self.Photo, [c], -1, (255, 0, 255), 2)
                cv2.circle(self.Photo, (cX, cY), 7, (255, 0, 255), -1)
	

    
    def Show(self):
        self.Photo=cv2.resize(self.Photo,(960,540))
        self.Photo_copy2=cv2.resize(self.Photo_copy2,(960,540))
        cv2.imshow('viewer',self.Photo)
        #cv2.imshow('viewer2',self.Photo_copy)
        #cv2.imshow('viewer3',self.Photo_copy2)
        cv2.waitKey()

computerV=CV()  
computerV.get_Photo()
computerV.Resize() #with 1920x1080
computerV.HSV_green()
computerV.thresh()
computerV.contours()
#computerV.canny()
computerV.Resize2() #with 960x540
computerV.Show()
