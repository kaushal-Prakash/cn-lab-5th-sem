import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))

data = input("Enter message : ")
client.send(data.encode())
response = client.recv(1024).decode()
print("Server response : ",response)
client.close()