import socket

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
