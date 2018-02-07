class Cipher(object):
	def __init__(self, cipherValue):
		self.cipherValue = cipherValue

	def encode(self, s):

		result = ''
		for c in s.upper():
			alphabetPosition  = ord(c) - 64

			cipherPosition = 64 + ( ( alphabetPosition + self.cipherValue ) % 26 )

			shiftedCharacter = chr ( cipherPosition ) 
			result = result + shiftedCharacter

		return result
