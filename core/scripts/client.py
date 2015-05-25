#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client.py
#  
#  Copyright 2015 EricsonWRP <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import socket
import server

class SucketClient():
	
	def __init__(self, host):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if host == "server_host":
			self.host = server.server_host
		else:
			self.host = host
		self.connection_established = False
		
	def __call__(self):
		print('Connecting host "{0:s}" to port "{1:d}"...'.format(self.host, server.server_port))
		self.client.connect((self.host, server.server_port))
		print("Connection established.")
		
	def send(self, data):
		self.client.send(data.encode())

	def accept(self):
		return self.client.accept()

	def close(self):
		self.client.close()

def main():

	host = input("Specify the host: ")
	sk = SucketClient(host)

	while not sk.connection_established:
		try:
			sk()
			sk.connection_established = True
		except Exception as e:
			print(e) 
				
		if sk.connection_established is True:
			msg = input("Input your message to the server: ")
			sk.send(msg)
			while True:
				data = sk.client.recv(server.buffer_size).decode()
				if len(data) > 0:
					print(str(data))
					break
	
	print("Connection closed.")
	sk.close()
	return 0

if __name__ == '__main__':
	main()

