# coding: utf-8
# please use blueTerm app of android for testing

import bluetooth
import time

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1  # oftentime, android app use port=1 to connect
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

# Always recive data from client
while True:
  data = client_sock.recv(1024)
  print "received [%s]" % data
  client_sock.send('Test from python server: %s' % time.time())

client_sock.close()
server_sock.close()