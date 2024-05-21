import socket

chat = socket.socket()
chat.bind(('localhost',9999))
print('Chat server created.')

chat.listen(1)

stop = False
msg = None
cl, addr = chat.accept()
print('client ready to chat')
print("Type 'stop' to exit.")
try:
    while not stop:
        if msg == 'stop':
            stop = True
        else:
            print(cl.recv(1024).decode('utf-8'))
            msg = input('Msg:')
            cl.send(msg.encode('utf-8'))
except:
    print('You cant chat right now!')
cl.close()
chat.close()