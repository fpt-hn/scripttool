import socket

s = socket.socket()
s.connect(("10.4.11.65",25))
banner = s.recv(1024)
banner = banner.strip()
print (banner)
