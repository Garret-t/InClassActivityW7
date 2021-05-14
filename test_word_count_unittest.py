import unittest
from word_count import word_count as wc

class TestWordCount(unittest.TestCase):
    #Check standard use with 1 word
    def test_correct(self):
        self.assertEqual(wc("Hello!"), 1)
    #Check for valid input with 2, 3, and 4 words
    def test_correct_multi(self):
        self.assertEqual(wc("Hello world!"), 2)
        self.assertEqual(wc("Hello nice world!"), 3)
        self.assertEqual(wc("Hello nice, wonderful world!"), 4)
    #Check sentence of length 0
    def test_no_words(self):
        self.assertEqual(wc(""), 0)
    #Check sentence of only space
    def test_space(self):
        self.assertEqual(wc("    "), 0)
    #Check if integers are allowed
    def test_int(self):
        self.assertEqual(wc(123), None)
        

if __name__ == "__main__":
    unittest.main()