
# -*- coding: utf-8 -*-
'test TCP server'
from socket import *
from time import ctime
import select
import sys
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
input = [tcpSerSock, sys.stdin]   #input是一个列表，初始有欢迎套接字以及标准输入
while True:
  print 'waiting for connection...'
  tcpCliSock, addr = tcpSerSock.accept()
  print '...connected from:',addr
  input.append(tcpCliSock)  #将服务套接字加入到input列表中
  while True:
    readyInput,readyOutput,readyException = select.select(input,[],[]) #从input中选择，轮流处理client的请求连接（tcpSerSock），client发送来的消息(tcpCliSock)，及服务器端的发送消息(stdin)
    for indata in readyInput:
      if indata==tcpCliSock:  #处理client发送来的消息
        data = tcpCliSock.recv(BUFSIZ)
        print data
        if data=='88':
          input.remove(tcpCliSock)
          break
      else:       #处理服务器端的发送消息
        data = raw_input('>')
        if data=='88':
          tcpCliSock.send('%s' %(data))
          input.remove(tcpCliSock)
          break
        tcpCliSock.send('[%s] %s' %(ctime(), data))
    if data=='88':
      break
  tcpCliSock.close()
tcpSerSock.close()

