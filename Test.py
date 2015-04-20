__author__ = 'dlgltlzed'

import unittest
from ShiftParser import ShiftParser
import json

class TestMethods(unittest.TestCase):

    def test_main(self):
        with open("testInput.txt") as input, open("testInput.txt.tokens.json") as output:
            self.assertEquals(ShiftParser().convert(input.read()), json.loads(output.read()))

if __name__ == '__main__':
    unittest.main()