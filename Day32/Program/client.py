import socket

csoc = socket.socket()
csoc.connect(('localhost',9999))
name = input(('Enter your name:'))
csoc.send(bytes(name,'utf-8'))
msg = csoc.recv(1000).decode()
print(msg)