__author__ = 'dlgltlzed'

import unittest
from ShiftParser import ShiftParser
import json

class TestMethods(unittest.TestCase):

    def test_main(self):
        """
        Creates tokens from an input
        """
        with open("testInput.txt") as input, open("testInput.txt.tokens.json") as output:
            self.assertEquals(ShiftParser().convert(input.read()), json.loads(output.read()))

    def test_coords(self):
        """
        Tests, if the coordinates of the tokens are correctly written
        """
        with open("testInputCoords.txt") as input, open("testInputCoords.txt.tokens.json") as output:
            shiftParser = ShiftParser()
            shiftParser.save_coords = True
            self.assertEquals(shiftParser.convert(input.read()), json.loads(output.read()))

if __name__ == '__main__':
    unittest.main()