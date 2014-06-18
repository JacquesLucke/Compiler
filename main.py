def Translate(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line)
    file.close()

Translate("test.code");
