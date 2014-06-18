import simplify

def Translate(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line)
    file.close()

print(simplify.Line("hallo =  5 + 04 + 'sefs sdf s'"))

Translate("test.code");
