import socket 

HOST="127.0.0.1"
PORT=1379

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

try:
    while True:
        user_message = input ("::")
        s.sendall(user_message.encode())
        
        server_message=""
        server_echo = s.recv(1024).decode()
        server_message += server_echo
        while server_echo=="" : 
            server_echo = s.recv(1024).decode()
            server_message+=server_echo
        print(server_message)

except:
    s.close()
