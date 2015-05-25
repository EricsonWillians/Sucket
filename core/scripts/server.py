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
 
import threading
import time
import socket
import platform

server_host = platform.node()
server_port = 8888
buffer_size = 4096

class SucketServer(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((server_host, server_port))
	
	def listen(self, number_of_connections):
		print("Listening...")
		self.server.listen(number_of_connections)
		
	def accept(self):
		return self.server.accept()
		
	def run(self):
		
	#	print("Connection established with {0:s}".format(str(address)))
	
		while True:
				connection, address = self.accept()
				data = connection.recv(buffer_size).decode()
				if len(data) > 0:
					connection.send(str('You, client, said "{0:s}".'.format(data) + "\n" + "And I answer: I'm fucking fine!\n").encode())	
				elif data == '':
					break
						
def main():

	sk = SucketServer()
	
	number_of_connections = int(input("How many connections do you want to listen to?\n"))
	sk.listen(number_of_connections)
	
	sk.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print("Connection closed.")
		sk.server.close()
		sk.running = False 
		
	return 0

if __name__ == '__main__':
	main()

