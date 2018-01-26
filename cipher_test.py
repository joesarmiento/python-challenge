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

    def test_OE_maps_to_QG(self):
        cipher = getCipher()
        result = cipher.encode('OE')
        self.assertEqual('QG', result)

    def test_e_maps_to_G(self):
        cipher = getCipher()
        result = cipher.encode('e')
        self.assertEqual('G', result)

    def test_nonascii_is_unchanged(self):
        cipher = getCipher()
        result = cipher.encode('(')
        self.assertEqual('(', result)

