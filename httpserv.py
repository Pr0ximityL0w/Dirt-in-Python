import socket, SimpleHTTPServer, SocketServer, os

print "Starting Server on " + ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])

sfolder = raw_input("Full path to folder to share: ")
os.chdir(sfolder)

p = int(raw_input("Enter port number for server: "))

h = SimpleHTTPServer.SimpleHTTPRequestHandler
s = SocketServer.TCPServer(("", p), h)
s.serve_forever()

