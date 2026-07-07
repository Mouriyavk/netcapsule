from parse import PacketInfo
from dataclasses import dataclass
from datetime import datetime




@dataclass(frozen=True, order=True)
class Endpoint:
	ip: str 
	port: int 

@dataclass(frozen=True)
class FlowKey:
    endpoint1: Endpoint
    endpoint2: Endpoint
    protocol: str


@dataclass
class Flow:
	endpoint1: Endpoint
	endpoint2: Endpoint
	protocol: str 
	packet_count: int 
	start_time: datetime 
	last_seen: datetime 
	total_bytes: int 



def build_flowKey(Packet: PacketInfo):
	endpoint1 = Endpoint(Packet.src_ip,Packet.src_port)
	endpoint2 = Endpoint(Packet.dst_ip,Packet.dst_port)

	small = min(endpoint1, endpoint2)
	large = max(endpoint1, endpoint2)

	Key = FlowKey(small, large, Packet.protocol)

	return Key

flowTable = {} 
def update_flowTable(Packet: PacketInfo):

	flow_key = build_flowKey(Packet)

	if flow_key in flowTable:
		flow = flowTable[flow_key]
		flow.packet_count += 1
		flow.last_seen = Packet.timestamp
		flow.total_bytes += Packet.size 

	else:
		endpoint1 = flow_key.endpoint1
		endpoint2 = flow_key.endpoint2
		new_flow = Flow(endpoint1, endpoint2, 
				Packet.protocol,
				1,
				Packet.timestamp,
				Packet.timestamp,
				Packet.size)

		flowTable[flow_key] = new_flow


		
	
for item in PacketInfo():
	update_flowTable(item)

def PacketDisplay(dict: flowTable):
	for key, value in flowTable.items():
		print(f'key: {key}\n value: {value}')


PacketDisplay(flowTable)

