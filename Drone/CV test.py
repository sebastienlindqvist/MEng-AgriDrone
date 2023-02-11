import cv2
print( cv2.__version__ )
from PIL import Image
import numpy as np

Photo=cv2.imread("/home/pi/Desktop/Drone/test_image.jpg")
Photo_copy=np.copy(Photo)



Photo_copy=cv2.GaussianBlur(Photo_copy, (31,31),0)
Photo_copy=cv2.cvtColor(Photo_copy,cv2.COLOR_BGR2HSV)

H,S,V=cv2.split(Photo_copy)
H=cv2.resize(H,(960,540))
S=cv2.resize(S,(960,540))
V=cv2.resize(V,(960,540))
cv2.imshow('Value',V)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.waitKey(0)
