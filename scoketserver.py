# -*- coding:utf-8 -*-
from socket import *
from time import ctime

try:
	HOST = ''
	PORT = 21568
	BUFSIZ = 1024
	ADDR =(HOST,PORT)
	tcpSerScok = socket(AF_INET,SOCK_STREAM)
	tcpSerScok.bind(ADDR)
	tcpSerScok.listen(5)

	while True:		
		print 'wating for connection...'
		tcpCliSock,addr = tcpSerScok.accept()
		print '...conneted from:',addr
		while True:
			print 'OK'
			data = tcpCliSock.recv(BUFSIZ)
			print data
			if not data:
				print 'not data'
				break
			tcpCliSock.send('[%s]%s' %(ctime(),data))
		tcpCliSock.close()
except Exception, e:
	print e
else:
	pass
finally:
	tcpSerScok.close()




