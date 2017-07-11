########################################################################
################           Talking to Networks        ##################
########################################################################

#   A network socket is like a phone call between computers through a Network
#   A port is like a phone extension
#   Client initiates the connection, Server (Host) replies
#   Domain name IP address is equivalent to the phone number
#   Port 80 is typically used.

#   Common TCP Ports
#   23 - Telnet Logic
#   22 - SSH Secure Login
#   80 - http
#   443 - https (Secure)
#   53 - DNS Domain name
#   25 - SMTP (Mail)
#   21 - FTP - File Transfer

#   Socket Library
import socket
# #   Start socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #   connect to a server
mysock.connect(('data.pr4e.org',80))   # connect(host,port)
#
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
mysock.send(cmd)

########################################################################
################          Write a Web Browser        ##############d####
########################################################################

#  What do we say?  .....  http
#  URL = http://www.host.com/document.htm

#  Getting Data from the Server:
#  Doing this by hand you use telnet command in the command line

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


#  Making http easier with urllib
import urllib.request
with urllib.request.urlopen("http://www.py4inf.com/code/romeo.txt") as url:
    s = url.read()
#  html body
print(s.decode())

#  Everything you can do with a file you can do with a URL
