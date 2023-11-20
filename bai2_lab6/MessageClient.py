from threading import Thread
import socket

host = socket.gethostname()
port = 8001
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
            print(f"Received message from PC1: {data}")
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


while True:
    data = input()
    if not data:
        break
    s = sendThread(host, 8000, sock, data)
    s.start()
    