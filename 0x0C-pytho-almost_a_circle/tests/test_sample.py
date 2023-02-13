#!/usr/bin/python3
from __future__ import print_function
import unittest
class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertTrue(True)
    def test_False(self):
        self.assertFalse(False)
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
if __name__ == '__main__':
    unittest.main()
