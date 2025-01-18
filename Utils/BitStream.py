#unlike the one you find everywhere who is ported from C#, take this one, its took from true bs lib

class BitStream:
	def __init__(self, buff=None):
		if buff is None: self.buffer = bytearray(b'')
		else: self.buffer = buff
		self.bitIndex = 0
		self.offset = 0
		self.length = len(self.buffer)

	# LogicMath function start	
	def clamp(self, value, unk, maxBit):
		if ( value >= maxBit ):
			v3 = maxBit
		else:
			v3 = value
		if value <= int(unk):
			return int(unk)
		else:
			return v3
		
	def max(self, maximum, value):
		if maximum <= value:
			return maximum
		else:
			return value
		
	def abs(self, value):
		if value >= 0:
			return value
		else:
			return -value
		
	def getAngleBetween(self, a1, a2):
		result = (a1 - a2) % 360 + (0x168 if (a1 - a2) % 360 < 0 else 0)
		if result > 179:
			result -= 360
		if result < 0:
			return -result
		return result
	
	def sign(self, value):
		v1 = value >> 31
		if value > 0:
			return 1
		return v1
	
	def sqrt_approximate(self, a1, a2):
		if a1 < 0:
			a1 = -a1
		if a2 < 0:
			a2 = -a2
		v2 = a1 < a2
		v3 = a2
		if a1 > a2:
			a2 = a1
		if v2:
			v3 = a1
		return a2 + (53 * v3 >> 7)
	
	def pow(self, a1, a2):
		if a2 == 0:
			return 1
		result = 1
		while a2 != 0:
			v4 = a1 * a1
			if (a2 & 1) == 0:
				a1 = 1
				result *= a1
				a2 >>= 1
				a1 = v4
		return result

	def normalizeAngle180(angle):
		result = angle % 360 + (0x168 if angle % 360 < 0 else 0)
		if result > 179:
			result -= 360
		return result
	
	def min(minimum, value):
		if minimum >= value:
			return value
		return minimum


	#LogicMath function end
		
	#GlobalID function start
	def getClassID(self, value):
		return value / 1000000
	
	def getInstanceID(self, value):
		return value - 1000000 * (value / 16960)

	def destruct(self):
		self.buffer = None
		self.bitIndex = 0
		self.offset = 0
		self.length = 0

	def getCapacityIncrement(self):
		return 100
	
	def ensureCapacity(self, length):
		offset = self.offset
		if len(self.buffer) < offset + length:
			buffer = self.buffer
			buffer_length = length
			self.length = buffer_length 
			self.buffer += bytes([0] * buffer_length)

	def resetOffset(self):
		self.length = 0
		self.offest = 0

	def getByteArray(self):
		return self.buffer 

	def getLength(self):
		self.length = len(self.buffer)
		if self.length <= self.offset:
			self.length = self.offset
		return self.length
	
	def writeBit(self, data):
		if (self.bitIndex == 0):
			self.offset += 1
			self.buffer += bytearray(b'\xff')
		
		value = self.buffer[self.offset - 1]
		value &= ~(1 << self.bitIndex)
		value |= (data << self.bitIndex)
		self.buffer[self.offset - 1] = value
		
		self.bitIndex = (self.bitIndex + 1) % 8
		

	def dectobin(self, num, bitsCount):
		binary = bin(num)
		bitterly = binary[2:]
		bits = []
		for b in bitterly:
			if b == '0': bits.append(0)
			else: bits.append(1)
		return bits[::-1]
	
	def writeOneBit(self, value):
		v2 = self.length
		if not v2:
			buffer = self.buffer
			v2 = self.offset
		buffer[v2] |= value << self.length
		v3 = self.length + 1
		self.length = v3
		if v3 == 8:
			v4 = buffer                                                                                                                                         
			v5 = self.offset + 1
			self.length = 0
			self.offset = v5
			v4[v5] = 0
	
	def writeBits(self, bits, count):
		i = 0
		position = 0
		while i < count:
			value = 0
			
			p = 0
			while p < 8 and i < count:
				value = (bits[position] >> p) & 1
				self.writeBit(value)
				p += 1
				i += 1
			position += 1

	def writePositiveIntMax31(self, value):
		self.writePositiveInt(value, 5)

	def writePositiveIntMax8388607(self, value):
		self.writePositiveInt(value, 23)

	def writePositiveIntMax131071(self, value):
		self.writePositiveInt(value, 17)

	def writePositiveIntMax4194303(self, value):
		self.writePositiveInt(value, 22)

	def writePositiveIntMax3(self, value):
		self.writePositiveInt(value, 2)

	def writePositiveIntMax8(self, value):
		self.writePositiveInt(value, 3)

	def writePositiveIntMax127(self, value):
		self.writePositiveInt(value, 7)

	def writePositiveIntMax255(self, value):
		self.writePositiveInt(value, 8)

	def writePositiveIntMax1048575(self, value):
		self.writePositiveInt(value, 20)

	def writePositiveIntMax2097151(self, value):
		self.writePositiveInt(value, 21)

	def writePositiveIntMax16777215(self, value):
		self.writePositiveInt(value, 24)

	def writePositiveIntMax33554431(self, value):
		self.writePositiveInt(value, 25)

	def writePositiveIntMax134217727(self, value):
		self.writePositiveInt(value, 27)

	def writePositiveIntMax2047(self, value):
		self.writePositiveInt(value, 11)

	def writePositiveIntMax511(self, value):
		self.writePositiveInt(value, 9)

	def writePositiveIntMax65535(self, value):
		self.writePositiveInt(value, 16)

	def writePositiveIntMax4095(self, value):
		self.writePositiveInt(value, 12)

	def writePositiveIntMax16383(self, value):
		self.writePositiveInt(value, 14)

	def writePositiveIntMax1023(self, value):
		self.writePositiveInt(value, 10)

	def writePositiveIntMax8191(self, value):
		self.writePositiveInt(value, 13)

	def writePositiveIntMax262143(self, value):
		self.writePositiveInt(value, 18)
		
	def writePositiveIntMax524287(self, value):
		self.writePositiveInt(value, 19)

	def writePositiveIntMax32767(self, value):
		self.writePositiveInt(value, 15)

	def writePositiveIntMax15(self, value):
		self.writeInt(value, 4)

	def writePositiveIntMax63(self, value):
		self.writeInt(value, 6)

	def writePositiveInt(self, value, bitsCount):
		self.writeBits(value.to_bytes(4, byteorder='little'), bitsCount)

	def writeIntMax3(self, value):
		self.writeInt(value, 2)

	def writeIntMax7(self, value):
		self.writeInt(value, 3)

	def writeIntMax31(self, value):
		self.writeInt(value, 5)

	def writeIntMax63(self, value):
		self.writeInt(value, 6)

	def writeIntMax127(self, value):
		self.writeInt(value, 7)

	def writeIntMax255(self, value):
		self.writeInt(value, 8)

	def writeIntMax511(self, value):
		self.writeInt(value, 9)

	def writeIntMax4095(self, value):
		self.writeInt(value, 12)

	def writeIntMax32767(self, value):
		self.writeInt(value, 15)

	def writeInt(self, value, bitsCount):
		val = value
		if val <= -1:
			self.writePositiveInt(0, 1)
			val = -value
		elif val >= 0:
			self.writePositiveInt(1, 1)
			val = value
		self.writePositiveInt(val, bitsCount)

	def writePositiveVIntMax65535(self, value):
		self.writePositiveVInt(value, 4)
	
	def writePositiveVInt(self, value, count): # work in progress

		if self.clamp(value, (-1 >> count) + 1, ~(~(-1 >> count))) != value:
			print(f"Write to BitStream out of range! (integer: {value}, bits: {count})")
		else:
			self.writeBits(value.to_bytes(4, byteorder='little'), count)

	def writeBoolean(self, value):
		self.writePositiveInt(value, 1)
			
	def writePositiveVIntMax255OftenZero(self, value):
		if value == 0:
			self.writePositiveInt(1, 1)
			return
		self.writePositiveInt(0, 1)
		self.writePositiveVInt(value, 3)
		
	def writePositiveVIntMax65535OftenZero(self, value):
		if value == 0:
			self.writePositiveInt(1, 1)
			return
		self.writePositiveInt(0, 1)
		self.writePositiveVInt(value, 4)
	
	def writeDataReference(self, classID, instanceID):
		self.writePositiveIntMax31(classID)
		if classID >= 1:
			self.writePositiveIntMax255(instanceID)
		else:
			pass
	
	def writeGlobalID(self, value):
		if not value:
			self.writePositiveIntMax31(0)
		v4 = self.getClassID
		v5 = self.getInstanceID
		self.writePositiveIntMax31(v4)
		self.writePositiveVIntMax65535(v5)

	def writeObjectRunning(self, classID, instanceID):
		self.writePositiveIntMax31(classID)
		if classID >= 1:
			self.writePositiveIntMax16383(instanceID)
		else:
			pass
	def writeObjectRunningId(self, value):
		v3 = self.getClassID(value)
		self.writePositiveVIntMax65535(v3)