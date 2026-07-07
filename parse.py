from capture import sniffing
from dataclasses import dataclass
from datetime import datetime
from scapy.all import *

@dataclass
class Packet:
	src_ip: str
	dst_ip: str
	src_port: int
	dst_port: int 
	protocol: str 
	size: int 
	timestamp: datetime

def PacketInfo():
	for packet,addr in sniffing():
		#print(f'count:{indexx}\n packet -> {packet} \naddress -> {addr}')
		pac = IP(packet)
		time_Arr = time.time()

		src_ip = pac[IP].src
		dst_ip = pac[IP].dst

		if pac.haslayer(TCP):
			protocol = "TCP"
			src_port = pac[TCP].sport 
			dst_port = pac[TCP].dport 
		elif pac.haslayer(UDP):
			protocol = "UDP"
			src_port = pac[UDP].sport 
			dst_port = pac[UDP].dport 

		size = len(packet) 

		packetInfo = Packet(src_ip,dst_ip,src_port,dst_port,protocol,size,time_Arr)

		yield packetInfo

'''
for item in PacketInfo():
	print(item)
'''
