line = input()

code = []
visited = []
while line != "":
    tokens = line.split()
    code.append((tokens[0], int(tokens[1])))
    visited.append(False)
    line = input()

for i in range(0, len(code)):
    if code[i][0] == "nop":
        code[i] = ("jmp", code[i][1])
    elif code[i][0] == "jmp":
        code[i] = ("nop", code[i][1])
    else:
        continue
    acc = 0
    index = 0
    visitedTemp = list(visited)
    while not visitedTemp[index]: # not visited before
        visitedTemp[index] = True
        if code[index][0] == "nop":
            index += 1
            continue
        elif code[index][0] == "acc":
            acc += code[index][1]
            index += 1
            continue
        else:
            index += code[index][1]
        if index >= len(code): # we reached the end, and we're done now
            print(acc)
            quit()
    if code[i][0] == "nop":
        code[i] = ("jmp", code[i][1])
    elif code[i][0] == "jmp":
        code[i] = ("nop", code[i][1])
