import socket
import json
import random

sock = socket.socket()

sock.bind(('', 9090))

sock.listen(1)

data = {
    "msg": "Hello,i'am caht bot. Let say hello to each other. Just send me hello",
    "action": "start"
}

data2 = {
    "msg": "Hello, my name is ChattiB",
    "action": "hello"
}

s_data = json.dumps(data)
s_data2 = json.dumps(data2)

while True:
    client, addr = sock.accept()
    print(f"Получен запрос на соединение от {str(addr)}")
    msg = client.recv(10000)
    msg.decode('utf-8')
    if msg.decode('utf-8') == 'hello':
        client.send('Hello, fam'.encode('utf-8'))
    elif msg.decode('utf-8') == 'end':
        print('Завершение сеанса')
        break

    client.close()
