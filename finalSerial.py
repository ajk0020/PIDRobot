import serial
import time

try:
    ser = serial.Serial("/dev/ttyACM0",9600,timeout=10)
    if ser.is_open:
        print ("Connection ACM0 opened..")
except:
    ser = serial.Serial("/dev/ttyACM1",9600,timeout=10)
    if ser.is_open:
        print ("Connection ACM1 opened..")


while True:
    inbuf = input()
    if inbuf == ('exit'):
            ser.close()
            exit()
    else:
        ser.write(inbuf.encode(encoding='ascii'))
        print ("Sent " + inbuf)
        time.sleep(1)
