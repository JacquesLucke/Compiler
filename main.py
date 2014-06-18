import simplify, tree

def Translate(fileName):

    # load all lines from file
    file = open(fileName, "r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    # prepare lines
    simplify.Lines(lines)
    code = simplify.MakeFullSource(lines)
    print(code)
    print()
    print()
    
    tree.FindBlocks(code)

Translate("test.code");
