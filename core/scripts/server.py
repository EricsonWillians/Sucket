#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server.py
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

class SucketServer():
	
	def __init__(self, host, port):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port
	
	def __call__(self):
		print('Binding host "{0:s}" to port "{1:d}"...'.format(self.host, self.port))
		self.server.bind((self.host, self.port))
	
	def listen(self, number_of_connections):
		print("Listening...")
		self.server.listen(number_of_connections)
		
	def accept(self):
		return self.server.accept()
		
	def close(self):
		self.server.close()

def main():

	sk = SucketServer("localhost", 8089)
	sk()
	sk.listen(5)
	connection, address = sk.accept()
	print("Connection established with {0:s}".format(str(address)))
	while True:
		data = connection.recv(1000).decode()
		if len(data) > 0:
			connection.send(str('You, client, said "{0:s}".'.format(data) + "\n" + "And I answer: I'm fucking fine!\n").encode())
			break
	
	print("Connection closed.")
	sk.close()
	return 0

if __name__ == '__main__':
	main()

