import serial
import time
from PIDcode import algorithm

try:
    ser = serial.Serial("/dev/ttyACM0",9600,timeout=10)
    if ser.is_open:
        print ("Connection ACM0 opened..")
except:
    ser = serial.Serial("/dev/ttyACM1",9600,timeout=10)
    if ser.is_open:
        print ("Connection ACM1 opened..")


while True:
    x, inbuf = algorithm(10,20,50,100)
    inbuf = str(int(inbuf))
    ser.write(inbuf.encode(encoding='ascii'))
    print ("Sent " + inbuf)

