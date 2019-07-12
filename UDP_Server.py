import socket
#Create a IP Element
localIP="127.0.0.1"
#Create a valid port to check
localPort=20001
#Size of buffer element to be verified
bufferSize=1024

Server_msg="Hello Client"
bytesToSend= str.encode(Server_msg)

#Creating a datagram
UDPSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Bind w/ Address and IP
UDPSocket.bind((localIP,localPort))

print ("UDP Server up and listening")

#Listening for incoming packets
while True:
    bytesAddress=UDPSocket.recvfrom(bufferSize)
    message= bytesAddress[0]
    address= bytesAddress[1]
    clientMsg= "Message from CLient: {}".format(message)
    clientIP= "Client Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

#Send Reply CLient
    UDPSocket.sendto(bytesToSend,address)

msgClient="Hello UDP Server"
bytesSend= str.encode(msgClient)
serverAddPort=("127.0.0.1",20001)
bufferSize=1024

#Create UDP Socket on client side
UDPClientSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

#Send packet to Server
UDPClientSocket.sendto(bytesSend,serverAddPort)

msgFromServer=UDPClientSocket.recvfrom(bufferSize)

msg="Message from Server {}".format(msgFromServer[0])

print(msg)
