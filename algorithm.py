import turtle
import os
import math

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

    print("SLOPE: {}".format(slope))
    print("DIRECTION: {}".format(direction))

    if ((slope < 0) and (direction == "right")):
        interceptPoint = [xLow, minY]  # bottom right
    elif ((slope > 0) and (direction == "right")):
        interceptPoint = [xHigh, maxY]  # top right
    elif ((slope < 0) and (direction == "left")):
        interceptPoint = [xHigh, maxY]  # top left
    elif ((slope > 0) and (direction == "left")):
        interceptPoint = [xLow, minY]  # bottom left

    return interceptPoint

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Algorithm");

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-350,0)
border_pen.pendown()
border_pen.pensize(3)


border_pen.fd(700)
border_pen.lt(90)
border_pen.fd(300)
border_pen.lt(90)
border_pen.fd(700)
border_pen.lt(90)
border_pen.fd(300)
border_pen.lt(90)
border_pen.hideturtle()

grid_pen = turtle.Turtle()
grid_pen.speed(0)
grid_pen.color("black")
grid_pen.penup()
grid_pen.setposition(-350,0)
grid_pen.pendown()
grid_pen.pensize(1)

grid_pen.fd(350)
grid_pen.lt(90)
grid_pen.fd(300)
grid_pen.hideturtle()

textLeft = turtle.Turtle()
textLeft.setposition(-395,0)
textLeft.write("-350", font=("Arial", 16, "normal"))
textLeft.penup()
textLeft.hideturtle()

textCenter = turtle.Turtle()
textCenter.setposition(0,-25)
textCenter.write(" 0", font=("Arial", 16, "normal"))
textCenter.penup()
textCenter.hideturtle()

textCenterUp = turtle.Turtle()
textCenterUp.setposition(0,305)
textCenterUp.write("300", font=("Arial", 16, "normal"))
textCenterUp.penup()
textCenterUp.hideturtle()


textCenter = turtle.Turtle()
textCenter.setposition(370,0)
textCenter.write("350", font=("Arial", 16, "normal"))
textCenter.penup()
textCenter.hideturtle()

puckARRAY = []
lineARRAY = []

straight = False;
upDown = False;
direction = ""
finalPoint = ""
finalPredict = ""

