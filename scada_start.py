#File: scada_start.py 
import socket 
client_socket  = 
socket.socket(socket.AF_INET,sock
et.SOCK_STREAM) 
client_socket.connect(('169.254.2
13.2', 502)) 
client_socket.send("49\x85\x00\x0
0\x00\x08\x 
00\x0f\x00\x63\x00\x01\x01\x01") 
# queryfor starting the mixing process
