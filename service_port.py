import socket



def get_service_name(port, protocol):
    try:
        return socket.getservbyport(port, protocol)
    except OSError:
        return 'unknown'
    
