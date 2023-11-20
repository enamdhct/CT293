import threading
import socket
import sys
from concurrent.futures import thread
    
def int_to_String(number):
    if number==0:
        result="khong"
    elif number==1:
        result="mot"
    elif number==2:
        result="hai"
    elif number==3:
        result="ba"
    elif number==4:
        result="bon"
    elif number==5:
        result="nam"
    elif number==6:
        result="sau"
    elif number==7:
        result="bay"
    elif number==8:
        result="tam"
    elif number==9:
        result="chin"
    else:
        result="Khong phai la so nguyen"
    return result
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
s.bind(server_address)
s.listen(1)
def handle_client(connect):
        data = connect.recv(50)
        print('So nhan duoc tu client: ' + data.decode())
        print('Ket qua tra ve client')
        data = int(data)
        result = int_to_String(data)
        connect.sendall(result.encode())
        connect.close()
        return
while True:
    print("Server dang lang nghe...")
    connect, client_address = s.accept()  
    t = threading.Thread(target=handle_client, args=(connect,))
    t.start()