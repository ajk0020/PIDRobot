import os
import math
import random


def pointDistance(x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def interceptVector(slope,intercept,direction):
    minY = 0
    maxY = 300
    minX = -350
    maxX = 350

    xLow = (minY - intercept) / slope
    xHigh = (maxY - intercept) / slope

    if ((slope < 0) and (direction == "right")):
        interceptPoint = [xLow, minY]  # bottom right
    elif ((slope > 0) and (direction == "right")):
        interceptPoint = [xHigh, maxY]  # top right
    elif ((slope < 0) and (direction == "left")):
        interceptPoint = [xHigh, maxY]  # top left
    elif ((slope > 0) and (direction == "left")):
        interceptPoint = [xLow, minY]  # bottom left

    return interceptPoint




def algorithm(x1,y1,x2,y2):

    puckARRAY = []

    finalPoint = ""
    finalPredict = ""



    if((x2-x1) >= 0):
        direction = "right"
    else:
        direction = "left"


    #calculate distance between the two points
    distance = pointDistance(x1,y1,x2,y2)

    #calculate slope between the two points
    if(x2 == x1):
        slope = 0
        upDown = True
        straight = False
    elif(y2 ==y1):
        slope = 0
        straight = True
        upDown = False
    else:
        slope = (y2 - y1) / (x2 - x1)
        straight = False
        upDown = False

    #calulcate intercept of the line
    intercept = y2 - (slope * x2)

    #boundaries of the table
    minX = -350
    maxX = 350

    interceptPointARRAY = []
    predictedPUCK_ARRAY = []


    #if the line is not going straight up/down or left/right
    if((straight == False)and (upDown == False)):

        #test the point at which the line will intercept with upper or lower boundary of table
        interceptPoint = interceptVector(slope,intercept,direction)

        #if intercept point exceeds boundary values then there will be no reflection
        #in other words, the line is pointing towards the goal line
        if((interceptPoint[0] > maxX) or (interceptPoint[0] < minX)):
            reflect = False
        else:
            reflect = True

        #if there's a reflection, calculate all theoretical bounce points
        #untiul you reach the goal
        if(reflect == True):
            numOfReflections = 0
            previousX = x2
            previousY = y2
            while(reflect == True):

                numOfReflections += 1
                interceptPointARRAY.append(interceptPoint)
                predictedPUCK_ARRAY.append([interceptPoint[0],interceptPoint[1]])

                x1Predict = previousX
                y1Predict = previousY

                x2Predict = interceptPoint[0]
                y2Predict = interceptPoint[1]

                #if theoretical intercept point = (x2,y2) then you don't need to calculate the distance
                #between theoretical point and (x2,y2)
                if((x1Predict == x2Predict) and (y1Predict == y2Predict)):
                    distance = math.sqrt((x2Predict - float(x1)) ** 2 + (y2Predict - float(y1)) ** 2)
                    theta = math.acos(float(abs(x2Predict-float(x1)) / distance))*(180/math.pi)

                else:
                    distance = math.sqrt((x2Predict - x1Predict) ** 2 + (y2Predict - y1Predict) ** 2)
                    theta = math.acos(float(abs(x2Predict-x1Predict)/distance))*(180/math.pi)

                if(direction == "right"):
                    xDir = 50
                    if(slope < 0):
                        yDir = 50
                    else:
                        yDir = -50
                elif(direction == "left"):
                    xDir = -50

                    if(slope < 0):
                        yDir = -50
                    else:
                        yDir = 50


                reflectionX = x2Predict + xDir * (math.cos(math.radians(theta)))
                reflectionY = y2Predict + yDir*(math.sin(math.radians(theta)))

                predictedPUCK_ARRAY.append([reflectionX,reflectionY])

                previousX = x2Predict
                previousY = y2Predict

                slope = ((reflectionY - y2Predict) / (reflectionX - x2Predict))+0.001
                intercept = reflectionY - (slope * reflectionX)
                if ((reflectionX - x2Predict) >= 0):
                    direction = "right"
                else:
                    direction = "left"

                interceptPoint = interceptVector(slope,intercept,direction)

                if ((interceptPoint[0] > 350) or (interceptPoint[0] < -350)):
                    reflect = False
                else:
                    reflect = True

            if (direction == "right"):
                finalPoint = [maxX, slope * maxX + intercept]
            elif (direction == "left"):
                finalPoint = [minX, slope * minX + intercept]

            # draw point on graph indicating final point
            finalPredict = [finalPoint[0],finalPoint[1]]


        #if there's no reflection, calculate final point
        elif(reflect == False):
            if(direction == "right"):
                finalPoint = [maxX,slope*maxX + intercept]
            elif(direction == "left"):
                finalPoint = [minX,slope*minX + intercept]

            #draw point on graph indicating final point
            finalPredict = [finalPoint[0], finalPoint[1]]

    #calculate final point for straight line trajectory
    #this is a different case than the one above
    elif(straight == True):
        if (direction == "right"):
            finalPoint = [maxX, slope * maxX+ intercept]
        elif (direction == "left"):
            finalPoint = [minX, slope * minX + intercept]

        #draw point on graph indicating final point
        finalPredict = [finalPoint[0], finalPoint[1]]

    #remove final point and restart loop, receiving an updated position of puck
    #if(finalPredict):
    #    print("IMPACT POINT at: {}".format(finalPoint))


    try:
        if(numOfReflections > 1):
            return(-900,-900)
        else:
            return (finalPoint[0], finalPoint[1])
    except IndexError:
        return (-900,-900);

