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

def sniffing():

	HOST = getLocalip()

	sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
	sniff.bind((HOST, 0))

	#these two are for some windows permision thing

	sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


	try:
		while True:
			yield sniff.recvfrom(65565)

	except KeyboardInterrupt:
		print("you pressed the ctrl + c it stopped")

	finally:
		#idk turning off this even work
		#this is to turn off that permission
		sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


#this is to test if this works
#for indexx,(packet,addr) in enumerate(sniffing()):
#	print(f'count -> {indexx} \npacket -> {packet} \naddress -> {addr}')