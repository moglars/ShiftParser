__author__ = 'dlgltlzed'

import sys
import json


def convert(input_text):
    level = -1
    found_tokens = []
    for line in input_text.splitlines():
        if line.strip() != "":
            if level == -1:
                count = 0
                for character in line:
                    if character == " ":
                        count += 1
                    else:
                        break
                level = count
                line = line[count:]
            else:
                maximum = level + 1
                consumed = 0
                for character in line:
                    if character == " ":
                        consumed += 1
                        if consumed == maximum:
                            break
                    else:
                        break
                line = line[consumed:]
                if consumed < level:
                    token = {
                        "type": "left shift",
                        "count": level - consumed
                    }
                    found_tokens.append(token)
                    level = consumed
                elif consumed == level:
                    token = {
                        "type": "no shift"
                    }
                    found_tokens.append(token)
                else:  # consumed == level + 1
                    token = {
                        "type": "right shift"
                    }
                    found_tokens.append(token)
                    level += 1
            token = {
                "type": "content",
                "text": line
            }
            found_tokens.append(token)
    return found_tokens


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        tokens = convert(file.read())
        with open(sys.argv[1] + ".tokens.json", mode="w") as output:
            output.write(json.dumps(tokens))


