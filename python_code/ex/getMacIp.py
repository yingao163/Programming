#!/usr/bin/python

import uuid
import socket
import fcntl
import struct

def get_mac_address():
	mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
	return ":".join([mac[e:e+2] for e in range(0,11,2)])
	
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

myname = socket.getfqdn(socket.gethostname())
myipaddr = socket.gethostbyname(myname)
mymacaddr = get_mac_address()

print 'my computer name:%s' % myname
print 'my ip address:%s' % myipaddr
print 'my mac address:%s' % mymacaddr

print get_ip_address('eth0')
