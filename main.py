import simplify

def Translate(fileName):

    # load all lines from file
    file = open(fileName, "r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    # prepare lines
    simplify.Lines(lines)
    
    print(lines)

Translate("test.code");
