"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket

# Get from: "$ bt-device -l"
serverMACAddress = 'D4:0B:1A:01:C6:20'  # host bluetooth device address
# serverMACAddress = '4c:DD:31:7'  # host bluetooth device address
port = 3  # this must match to server.py
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    # print 'AA'
# import pdb; pdb.set_trace()
# s.send('AABB')
    # print s.recv(10)
    text = raw_input()
    if text == "quit":
        break
    print [1]
    s.send(text)
    print [text]
    print [2]
s.close()



# from bluetooth import *

# # Create the client socket
# client_socket=BluetoothSocket( RFCOMM )

# client_socket.connect(("D4:0B:1A:01:C6:20", 4))

# client_socket.send("Hello World")

# print "Finished"

# client_socket.close()