import socket
import json

sock = socket.socket()

sock.connect(('localhost', 9090))

result = ""

while True:
    msg = input('Hello,iam chat bot.Let say hello to each other. Just send me hello \n')
    sock.send(msg.encode('utf-8'))
    data = sock.recv(1024)
    result = data.decode("utf-8")
    print(result)
    if result == 'Hello, fam':
        print('Now thats all i can. Come again later and you will see how i grown up. Send my end to kill session. \n')
        msg = input()
        sock.send(msg.encode('utf-8'))
        if msg == 'end':
            break


sock.close()
