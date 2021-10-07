import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_upper_fail(self):
        self.assertEqual('foo', 'foo')

if __name__ == '__main__':
    unittest.main()