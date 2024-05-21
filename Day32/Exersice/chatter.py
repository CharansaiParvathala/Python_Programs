import socket

chat = socket.socket()
chat.connect(('localhost',9999))
stop = False
msg = None
print("Type 'stop' to exit.")
try:
    while not stop:
        if msg == 'stop':
            stop = True
        else:
            msg = input('Msg:')
            chat.send(msg.encode('utf-8'))
            print(chat.recv(1024).decode('utf-8'))
except:
    print('You cant chat right now!')
chat.close()