import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECTED"
SERVER = "192.168.0.34"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


nickname = input('Nickname: ')


def write(data):
    with open("test.text", 'w') as file:
        file.write(data)
        file.close()


write('a')


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    received = client.recv(2048).decode(FORMAT)
    print(f'[{nickname}] ' + received)


while True:
    answer = input('Message: ')
    if 'disconnect' in answer.lower():
        break
    else:
        send(answer)

send(DISCONNECT_MESSAGE)
