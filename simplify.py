from util import ReplaceIndex

def Line(line):
    # find expression end, block starts, block ends; remove whitespaces and tabs
    isString = False
    stringChar = "";
    i = 0
    while i < len(line):
        if line[i] == stringChar:
            isString = False
            stringChar = "";
        elif line[i] == "'" and stringChar == "":
            isString = True
            stringChar = "'"
        elif line[i] == '"' and stringChar == "":
            isString = True
            stringChar = '"'
            
        if not isString:
            if line[i] == chr(32): # white space
                line = line[:i] + line[(i+1):]
                i -= 1
            elif line[i] == chr(9): # tab
                line = line[:i] + line[(i+1):]
                i -= 1         
            elif line[i] == "{":
                line = ReplaceIndex(line, "_BS_", i) # for "Block Start"         
            elif line[i] == "}":
                line = ReplaceIndex(line, "_BE_", i) # for "Block End"
        i += 1

    # remove line breaks
    if line[-1:] == "\n":
        line = line[:-1]
    return line

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
