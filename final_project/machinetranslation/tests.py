import unittest
from translator import englishToFrench, frenchToEnglish

class TestmyTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test2(self):
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
    def test3(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    def test4(self):
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
        
if __name__=='__main__':
    unittest.main()