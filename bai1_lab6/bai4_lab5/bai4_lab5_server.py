from multiprocessing import connection
import socket
import os
import threading

server_address = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
server_address2 = ('localhost', 8001)
s.bind(server_address)
s2.bind(server_address2)
s.listen(5)
s2.listen(5)

def handl_client(connect):
    requestFromClient = connect.recv(1024)
    print("Yeu cau tu client: ",requestFromClient.decode())
    data = (requestFromClient.decode()).split(" ")
    protocol = data[0]
    fileName = data[1]
    
    msgSuccess = "OK"
    msgError = "ERROR"
    msgErrorRequest = "Yeu cau khong dung"
    existsfile = os.path.exists(fileName)
    if existsfile == True:
        connect.send(msgSuccess.encode())
        connect2, client_address2 = s2.accept()
        print("Start up on port 8001...")
        if protocol == 'GET':
            f = open(fileName, 'rb')
            while True:
                data1 = f.read(1024)
                while (data1):
                    connect2.send(data1)
                    data1 = f.read(1024)
                if not data1:
                    f.close()
                    print("Closing connection")
                    connect2.close()
                    break
            connect2.close()
            # break
        elif protocol == 'DELETE':
            print("Request from client: ",requestFromClient.decode())
            os.remove(fileName)
            msg="Delete "+ fileName +" => success"
            connect2.send(msg.encode())
            # break
        else:
            connect2.send(msgErrorRequest.encode())
    else:
        connect.send(msgError.encode())
        print("Closing connection")
        connect.close()
        # break 
    return 
while True:
    print("Start up on port 8000...")
    connect, client_address2 = s.accept()
    t = threading.Thread(target=handl_client, args=(connect,))
    # thread starting
    t.start()