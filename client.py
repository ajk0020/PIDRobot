import socket

TCP_IP = socket.gethostname()
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    #s.send(input("MSG: ").encode())
    MESSAGE = s.recv(1024)
    print(MESSAGE)
    #data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)