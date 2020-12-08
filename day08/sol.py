line = input()

code = []
visited = []
while line != "":
    tokens = line.split()
    code.append((tokens[0], int(tokens[1])))
    visited.append(False)
    line = input()

acc = 0
index = 0
while not visited[index]: # not visited before
    visited[index] = True
    if code[index][0] == "nop":
        index += 1
        continue
    elif code[index][0] == "acc":
        acc += code[index][1]
        index += 1
        continue
    else:
        index += code[index][1]


print(acc)
