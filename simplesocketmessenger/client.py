import socket

client = socket.socket()

client.connect(('127.0.0.1', 21324))

print('Enter 0 to exit.') #client ends the connection
print('Waiting for server...')

while True:
    server = b''
    while b'\n' not in server:
        server += client.recv(1024)
    print(server.decode().strip())

    msg = input('Client: ') + '\n'
    
    
    if msg.strip() == '0':
        client.sendall(msg.encode())
        print('Terminating session...')
        break
    client.sendall(b'Client: ' + msg.encode())
client.close()
    
    
