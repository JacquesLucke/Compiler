def Line(line):
    newLine = ""

    isString = False
    for i in range(0, len(line)):
        c = line[i]
        
        if c == "'":
            isString = not isString
            
        if c != " " or isString:
            newLine += line[i]
        
    return newLine
