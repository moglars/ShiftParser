__author__ = 'dlgltlzed'

import sys
import json


class ShiftParser:
    line_count = 0
    column_count = 0
    position = 0
    save_coords = False
    level = -1
    found_tokens = []
    types = ('left shift', 'no shift', 'right shift', 'content')
    input_text = ""

    def __init__(self, input_text):
        self.input_text = input_text

    def __iter__(self):
        return (token for token in self.convert())

    def createToken(self, type, chars_consumed, **kwargs):
        if type in self.types:
            kwargs['type'] = type
            if self.save_coords:
                kwargs['coords'] = "%s:%s" % (self.line_count, self.column_count)
            self.column_count += chars_consumed
            return kwargs
        else:
            raise TypeError("Type '%s' not known" % type)

    def convert(self):
        self.line_count = 0
        self.column_count = 0
        self.position = 0
        self.level = -1

        for line in self.input_text.splitlines():
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
                        yield self.createToken('left shift', consumed,
                                      count=self.level - consumed)
                        self.level = consumed
                    elif consumed == self.level:
                        yield self.createToken('no shift', consumed)
                    else:  # consumed == self.level + 1
                        self.level += 1
                        yield self.createToken('right shift', consumed)
                yield self.createToken('content', len(line), text=line)
            self.line_count += 1
            self.column_count = 0


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        tokens = [token for token in ShiftParser(file.read())]
        try:
            target = sys.argv[2]
        except IndexError:
            target = sys.argv[1] + ".tokens.json"
        with open(target, mode="w") as output:
            output.write(json.dumps(tokens))
