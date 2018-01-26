class Cipher(object):
    def __init__(self, cipher):
        self.cipher = cipher 

    def encode(self, s):
        characters = list(s.upper())
        result = ''
        for c in characters:
            result = result + chr(ord(c) + self.cipher)

        return result
