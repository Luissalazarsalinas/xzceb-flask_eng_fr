import unittest
from translator import english_to_french, french_to_english


class TestenglishTofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "Unable to validate payload size, the 'text' is empty")
        self.assertNotEqual(english_to_french("Hello"), "Bounjour")

class TestfrenchToenglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "Unable to validate payload size, the 'text' is empty")
        self.assertNotEqual(french_to_english("Bounjour"), "Hello")

unittest.main()