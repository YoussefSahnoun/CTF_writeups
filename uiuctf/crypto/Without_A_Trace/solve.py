import numpy as np
from Crypto.Util.number import *
from itertools import permutations
import socket
import ssl
hostname = 'without-a-trace.chal.uiuc.tf'
port = 1337
def sock_connect(hostname,port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	context = ssl.create_default_context()
	conn = context.wrap_socket(sock, server_hostname=hostname)
	conn.connect((hostname,port))
	return conn
def get_base_sum():
    	user_input = '1 \n '  
    	for i in range(5):
    		conn.sendall(user_input.encode())
    		final_output = conn.recv()
    		if i ==4:
    			base_sum=int(final_output.decode()[16:])
    		
    	return base_sum
def get_pos_part(pos):
    	user_input = '1 \n '  
    	for i in range(5):
    		if i == pos:
    			conn.sendall('2 \n'.encode())
    			output = conn.recv()
    		else:
    			conn.sendall(user_input.encode())
    			output = conn.recv()
    		if i ==4:
    			tot_sum=int(output.decode()[16:])

    		
    	return tot_sum
conn = sock_connect(hostname,port)
print(f"Connected to {hostname}:{port}")
initial_output = conn.recv()
print("Initial output from server:")
print(initial_output.decode())
base=get_base_sum()
print(base)
conn.close()
flag=b""
for i in range(5):
	print(f"connection number {i+1}")
	conn = sock_connect(hostname,port)
	print(f"Connected to {hostname}:{port}")
	initial_output = conn.recv()
	print("Initial output from server:")
	print(initial_output.decode())
	output=get_pos_part(i)
	conn.close()
	flag+=long_to_bytes(output-base)
	
print(flag)