for x in range(0,100):
    x = input("Enter location x: ")
    y = input("Enter location y: ")
    puck = turtle.Turtle()
    puck.color("blue")
    puck.shape("circle")
    puck.shapesize(1.5,1.5)
    puck.penup()
    puck.speed(0)
    puck.setposition(float(x),float(y))
    puckARRAY.append(puck)


    if(len(puckARRAY) >= 3):
        puckARRAY[0].clear()
        puckARRAY[0].ht()

        puckARRAY.pop(0)

    if(len(puckARRAY) == 2):
        print("Puck 1: {}".format(puckARRAY[0].pos()))
        print("Puck 2: {}".format(puckARRAY[1].pos()))

        x1 = puckARRAY[0].pos()[0]
        y1 = puckARRAY[0].pos()[1]

        x2 = puckARRAY[1].pos()[0]
        y2 = puckARRAY[1].pos()[1]

        if((x2-x1) >= 0):
            color = "green"
            direction = "right"
        else:
            color = "red"
            direction = "left"

        arrow = turtle.Turtle()
        lineARRAY.append(arrow)

        if (len(lineARRAY) >= 2):
            lineARRAY[0].clear()
            lineARRAY[0].ht()
            lineARRAY.pop(0)

        arrow.color(color)
        arrow.penup()
        arrow.setposition(x1,y1)
        arrow.pendown()
        arrow.goto(x2,y2)
        arrow.hideturtle()

        distance = pointDistance(x1,y1,x2,y2)

        if(x2 == x1):
            print("Going straight up or down")
            slope = 0
            upDown = True
        elif(y2 ==y1):
            print("Going in stright line")
            slope = 0
            straight = True
        else:
            slope = (y2 - y1) / (x2 - x1)
            straight = False;
            upDown = False;


        intercept = y2 - (slope * x2)

        print("Distance between points: {}".format(distance))
        print("Slope: {}".format(slope))
        print("Intercept: {}".format(intercept))
        print("Slope Intercept Form: y = mx + B".format(slope, intercept))
        print("Slope Intercept Form: y = {}x + {}".format(slope,intercept))

        minY = 0
        maxY = 300
        minX = -350
        maxX = 350


        interceptPointARRAY = []



        if((straight == False)and (upDown == False)):
            # check lower boundary
            # xLow = (minY - intercept) / slope
            # xHigh = (maxY - intercept) / slope
            #
            #
            # print("SLOPE: {}".format(slope))
            # print("DIRECTION: {}".format(direction))
            #
            # if((slope < 0) and (direction=="right")):
            #     interceptPoint = [xLow,minY] #bottom right
            # elif((slope > 0) and (direction=="right")):
            #     interceptPoint = [xHigh,maxY] #top right
            # elif ((slope < 0) and (direction == "left")):
            #     interceptPoint = [xHigh,maxY] #top left
            # elif ((slope > 0) and (direction == "left")):
            #     interceptPoint = [xLow,minY] #bottom left

            interceptPoint = interceptVector(slope,intercept,direction)

            print("Intercept Point: {}".format(interceptPoint))

            if((interceptPoint[0] > 350) or (interceptPoint[0] < -350)):
                reflect = False
            else:
                reflect = True

            if(reflect == True):
                print("Intercept Point: {}".format(interceptPoint))
                previousX = x2
                previousY = y2
                while(reflect == True):

                    interceptPointARRAY.append(interceptPoint)
                    predictedPUCK = []
                    puckPredict = turtle.Turtle()
                    puckPredict.color("green")
                    puckPredict.shape("circle")
                    puckPredict.shapesize(1.5, 1.5)
                    puckPredict.penup()
                    puckPredict.speed(0)
                    puckPredict.setposition(float(interceptPoint[0]), float(interceptPoint[1]))
                    predictedPUCK.append(puckPredict)

                    x1Predict = previousX
                    y1Predict = previousY

                    x2Predict = puckPredict.pos()[0]
                    y2Predict = puckPredict.pos()[1]


                    print("x1: {} y1: {}".format(x1Predict,y1Predict))
                    print("x2: {} y2: {}".format(x2Predict,y2Predict))


                    if((x1Predict == x2Predict) and (y1Predict == y2Predict)):
                        print("No need to calculate DISTANCE")
                        print(puckARRAY[0].pos()[1])
                        distance = math.sqrt((x2Predict - puckARRAY[0].pos()[1]) ** 2 + (y2Predict - puckARRAY[0].pos()[1]) ** 2)
                        theta = math.asin(float(abs(y2Predict-puckARRAY[0].pos()[1]) / distance))
                        print("Theta: {}".format(theta))
                    else:
                        print("Distance between [{},{}] and [{},{}]: {}".format(x1Predict,y1Predict,x2Predict,y2Predict,distance))
                        distance = math.sqrt((x2Predict - x1Predict) ** 2 + (y2Predict - y1Predict) ** 2)
                        theta = math.asin(float(abs(y2Predict-y1Predict)/distance))
                        print("Theta: {}".format(theta))

                    if(direction == "right"):
                        xDir = 20
                        if(slope < 0):
                            yDir = 20
                        else:
                            yDir = -20
                    elif(direction == "left"):
                        xDir = -20
                        if(slope < 0):
                            yDir = -20
                        else:
                            yDir = 20

                    reflectionX =x2Predict+ xDir*math.sin(theta)
                    reflectionY = y2Predict+ yDir * math.cos(theta)

                    puckPredict = turtle.Turtle()
                    puckPredict.color("purple")
                    puckPredict.shape("circle")
                    puckPredict.shapesize(1.5, 1.5)
                    puckPredict.penup()
                    puckPredict.speed(0)
                    puckPredict.setposition(reflectionX, reflectionY)
                    predictedPUCK.append(puckPredict)

                    #randomPointX = 2sin(theta)
                    #randomPointY = 2cos(theta)

                    x1Predict = x2Predict
                    y1Predict = y2Predict

                    reflect = False



                    #reflect = False

            elif(reflect == False):
                if(direction == "right"):
                    finalPoint = [maxX,slope*maxX + intercept]
                elif(direction == "left"):
                    finalPoint = [minX,slope*minX + intercept]

                print("IMPACT AT: {}".format(finalPoint))

                finalPredict = turtle.Turtle()
                finalPredict.color("red")
                finalPredict.shape("circle")
                finalPredict.shapesize(1.5, 1.5)
                finalPredict.penup()
                finalPredict.speed(0)
                finalPredict.setposition(float(finalPoint[0]), float(finalPoint[1]))



        elif(straight == True):
            if (direction == "right"):
                finalPoint = [maxX, slope * maxX + intercept]
            elif (direction == "left"):
                finalPoint = [minX, slope * minX + intercept]

            print("IMPACT AT: {}".format(finalPoint))

            finalPredict = turtle.Turtle()
            finalPredict.color("red")
            finalPredict.shape("circle")
            finalPredict.shapesize(1.5, 1.5)
            finalPredict.penup()
            finalPredict.speed(0)
            finalPredict.setposition(float(finalPoint[0]), float(finalPoint[1]))



    if(finalPredict):
        input("Press Enter to Continue")
        finalPredict.clear()
        finalPredict.ht()




