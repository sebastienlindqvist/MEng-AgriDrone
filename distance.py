#import libraries
from PIL import Image


#variables

#centre=

#modules centre distances from the camera

# 1cm = 1786.571 cm*pixels
#1 3 cm above
#2 3 cm right
#3 3 cm below
#4 3 cm left

def getHeighht():
    altitude=1.5 #vehicle.alltitude() #this will give in metres
    altitude = altitude*10
    
    # 0,0 being upper left of image
    # below i adapt where the collector modules are
    while True:
        altitude=1.5 #vehicle.alltitude() #this will give in metres
        altitude = altitude*10
        if CurrentSample == 1:
            #1 collector in pixels
            width = Original_width
            height = Original_height - 3*(1786.571/altitude)#3 is 3cm from centre
        elif CurrentSample ==2:
            #2 collector in pixels
            width = Original_width + 3*(1786.571/altitude)
            height = Original_height 
        elif CurrentSample ==3:
            # #3 collector in pixels
            width = Original_width
            height = Original_height + 3*(1786.571/altitude)
        elif CurrentSample ==4:
            #4 collector in pixels
            width = Original_width - 3*(1786.571/altitude)
            height = Original_height


def centre():
    im = Image.open('whatever.png')
    Original_width, Original_height = im.size
    #image=2
    #PlantCOMheight=height
    #PlantCOMwidth=width


def DistanceDifference(width,height):
    # if plant is right of collector. difference is possitive
    # if plant is left of collector. difference is negative
    # if plant is below of collector. difference is possitive
    # if plant is above of collector. difference is negative
    plantWidth=0
    plantHeight=0
    #
    widthDifference=plantWidth-width
    heightDifference=plantHeight-height
    #cm*pixels/pixels
    realHeight=1786.571/heightDifference
    realWidth=1786.571/widthDifference
    #vehicle.simple_goto()
    

    
    
    
