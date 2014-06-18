from util import InsertAtIndex

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
            elif line[i] == ";":
                line = InsertAtIndex(line, "_EE_", i) # for "Expression End"            
            elif line[i] == "{":
                line = InsertAtIndex(line, "_BS_", i) # for "Block Start"         
            elif line[i] == "}":
                line = InsertAtIndex(line, "_BE_", i) # for "Block End"
        i += 1

    # find string starts and ends
    i = 0
    waitingFor = ""
    while i < len(line):
        if line[i] == waitingFor:
            waitingFor = ""
            line = InsertAtIndex(line, "_SE_", i) # for "String End"

        if waitingFor == "":
            if line[i] == "'":
                waitingFor = "'"
                line = InsertAtIndex(line, "_SS_", i) # for "String Start"
            if line[i] == '"':
                waitingFor = '"'
                line = InsertAtIndex(line, "_SS_", i) # for "String Start"
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
