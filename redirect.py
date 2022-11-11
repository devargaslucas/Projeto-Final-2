import http.client
import sys
import socket

domain = sys.argv[1]


while True:
	try:
		conn = http.client.HTTPConnection(domain)
		conn.request("GET", "/")
		r1 = conn.getresponse()
		print(r1.status, r1.reason)
		break
	except (socket.gaierror, IndexError, ConnectionError):
		#dprint("0")
		break