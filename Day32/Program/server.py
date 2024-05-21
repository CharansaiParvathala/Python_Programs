import socket

soc = socket.socket()
soc.bind(('localhost',9999))
print('Server Created')

soc.listen(2)
print('server waiting for the user')

while True:
    client, addr = soc.accept()
    name = client.recv(1000).decode()
    print(f'{name} connected to the server with {addr}')
    client.send(bytes(f'Hi {name} Welcome to the server.','utf-8'))
    client.close()