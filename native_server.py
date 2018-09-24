# coding: utf-8
# please use blueTerm app of android for testing

import socket
import time

# ifconfig: "$ hciconfig"
hostMACAddress = '5C:F3:70:81:1C:A0' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 1 # 1 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1  # one allow one client at once
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data + 'at %s\r\n' % time.time())
except: 
    print("Closing socket") 
    client.close()
    s.close()
