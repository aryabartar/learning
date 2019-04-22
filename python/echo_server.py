import socket

HOST="127.0.0.1"
PORT=1379

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1) 

try:
    while True:
        client_socket, address= s.accept()
        print("Accepting connection from: " , address)

        while True:
            message= client_socket.recv(1024).decode() 
            print("Client message is: " , message)
            if message == "" : 
                break
            client_socket.sendall(message.encode())
            
        print ("closing connection!")
except:
    print ("CLOSING")
    s.close()