__author__ = 'dlgltlzed'

import sys
import json


class ShiftParser:
    line = 0
    column = 0
    position = 0
    save_coords = False
    save_position = False
    level = -1
    found_tokens = []
    types = ('left shift', 'no shift', 'right shift', 'content')

    def addToken(self, type, **kwargs):
        if type in self.types:
            kwargs['type'] = type
            self.found_tokens.append(kwargs)
        else:
            raise TypeError("Type '%s' not known" % type)

    def convert(self, input_text):
        for line in input_text.splitlines():
            if line.strip() != "":
                if self.level == -1:
                    count = 0
                    for character in line:
                        if character == " ":
                            count += 1
                        else:
                            break
                    self.level = count
                    line = line[count:]
                else:
                    maximum = self.level + 1
                    consumed = 0
                    for character in line:
                        if character == " ":
                            consumed += 1
                            if consumed == maximum:
                                break
                        else:
                            break
                    line = line[consumed:]
                    if consumed < self.level:
                        self.addToken('left shift',
                                      count=self.level - consumed)
                        self.level = consumed
                    elif consumed == self.level:
                        self.addToken('no shift')
                    else:  # consumed == self.level + 1
                        self.addToken('right shift')
                        self.level += 1
                self.addToken('content', text=line)
        return self.found_tokens


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        tokens = ShiftParser().convert(file.read())
        with open(sys.argv[1] + ".tokens.json", mode="w") as output:
            output.write(json.dumps(tokens))


