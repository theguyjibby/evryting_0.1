import socket
from datetime import datetime
import re
import sys
from ip import get_ip_address
from service_port import get_service_name
from port_version import get_service_version


#DEFINE OUR TARGET 
print('......Evryting port Scanner......')
ip_address = input('Enter IP Address or Host Name: ').strip()

if  re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}+\.[0-9]{1,3}+$', ip_address):
    print('Scanning........')
	
elif re.search(r'.+\.(com|gov|org|edu|net)$', ip_address):
	print('Retrieving Host IP Address.....')
	ip_address= get_ip_address(ip_address)
	print(f'Host IP Address:  {ip_address}')
	
	
else:
    sys.exit('invalid ip address')
    
    

#ADDING A BANNER
print ("-" * 50)
print ("scanning target "+ip_address)
print ("Time started: "+str(datetime.now()))
print ("-" * 50)

try: 
	for port in range (1,500):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((ip_address,port)) #RETURNS AN ERROR INDICATOR
		if result == 0:
			version = get_service_version(str(ip_address), port)
			if version == None:
				print ('port {} is open'.format(port), ' | ', get_service_name(port, 'tcp'or 'udp'))
			else:
				print ('port {} is open'.format(port), ' | ', get_service_name(port, 'tcp'or 'udp'),' | ' ,get_service_version(str(ip_address), port ))
			
			
		s.close()

		
except KeyboardInterrupt:
	print ('\nexiting program.')
	sys.exit()
	
except socket.gaierror: 
	print('Hostname could not be resolved.')
	sys.exit()
	
except socket.error:
	print("couldn't connect to server.")
	sys.exit()		