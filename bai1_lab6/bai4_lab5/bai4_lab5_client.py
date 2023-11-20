
import socket
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
server_address2 = ('localhost', 8001)

s.connect(server_address)
requestFromClient = input("Nhap yeu cau (GET/LIST/DELETE <file_name>) :")

fileName = requestFromClient.split(" ")[1]
protocol = requestFromClient.split(" ")[0]
existsfolder = os.path.isdir(fileName)

s.send(requestFromClient.encode())
data = s.recv(1024)
print("Phan hoi tu server cho yeu cau => " +data.decode())

if data.decode() == "OK":
    s2.connect(server_address2)

    if protocol == "GET":
        data1 = s2.recv(1024)
        f = open('content.txt','wb')
        f.write(data1)
        f.close()
        print("Copy noi dung file tu '" + fileName+"' into 'content.txt' => Success")
        s2.close()
    if protocol == 'DELETE':
        data1 = s2.recv(1024)
        print(data1.decode())  
else:
    s.close()
    s2.close()