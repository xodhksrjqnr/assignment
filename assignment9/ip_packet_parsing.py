import os
import socket
import argparse
import struct

ETH_P_ALL = 0x0003
ETH_SIZE = 14
packetCount = 1

def dumpcode(buf):
	print("%7s"% "offset ", end='')

	for i in range(0, 16):
		print("%02x " % i, end='')

		if not (i%16-7):
			print("- ", end='')

	print("")

	for i in range(0, len(buf)):
		if not i%16:
			print("0x%04x" % i, end= ' ')

		print("%02x" % buf[i], end= ' ')

		if not (i % 16 - 7):
			print("- ", end='')

		if not (i % 16 - 15):
			print(" ")

	print("")

def make_ethernet_header(raw_data):
	ether = struct.unpack('!6B6BH', raw_data)
	return {'dst':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
		'src':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
		'ether_type':ether[12]}

def make_ip_header(raw_data, length):
	ipOptionLen = str(length - 20)
	unpackType = '!BBHHHBBH4B4B' + ipOptionLen + 'B'
	ip = struct.unpack(unpackType, raw_data)
	return {'Version' : '%d' %((ip[0] & 0xF0) >> 4),
		'Header_length' : '%d' %(ip[0] & 0x0F),
		'Type_of_service' : '%d' %ip[1],
		'Total_length' : '%d' %ip[2],
		'Identification' : '%d' %ip[3],
		'Flag' : '%d' %((ip[4] & 0xE000) >> 13),
		'Fragment_offset' : '%d' %(ip[4] & 0x1FFF),
		'TTL' : '%d' %ip[5],
		'Protocol' : '%d' %ip[6],
		'Header_checksum' : '%d' %ip[7],
		'Source' : '%d.%d.%d.%d' %ip[8:12],
		'Destination' : '%d.%d.%d.%d' %ip[12:16],
		'IP_option' : '%dbyte' %int(ipOptionLen)}

def sniffing(nic):
	global packetCount
	if os.name == 'nt':
		address_familiy = socket.AF_INET
		protocol_type = socket.IPPROTO_IP
	else:
		address_familiy = socket.AF_PACKET
		protocol_type = socket.ntohs(ETH_P_ALL)

	with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
		sniffe_sock.bind((nic, 0))

		if os.name == 'nt':
			sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

		data, _ = sniffe_sock.recvfrom(65535)
		ethernet_header = make_ethernet_header(data[:ETH_SIZE])

		if ethernet_header['ether_type'] == 2048 :
			print('<Ethernet_Header>')
			for item in ethernet_header.items():
				print('{0} : {1}'.format(item[0], item[1]))
			version = (data[ETH_SIZE] & 0xF0) >> 4
			headerLen = 4 * (data[ETH_SIZE] & 0x0F)
			ipHeader = make_ip_header(data[ETH_SIZE:headerLen+14], headerLen)
			print('\n<Ip_Header>')
			for item in ipHeader.items():
				print('{0} : {1}'.format(item[0], item[1]))
			print('\n<Raw Data>')
			dumpcode(data)
			packetCount += 1

		if os.name == 'nt':
			sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a simple packet sniffer')
	parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
	args = parser.parse_args()
	while True:
		print('[%d]Packet-------------------------------------------------' %packetCount)
		sniffing(args.i)