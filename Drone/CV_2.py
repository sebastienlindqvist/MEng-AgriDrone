import cv2
from PIL import Image
import matplotlib.pyplot as plt
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
        IMGcontours, hierarchy = cv2.findContours(self.Photo_copy2,
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#on raspberry pi it needs _,   ,_
        cv2.drawContours(self.Photo_copy, IMGcontours, -1, (0, 255, 0), 3)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (50, 50) 
        # Approximate contours to polygons + get bounding rects and circles
        contours_poly = [None]*len(IMGcontours)
        boundRect = [None]*len(IMGcontours)
        centers = [None]*len(IMGcontours)
        radius = [None]*len(IMGcontours)
        for i, c in enumerate(IMGcontours):
            contours_poly[i] = cv2.approxPolyDP(c, 3, True)
            boundRect[i] = cv2.boundingRect(contours_poly[i])
            centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
        drawing = np.zeros((self.Photo_copy2.shape[0], self.Photo_copy2.shape[1], 3), dtype=np.uint8)
        # Draw polygonal contour + circles
        color=(256,256,256)
        for i in range(len(IMGcontours)):
            if(int(boundRect[i][3])>=2):#>=250#10
                cv2.rectangle(self.Photo_copy, (int(boundRect[i][0])-10, int(boundRect[i][1])-10),
                    (int(boundRect[i][0]+boundRect[i][2])+10, int(boundRect[i][1]+boundRect[i][3])+10), color, 10)
                cv2.drawContours(self.Photo_copy, contours_poly, i, color)
                cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 10)
                cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), 1, color, 10)
            

    
    def Show(self):
        self.Photo=cv2.resize(self.Photo,(960,540))
        self.Photo_copy2=cv2.resize(self.Photo_copy2,(960,540))
        #cv2.imshow('viewer',self.Photo)
        cv2.imshow('viewer2',self.Photo_copy)
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
