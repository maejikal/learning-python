import socket

server = socket.socket()

ip = '127.0.0.1'
port = 21324

server.bind((ip, port))
server.listen()

new, address = server.accept()

print('Connected to: ' + str(address))

while True:
    msg = input('Server: ') + '\n'
    new.sendall(b'Server: ' + msg.encode())
    
    client = b''
    while b'\n' not in client:
        client += new.recv(1024)
    if client == b'0\n':
        print('Client has terminated session.')
        break
    print(client.decode().strip())

new.close()
server.close()
