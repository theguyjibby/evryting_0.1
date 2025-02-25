import socket

def get_service_version(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        
        # Send a request to elicit a response
        if port == 21:  # FTP
            request = b"VERSION\r\n"
        elif port == 22:  # SSH
            request = b"\x00\x00\x00\x07ssh-connection"
        elif port == 25:  # SMTP
            request = b"EHLO example.com\r\n"
        elif port == 53:  # DNS
            request = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
        elif port == 80:  # HTTP
            request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode('utf-8')
        elif port == 110:  # POP3
            request = b"CAPA\r\n"
        elif port == 139:  # NetBIOS
            request = b"\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        elif port == 143:  # IMAP
            request = b"CAPABILITY\r\n"
        elif port == 443:  # HTTPS
            request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode('utf-8')
        elif port == 445:  # SMB
            request = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        else:
            request = b"\x00\x00\x00\x07"
        
        sock.sendall(request)
        
        # Receive the response
        response = sock.recv(1024).decode('utf-8')
        
        # Try to extract version information from the response
        if port == 21:  # FTP
            for line in response.splitlines():
                if "Version" in line:
                    return line.split(":")[1].strip()
        elif port == 22:  # SSH
            return response.split()[0]
        elif port == 25:  # SMTP
            for line in response.splitlines():
                if "SMTP" in line:
                    return line.split()[1]
        elif port == 53:  # DNS
            return response.split()[0]
        elif port == 80:  # HTTP
            for line in response.splitlines():
                if "Server:" in line:
                    return line.split(":")[1].strip()
        elif port == 110:  # POP3
            for line in response.splitlines():
                if "POP3" in line:
                    return line.split()[1]
        elif port == 139:  # NetBIOS
            return response.split()[0]
        elif port == 143:  # IMAP
            for line in response.splitlines():
                if "IMAP" in line:
                    return line.split()[1]
        elif port == 443:  # HTTPS
            for line in response.splitlines():
                if "Server:" in line:
                    return line.split(":")[1].strip()
        elif port == 445:  # SMB
            return response.split()[0]
        
        
    except Exception as e:
        
        pass


