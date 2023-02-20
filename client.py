import socket
from time import time 
from datetime import datetime
import uuid
start=time()
host=(socket.gethostbyname(socket.gethostname()))
serverPort=1356
clientSocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,serverPort))
IP_address = input("enter an IP address: ")
clientSocket.send(IP_address.encode())
# print a message with the request details and the exact time sent
print("request:", IP_address, "received at time: ", datetime.utcnow())
answer=clientSocket.recv(1024)
# time at which message was recieved 
print('From Server:', answer)
print("response exact time:", datetime.utcnow())
clientSocket.close()
print ("The MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
end=time()
print("total round trip: ", end-start)

