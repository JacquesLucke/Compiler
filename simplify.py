def Line(line):
    newLine = line

    # find expression end, block starts, block ends
    isString = False
    stringChar = "";
    i = 0
    while i < len(newLine):
        if newLine[i] == stringChar:
            isString = False
            stringChar = "";
        if newLine[i] == "'" and stringChar == "":
            isString = True
            stringChar = "'"
        if newLine[i] == '"' and stringChar == "":
            isString = True
            stringChar = '"'
            
        if not isString:
            if newLine[i] == " ":
                newLine = newLine[:i] + newLine[(i+1):]
                i -= 1
            elif newLine[i] == "\t":
                newLine = newLine[:i] + newLine[(i+1):]
                i -= 1 
            elif newLine[i] == ";":
                newLine = newLine[:i] + "_EE_" + newLine[(i+1):] # for "Expression End"               
            elif newLine[i] == "{":
                 newLine = newLine[:i] + "_BS_" + newLine[(i+1):] # for "Block Start"         
            elif newLine[i] == "}":
                newLine = newLine[:i] + "_BE_" + newLine[(i+1):] # for "Block End"
            
        i += 1

    # remove line breaks
    if newLine[-1:] == "\n":
        newLine = newLine[:-1]
    return newLine

def Lines(lines):
    i = 0
    while i < len(lines):
        lines[i] = Line(lines[i])
        
        if lines[i] == "":
            del lines[i]
        else:
            i += 1

def MakeFullSource(lines):
    code = ""
    for line in lines:
        code += line
    return code
