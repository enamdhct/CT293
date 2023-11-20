from threading import Thread
import socket

host = socket.gethostname()
port = 8000
buffer_size = 1024

class recvThread(Thread):
    def __init__(self, host, port, sock):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = sock
        
    def run(self):
        while True:
            data, addr = self.sock.recvfrom(buffer_size)
            data = data.decode()
            print(f"Received message from PC2: {data}")
            print(f"Input message: ")

class sendThread(Thread):
    def __init__(self, host, port, sock, data):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = sock
        self.data = data
    
    def run(self):
        self.sock.sendto(self.data.encode(), (self.host, self.port))

    

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

r = recvThread(host, port, sock)
r.start()

print(f"Input message: ")
while True:
    data = input()
    if not data:
        break
    s = sendThread(host, 8001, sock, data)
    s.start()