import bluetooth

bd_addr = "01:23:45:67:89:AB"  # here need to modify. use hciconfig to get address

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
