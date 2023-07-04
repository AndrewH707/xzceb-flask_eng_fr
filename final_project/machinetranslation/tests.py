import unittest
from translator import english_to_french, french_to_english

class TestmyTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test2(self):
        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')
    def test3(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test4(self):
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')
        
if __name__=='__main__':
    unittest.main()