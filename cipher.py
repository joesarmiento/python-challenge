class Cipher(object):
    def __init__(self, cipherValue):
        self.cipherValue = cipherValue

    def cipher(self, c):
        asciiValue = ord(c)
        if asciiValue >= 65 and asciiValue <= 90:
            return chr(asciiValue + self.cipherValue)
        else:
            return c

    def encode(self, s):
        characters = list(s.upper())
        return ''.join(map(self.cipher, characters))
