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

#   Start socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   connect to a server
mysock.connect('www.py4inf.com',80)   # connect(host,port)
