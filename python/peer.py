import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 12345))
message=b'hello'
s.sendto(message, ('127.255.255.255', 12346))
print("I am done!")