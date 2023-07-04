import unittest
from translator import englishToFrench, frenchToEnglish

class TestmyTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test2(self):
        self.assertNotEqual(englishToFrench('Goodbye'), 'Bonjour')
    def test3(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test4(self):
        self.assertNotEqual(frenchToEnglish('Au revoir'), 'Hello')
        
if __name__=='__main__':
    unittest.main()