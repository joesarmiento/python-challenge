class Cipher(object):
    def __init__(self, cipherValue):
        self.cipherValue = cipherValue

    def encode(self, s):
	shiftedCharacter = chr ( ord(s) + 2) 
        return shiftedCharacter 
