import unittest


def palindrome(word):
    
    if word == "".join(reversed(word)):
        return True
    else:
        return False

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_simple2(self):
        result = palindrome('hola')
        self.assertEqual(result, False)
    
    def test_palindrome_simple3(self):
        result = palindrome('reconocer')
        self.assertEqual(result, True)

    def test_palindrome_simple4(self):
        result = palindrome('python')
        self.assertEqual(result, False)

    def test_palindrome_simple5(self):
        result = palindrome('amor a roma')
        self.assertEqual(result, True)        

if __name__ == '__main__':
    unittest.main()