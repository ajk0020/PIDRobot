import serial
import time
from PIDcode import algorithm

x1 = input("Input the first x position: ")
y1 = input("Input the first y position: ")
x2 = input("Input the second x position: ")
y2 = input("Input the second y position: ")

start = time.time_ns()
x = algorithm(int(x1),int(y1),int(x2),int(y2))
end = time.time_ns()
print(x)
print(end-start)

