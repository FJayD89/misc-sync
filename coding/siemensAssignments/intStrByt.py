theData = bytearray([0x54,0x68,0x69,0x73,0x20,0x69,0x73,0x20,0x61,0x20,0x74,0x65,0x73,0x74,0x2e])

def encodePayload(payload):
	# return as bytes
	headerString = "START "
	head = bytes(headerString,'ascii') #header start identifier
	length = len(payload)
	lengthBytes = int.to_bytes(length,2,'big')
	wholePacket = b"".join([head, lengthBytes, theData]) #packet to be transfered

	return wholePacket

def encodeOld(payload):
	# Little endian !!!
	a = bytes("START ", 'ascii')  # header start identifier
	b = bytes(chr(len(payload) & 0xFF),'utf-8') #data length lower
	# b = int.to_bytes(len(theData) & 0xFF)
	c = bytes(chr((len(payload) >> 8) & 0xFF), 'utf-8') # data length upper
	# payload
	wholePacket = b"".join([a, b, c, payload])  # packet to be transfered
	return wholePacket


def decodePacket(packet):
	headerString = b"START "
	totalLength = len(packet)

	if totalLength < 8:
		# head
		raise ValueError("Packet has insufficient length! (len < 8)")

	if not isinstance(packet, bytes):
		raise TypeError("Packet is not in bytes!")

	head = packet[0:6]
	if head != headerString:
		raise ValueError("Invalid header!")

	lengthData = int.from_bytes(packet[6:8], 'little')
	payloadLength = totalLength - 6 - 2 # len(head) == 6, len(lengthData) == 2
	if lengthData != payloadLength:
		raise ValueError("Length of payload does not match the length encoded!")

	payload = packet[8:]
	return payload

def decode_packet(packet):
	# Check if the packet starts with "START "
	if not packet.startswith(b"START "):
		raise ValueError("Invalid packet format: Packet must start with 'START '")

	# Check if the packet length is at least 8 bytes
	if len(packet) < 8:
		raise ValueError("Invalid packet format: Packet length is too short")

	# Extract the length bytes
	length_bytes = packet[6:8]

	# Convert the length bytes to an integer
	length = int.from_bytes(length_bytes, byteorder='big')

	# Calculate the expected length of the decoded packet
	expected_length = 8 + length

	# Check if the packet length matches the expected length
	if len(packet) != expected_length:
		raise ValueError("Invalid packet format: Packet length does not match the expected length")

	# Extract the payload
	payload = packet[8:]

	# Check if the entire payload consists of valid bytes
	if len(payload) != length:
		raise ValueError("Invalid packet format: Payload length does not match the expected length")

	return payload


wrongPacket = bytearray(b"START \x00\x01")
wrongPacket.append(65)
print("wrongPacket = ", wrongPacket)
# encoded = encodePayload(theData)
encoded =  encodePayload(theData)
print(type(encoded))
print(encoded)
decodedToBytes = decode_packet(wrongPacket)

decodedToString = decodedToBytes.decode('utf-8')
print(decodedToBytes)
print(decodedToString)



# print(encoded[0:6])
# print(type(encoded[0:2]))

# testLength = 28
# testBytes = int.to_bytes(testLength,2,'big')
# print(testLength)
# print(testBytes)
