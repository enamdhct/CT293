import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
s.connect(server_address)

try:
    print("Nhap 1 so tu 0 den 9")
    number = input()
    print("So vua nhap: ", number)
    s.sendall(number.encode())

    amount_received = 0
    amount_expected = len(number)
    msg = []
    while amount_received < amount_expected:
        data = s.recv(100)
        amount_received += len(data)
        msg.append(data)
        print('Ket qua =>', b''.join(msg).decode())

finally:
    print('Nhan phan hoi tu server thanh cong!')
    s.close()
