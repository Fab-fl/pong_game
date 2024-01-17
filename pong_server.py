import socket
from _thread import *
import sys
import time

host = "10.0.0.189"
port = 5555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((host, port))
    
except socket.error as e:
    print(str(e))

socket.listen(2)
print('listening for connection')
time.sleep(9)