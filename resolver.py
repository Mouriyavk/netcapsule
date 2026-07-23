import socket 
from datetime import datetime
from dataclasses import dataclass
from network import getLocalip, getGateway




@dataclass
class pktval:
    ipAddr: str
    domain: str
    port: int
    duration: datetime 
    data_usage: float 
    packet_count: int 
 
domain_cache = {}



localip = getLocalip()
gateway = getGateway(localip)



def domainName(endpoint1, endpoint2):

    if endpoint1.ip == localip or endpoint1.ip == gateway:
        if endpoint2.ip in domain_cache:
            domain = domain_cache[endpoint2.ip]
        else:
            domain = socket.gethostbyaddr(endpoint2.ip)
            domain_cache[endpoint2] = domain 
    
        return(endpoint2.ip, domain, endpoint2.port)

    else:
        
        if endpoint1.ip in domain_cache:
            domain = domain_cache[endpoint1.ip]
        else:
            domain = socket.gethostbyaddr(endpoint1.ip)
            domain_cache[endpoint1] = domain 

        return(endpoint1.ip,domain, endpoint1.port) 


def resolve(Flow):

     domainInfo = domainName(Flow.endpoint1, Flow.endpoint2)
     duration = Flow.last_seen - Flow.start_time.total_seconds() / 60

     packet_count = Flow.packet_count
     data_usage = Flow.total_bytes / 1024

     pkt = pktval(domainInfo[0],domainInfo[1], domainInfo[2], duration, data_usage, packet_count)

     return pkt































