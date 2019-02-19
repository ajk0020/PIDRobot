import turtle
import os
import math

def setupScreen():
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Algorithm");

    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("black")
    border_pen.penup()
    border_pen.setposition(-350, 0)
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
    grid_pen.setposition(-350, 0)
    grid_pen.pendown()
    grid_pen.pensize(1)

    grid_pen.fd(350)
    grid_pen.lt(90)
    grid_pen.fd(300)
    grid_pen.hideturtle()

    textLeft = turtle.Turtle()
    textLeft.setposition(-395, 0)
    textLeft.write("-350", font=("Arial", 16, "normal"))
    textLeft.penup()
    textLeft.hideturtle()

    textCenter = turtle.Turtle()
    textCenter.setposition(0, -25)
    textCenter.write(" 0", font=("Arial", 16, "normal"))
    textCenter.penup()
    textCenter.hideturtle()

    textCenterUp = turtle.Turtle()
    textCenterUp.setposition(0, 305)
    textCenterUp.write("300", font=("Arial", 16, "normal"))
    textCenterUp.penup()
    textCenterUp.hideturtle()

    textCenter = turtle.Turtle()
    textCenter.setposition(370, 0)
    textCenter.write("350", font=("Arial", 16, "normal"))
    textCenter.penup()
    textCenter.hideturtle()

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




def main():
    setupScreen()

    puckARRAY = []
    lineARRAY = []

    straight = False;
    upDown = False;
    direction = ""
    finalPoint = ""
    finalPredict = ""

    for x in range(0,100):

        #Enter location and add point to graph
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

        #if theres more than 3 points on graph remove the oldest one
        if(len(puckARRAY) >= 3):
            puckARRAY[0].clear()
            puckARRAY[0].ht()

            puckARRAY.pop(0)

        #if there's exactly 2 points draw line between them
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

            #calculate distance between the two points
            distance = pointDistance(x1,y1,x2,y2)

            #calculate slope between the two points
            if(x2 == x1):
                print("Going straight up or down")
                slope = 0
                upDown = True
                straight = False
            elif(y2 ==y1):
                print("Going in stright line")
                slope = 0
                straight = True
                upDown = False
            else:
                slope = (y2 - y1) / (x2 - x1)
                straight = False;
                upDown = False;


            #calulcate intercept of the line
            intercept = y2 - (slope * x2)

            print("Distance between points: {}".format(distance))
            print("Slope: {}".format(slope))
            print("Intercept: {}".format(intercept))
            print("Slope Intercept Form: y = mx + B".format(slope, intercept))
            print("Slope Intercept Form: y = {}x + {}".format(slope,intercept))

            #boundaries of the table
            minY = 0
            maxY = 300
            minX = -350
            maxX = 350


            interceptPointARRAY = []


            #if the line is not going straight up/down or left/right
            if((straight == False)and (upDown == False)):

                #test the point at which the line will intercept with upper or lower boundary of table
                interceptPoint = interceptVector(slope,intercept,direction)

                print("Intercept Point: {}".format(interceptPoint))

                #if intercept point exceeds boundary values then there will be no reflection
                #in other words, the line is pointing towards the goal line
                if((interceptPoint[0] > 350) or (interceptPoint[0] < -350)):
                    reflect = False
                else:
                    reflect = True

                #if there's a reflection, calculate all theoretical bounce points
                #untiul you reach the goal
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

                        #if theoretical intercept point = (x2,y2) then you don't need to calculate the distance
                        #between theoretical point and (x2,y2)
                        if((x1Predict == x2Predict) and (y1Predict == y2Predict)):
                            print("No need to calculate DISTANCE")
                            print(puckARRAY[0].pos()[1])
                            distance = math.sqrt((x2Predict - puckARRAY[0].pos()[0]) ** 2 + (y2Predict - puckARRAY[0].pos()[1]) ** 2)
                            theta = math.acos(float(abs(y2Predict-puckARRAY[0].pos()[1]) / distance))*(180/math.pi)
                            print("Theta: {}".format(theta))
                        else:
                            print("Distance between [{},{}] and [{},{}]: {}".format(x1Predict,y1Predict,x2Predict,y2Predict,distance))
                            distance = math.sqrt((x2Predict - x1Predict) ** 2 + (y2Predict - y1Predict) ** 2)
                            theta = math.acos(float(abs(x2Predict-x1Predict)/distance))*(180/math.pi)
                            print("Theta: {}".format(theta))

                        print("Impact Point: ({},{})".format(x2Predict,y2Predict))

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

                        print("X: {}".format(reflectionX))
                        print("Y: {}".format(reflectionY))

                        puckPredict = turtle.Turtle()
                        puckPredict.color("purple")
                        puckPredict.shape("circle")
                        puckPredict.shapesize(1.5, 1.5)
                        puckPredict.penup()
                        puckPredict.speed(0)
                        puckPredict.setposition(reflectionX, reflectionY)
                        predictedPUCK.append(puckPredict)


                        reflect = False


                #if there's no reflection, calculate final point
                elif(reflect == False):
                    if(direction == "right"):
                        finalPoint = [maxX,slope*maxX + intercept]
                    elif(direction == "left"):
                        finalPoint = [minX,slope*minX + intercept]

                    print("IMPACT AT: {}".format(finalPoint))

                    #draw point on graph indicating final point
                    finalPredict = turtle.Turtle()
                    finalPredict.color("red")
                    finalPredict.shape("circle")
                    finalPredict.shapesize(1.5, 1.5)
                    finalPredict.penup()
                    finalPredict.speed(0)
                    finalPredict.setposition(float(finalPoint[0]), float(finalPoint[1]))

                input("Press enter to continue\n")

                for point in predictedPUCK:
                    point.clear()
                    point.ht()
                predictedPUCK = []
            #calculate final point for straight line trajectory
            #this is a different case than the one above
            elif(straight == True):
                if (direction == "right"):
                    finalPoint = [maxX, slope * maxX + intercept]
                elif (direction == "left"):
                    finalPoint = [minX, slope * minX + intercept]

                print("IMPACT AT: {}".format(finalPoint))

                #draw point on graph indicating final point
                finalPredict = turtle.Turtle()
                finalPredict.color("red")
                finalPredict.shape("circle")
                finalPredict.shapesize(1.5, 1.5)
                finalPredict.penup()
                finalPredict.speed(0)
                finalPredict.setposition(float(finalPoint[0]), float(finalPoint[1]))




        #remove final point and restart loop, receiving an updated position of puck
        if(finalPredict):
            input("Press Enter to Continue")
            finalPredict.clear()
            finalPredict.ht()


if __name__ == "__main__":
    main()