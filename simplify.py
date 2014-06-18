def Line(line):
    newLine = ""

    isString = False
    for i in range(0, len(line)):
        c = line[i]

        # check if we are in an string
        if c == "'":
            isString = not isString

        # remove spaces if we aren't in a string
        if c != " " or isString:
            newLine += line[i]

    # remove line breaks
    if newLine[-1:] == "\n":
        newLine = newLine[:-1]
        
    return newLine

def Lines(lines):
    for i in range(0, len(lines)):
        lines[i] = Line(lines[i])
