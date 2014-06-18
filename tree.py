def FindBlocks(code):
    index = 0
    inBlock = False
    blocks = []
    ready = False

    while not ready:
        if not inBlock:
            nextStart = code.find("_BS_", index)
            if nextStart == -1:
                blocks.append(code[index:])
                ready = True
            else:
                blocks.append(code[index:nextStart])
                inBlock = True
                index = nextStart + 4
        else:
            deep = 1
            nextIndex = index
            while not deep == 0:
                nextStart = code.find("_BS_", nextIndex)
                nextEnd = code.find("_BE_", nextIndex)

                if nextStart < nextEnd and nextStart > 0:
                    deep += 1
                    nextIndex = nextStart + 4
                else:
                    deep -= 1
                    nextIndex = nextEnd + 4
            blocks.append(code[index:nextEnd])
            index = nextEnd + 4
            inBlock = False
    Write(blocks)

def Write(blocks):
    for i in range(len(blocks)):
        print(blocks[i])
        print()
