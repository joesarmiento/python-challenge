import unittest
from cipher import Cipher

def getCipher():
    return Cipher(2)

class CipherTests(unittest.TestCase):
 
    def test_K_maps_to_M(self):
        cipher = getCipher()
        result = cipher.encode('K')
        self.assertEqual('M', result)

    def test_O_maps_to_Q(self):
        cipher = getCipher()
        result = cipher.encode('O')
        self.assertEqual('Q', result)

    def test_E_maps_to_G(self):
        cipher = getCipher()
        result = cipher.encode('E')
        self.assertEqual('G', result)

    def test_Z_maps_to_B(self):
        cipher = getCipher()
        result = cipher.encode('Z')
        self.assertEqual('B', result)

    def test_Y_maps_to_A(self):
        cipher = getCipher()
        result = cipher.encode('Y')
        self.assertEqual('A', result)

    def test_OE_maps_to_QG(self):
        cipher = getCipher()
        result = cipher.encode('OE')
        self.assertEqual('QG', result)

    def test_e_maps_to_G(self):
        cipher = getCipher()
        result = cipher.encode('e')
        self.assertEqual('G', result)

    def test_Y_maps_to_B_when_cipher_is_3(self):
	cipher = Cipher(3)
        result = cipher.encode('Y')
        self.assertEqual('B', result)

    def test_nonascii_is_unchanged(self):
        cipher = getCipher()
        result = cipher.encode('(')
        self.assertEqual('(', result)

    def test_challenge_text_block(self):
        cipher = getCipher()
        result = cipher.encode('map')
        self.assertEqual('OCR', result)

