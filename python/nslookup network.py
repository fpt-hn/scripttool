import socket
##############LOOKUP DOMAIN ######################################33
##############CREATE DOMAIN.TXT AND RUN SCRIPT#################################
###################### JUSTATEAM ################################################
f = open("domain.txt")
line = f.readlines()
for x in line:
	host = x.strip()
	print("%s - %s" % (host, socket.gethostbyname(host)))
f.close()