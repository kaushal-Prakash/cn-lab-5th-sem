import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("0.0.0.0",8080))
server.listen(1)
print("Server running on port 8080..")
conn,add = server.accept()
print("Connected clinet : ",add)
data = conn.recv(1024).decode()
data = data.upper()
conn.send(data.encode())
conn.close()
server.close()