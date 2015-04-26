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
            self.assertEquals([token for token in ShiftParser(input.read())], json.loads(output.read()))

    def test_coords(self):
        """
        Tests, if the coordinates of the tokens are correctly written
        """
        with open("testInputCoords.txt") as input, open("testInputCoords.txt.tokens.json") as output:
            shiftParser = ShiftParser(input.read())
            shiftParser.save_coords = True
            self.assertEquals([token for token in shiftParser], json.loads(output.read()))

    def test_command(self):
        """
        Simulates the use of ShiftParser in console.
        """
        import subprocess, os

        subprocess.call("python ShiftParser.py testInput.txt testInput_test_command.tokens.json")
        with open("testInput.txt.tokens.json") as input, open("testInput_test_command.tokens.json") as result:
            self.assertEquals(json.loads(input.read()), json.loads(result.read()))
        os.remove("testInput_test_command.tokens.json")

if __name__ == '__main__':
    unittest.main()