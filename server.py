import socket               # Import socket module
import _thread

def on_new_client(clientsocket,addr):
    while True:
        #msg = clientsocket.recv(1024)
        #print(msg)
        clientsocket.send(input("MSG: ").encode())
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5000                # Reserve a port for your service.

print ('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   _thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()