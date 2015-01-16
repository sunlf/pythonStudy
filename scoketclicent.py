# -*- coding:utf8 -*
from socket import *
HOST ='localhost'
PORT = 21568
BUFSIZE = 1024
ADDR =(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
print 'enter x exit'
while True:
	data = raw_input('>')
	if data == 'x':
		break
	if not data:
		print 'not data'
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZE)
	if not data:
		break
	print data

tcpCliSock.close()