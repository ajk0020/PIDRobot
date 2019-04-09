#!/usr/bin/env python3
import cv2
import numpy as np
import imutils
import time
from PIDcode import algorithm
import socket
import sys
import serial
import math 
##try:
##    ser = serial.Serial("/dev/ttyACM0",9600,timeout=10)
##    if ser.is_open:
##        print ("Connection ACM0 opened..")
##except:
##    ser = serial.Serial("/dev/ttyACM1",9600,timeout=10)
##    if ser.is_open:
##        print ("Connection ACM1 opened..")

s = socket.socket()         # Create a socket object
host = "192.168.0.1"    # Get local machine name
port = 5000                # Reserve a port for your service.

print ('Server started!')
print('Waiting for clients...')

#s.bind((host, port))        # Bind to the port
#s.listen(5)                 # Now wait for client connection.
#c, addr = s.accept()        # Establish connection with client.
#print('Got connection from', addr)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
cap.set(cv2.CAP_PROP_FPS,120)
print("FPS", cap.get(cv2.CAP_PROP_FPS))



#cap.set(cv2.CAP_PROP_FRAME_COUNT,45)

x = 0
y = 0
oldx = 0
oldy = 0
count = 0
old_outy = 0
impact = 0
number_range = [0,0,0]

while(1):
    #print("FPS", cap.get(cv2.CAP_PROP_FPS))
    start = time.time()

    # Take each frame
    _, frame = cap.read()

    (h,w) = frame.shape[:2]
    center = (w/2,h/2)

    M = cv2.getRotationMatrix2D(center,-2.5,1.0)
    rotated = cv2.warpAffine(frame,M,(w,h))
    frame = rotated
    frame = frame[40:210,0:320]

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue = np.array([90,50,50])
    # upper_blue = np.array([110,255,255])

    # lower_blue = np.array([90,64,98])

    lower_blue = np.array([0, 79, 24])
    upper_blue = np.array([8,255,204])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    #cv2.imshow('res',res)


    try:
        points = cv2.findNonZero(mask);
        avg = np.mean(points,axis=0) 
        
    except IndexError:
        avg = [[-500,-500],[-500,-500]]
        
    
    if(avg[0][0] > 0 and avg[0][1] > 0):
        end = time.time()

        xconversion = 700
        yconversion = 300

        xrange = 305
        yrange = 139

        xoffset = 10
        yoffset = 14

        x = int(avg[0][0]) - xoffset
        y = int(avg[0][1]) - yoffset
        
    
        x = (x/xrange) * xconversion
        y = (1-(y/yrange))* yconversion

        x = x-350

        if(x < -350):
            x = -350
        elif(x > 350):
            x = 350

        if(y < 0):
            y = 0
        elif(y > 300):
            y = 300

        if(oldx == 0 and oldy == 0):
            oldx = x
            oldy = y

##        print("original x:{} original y:{} ".format(int(avg[0][0]),int(avg[0][1]) ))
##        print("mew x     :{} new y     :{}".format(int(x),int(y)))
        
        count+=1

        if(count == 1):
            #print("original x:{} original y:{} ".format(int(oldx),int(oldy)))
            #print("mew x     :{} new y     :{}".format(int(x),int(y)))

            outx,outy = algorithm(int(oldx),int(oldy),int(x),int(y))
        
            
            if(outx != -900 and outy != -900):
                number_range.insert(0,outy)
                if(abs(number_range[0]-number_range[1]) < 50 and
                   abs(number_range[0]-number_range[2]) < 50 and
                   abs(number_range[1]-number_range[2]) < 50):
                    if(outx > 0):
                        print("impact x  :{} impact y  :{}".format(int(outx),int(number_range[0])))
                oldx = x
                oldy = y
                number_range.pop()
##
##                inbuf = str(int(outy))
##                ser.write(inbuf.encode(encoding='ascii'))
                #print ("Sent " + inbuf)
##                time.sleep(5) 

            count = 0
            
            
        #if(x != -500 and y != -500):
         #   #print("x:{} y:{} Time:{}".format(int(x),int(y),end-start))

            #final serial code
          #  outx,outy = algorithm(oldx,oldy,x,y)

           # if(outx != -900 and outy != -900):
            #    if(outy > 0 and outy < 350):
             #       message = ("{},{}".format(int(x),int(y)))
              #      print("x:{} y:{}".format(int(x),int(y)))
               #     try:
                #        recv = c.recv(1024)
                 #       recv = recv.decode()
                  #      if(recv == "ready"):
                   #         c.send(message.encode())
                            
                   # except (BrokenPipeError, IOError):
                    #    print("error occured")
                     #   sys.exit()
                        
                            
                    
        
            #old_outy = outy
            #oldx = x
            #oldy = y

    
    
    #cv2.waitKey()

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

message = "close"
#c.send(message.encode())
#s.close()
cv2.destroyAllWindows()
