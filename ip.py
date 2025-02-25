import socket
import sys


def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        sys.exit('unable to resolve hostname')
    

