def search(address, j):
    all = []
    no_x = True
    for i in range(j, 36):
        if address[i] == "X":
            no_x = False
            all = all + search(address[:i] + "1" + address[i + 1:], i) + search(address[:i] + "0" + address[i + 1:], i)
            break #optimize
    if no_x:
        all.append(address)
    return all

line = input()

mask = ""
mem = {}
while line != "":
    tokens = line.split()
    if tokens[0] == "mask":
        mask = tokens[2]
    else:
        given = bin(int(tokens[0][4:-1]))[2:].zfill(36)
        address = given
        for i in range(0, 36):
            if mask[i] == "X":
                address = address[:i] + "X" + address[i + 1:]
            elif mask[i] == "1":
                address = address[:i] + "1" + address[i + 1:]
        print("\naddress:", given,"\nmask:",mask,"\n result:", address)
        for a in search(address, 0):
            mem[a] = int(tokens[2])
    line = input()

print(mem)

sum = 0
for i in mem.values():
    sum += i

print(sum)
