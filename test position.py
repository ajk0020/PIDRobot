from PIDcode import algorithm

inbuf = algorithm(10,20,50,100)
print(float(inbuf))

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
    inbuf = str(int(algorithm(10,20,50,100)))
    ser.write(inbuf.encode(encoding='ascii'))
    print ("Sent " + inbuf)
    time.sleep(5)
