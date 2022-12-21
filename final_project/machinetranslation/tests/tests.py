
import unittest
import machinetranslation

from machinetranslation.translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test0(self):
        self.assertEqual(englishToFrench("one"), "Un")
        self.assertEqual(englishToFrench("two"), "Deux")
        self.assertEqual(englishToFrench(" "), " ")
        self.assertEqual(englishToFrench("hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Hi"), "Hi")
        self.assertEqual(frenchToEnglish("Deux"), "Two")
        self.assertEqual(frenchToEnglish(" "), " ")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()