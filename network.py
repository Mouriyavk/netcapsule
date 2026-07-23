import socket

def getLocalip():

	temp_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

	try:
		temp_soc.connect(("1.1.1.1", 80))
		local_ip = temp_soc.getsockname()[0]

		print(f'Using this LocalIP --> {local_ip}')

	except Exception:
		local_ip = "127.0.0.1"
		print(f'using the the loopback as local ip --> {local_ip}')
	finally:
		temp_soc.close()

	return local_ip


#for now this is for /24 because ukkk i am dumb 
def getGateway(local_ip):

	ip_part = local_ip.split(".")
	ip_part[3] = "1"

	gateway = ".".join(ip_part)
	return gateway




