import unittest
from palindrome import palindrome as pal

class TestPalindrome(unittest.TestCase):
    #Test correct case for True
    def test_correct(self):
        self.assertEqual(pal("lol"), True)
    #Test correct case for False
    def test_correct2(self):
        self.assertEqual(pal("no"), False)
    #Test correct case for multiple words
    def test_multiple(self):
        self.assertEqual(pal("lol lol"), True)
    #Test correct case for digit values
    def test_digit(self):
        self.assertEqual(pal("121"), True)
    #Test invalid case for integer values
    def test_int(self):
        self.assertEqual(pal(121), None)
    #Test if single character acceptable
    def test_single(self):
        self.assertEqual(pal("l"), True)
    #Test empty string, this input should not
    #be allowed to go through
    def test_empty(self):
        self.assertEqual(pal(""), None)


if __name__ == "__main__":
    unittest.main()