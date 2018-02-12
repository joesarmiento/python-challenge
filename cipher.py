class Cipher(object):
	def __init__(self, cipherValue):
		self.cipherValue = cipherValue

	def encodeCharacter(self, c):
			alphabetPosition  = ord(c) - 64
			if 1 <= alphabetPosition <= 26: 
				cipherPosition = 64 + ( ( alphabetPosition + self.cipherValue ) % 26 )
				return chr ( cipherPosition )
			else: 
				return c 

	def encode(self, s):
		result = [ self.encodeCharacter(c) for c in s.upper() ]
		return ''.join(result)
