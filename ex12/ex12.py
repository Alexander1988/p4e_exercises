import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    handle=data.decode()
    print(handle,end='')
    #for line in handle:
        #line=line.rstrip() #delete all spaces at the right of each line

        #num=re.findall('[0-9]+',line)#find all numbers in the line (greedy!)
        #print(line)

mysock.close()
