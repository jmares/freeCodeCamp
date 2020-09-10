import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pannix.net', 80))
cmd ='GET http://www.pannix.net/index.html HTTP/1.0\n\n'.encode()
#mysock.connect(('data.pr4e.org', 80))
#cmd ='GET http://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()