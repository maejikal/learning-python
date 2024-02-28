import socket

client_socket = socket.socket()
address = '127.0.0.1'
port = 12345

client_socket.connect((address, port))
print('connected, waiting for secret word.')
print('Menu:\n1) Guess a letter\n2) Guess a word\n3) Quit')

#receive length of word
length = client_socket.recv(1024).decode()[6]
guessed = ["?"]*int(length)
print("Current word guessed: " + ''.join(guessed))

while True:
    print('\nMenu:\n1) Guess a letter\n2) Guess a word\n3) Quit')
    menu = input("Enter your option: ")
    if menu not in '123':
        print('Invalid option, enter 1, 2 or 3')
        continue
    else:
        if menu == '1':
            letter = input("Enter a letter: ")
            if letter.isalpha() == False or len(letter) != 1:
                print('Invalid. Please enter a letter only.')
                client_socket.sendall(letter.encode() + b'\n') #send letter to invoke 'invalid' message from server
            else:
                msg = 'GUESS,' + letter + "\n"
                client_socket.sendall(msg.encode())

        if menu == '2':
            word = input('Enter a word: ')
            msg = 'HWORD,' + word + '\n'
            client_socket.sendall(msg.encode())

        if menu == '3':
            print('You quit.')
            client_socket.sendall(b'QUIT\n')
            break

    #check if win/lose:
    msg = client_socket.recv(1024).decode()
    if msg == "INVALID\n":
        continue
    if msg == "LOSE\n":
        print('You lose.')
        break
    if msg == "WIN\n":
        print('You win.')
        break

    #if guess is not correct, dont change 'guessed':
    if msg == 'GUESS\n':
        pass
    else:
    #display hidden word and letters guessed if correct.
        pos = msg[6:-1].split(',')
        for i in pos:
            guessed[int(i)] = letter
    print("Current word guessed: " + ''.join(guessed))
    continue

client_socket.close()