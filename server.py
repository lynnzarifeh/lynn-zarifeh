import socket

from time import time
from datetime import datetime
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort = 1356
PC_IP= (socket.gethostbyname(socket.gethostname()))
serverSocket.bind((PC_IP,serverPort))
serverSocket.listen(1)
print("the server is ready to receive")
while True:
        connectionSocket, addr=serverSocket.accept()
        IP_address = connectionSocket.recv(1024)
        print("address of client: ",addr)
        #print a message describing this request with the IP and exact time of the request
        print ("the client's request : ", IP_address.decode())
        socketNew= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socketNew.connect((IP_address.decode(),80))
        request="GET / HTTP/1.1\r\nHost:" + IP_address.decode()+"\r\n\r\n"
        #send the client's request to the destination server
        print ("client's request to destination:", request, "at exact time", datetime.utcnow()) 
        socketNew.send(request.encode())   
        reply=socketNew.recv(1024)   
        #print the message and the time it was received at
        print("reply was received at time:",datetime.utcnow())
        connectionSocket.send(reply)
        print("reply was sent at time:",datetime.utcnow())
        serverSocket.close()
        socketNew.close()
  
    
    
        
    
    
