line = input()

mask = ""
mem = {}
while line != "":
    tokens = line.split()
    if tokens[0] == "mask":
        mask = tokens[2]
    else:
        pow2 = 2**35
        given = bin(int(tokens[2]))[2:].zfill(36)
        new = 0
        for i in range(0, 36):
            if mask[i] == "X":
                new += int(given[i]) * pow2
            else:
                new += int(mask[i]) * pow2
            pow2 = int(pow2 / 2)
        #print("value:",given, "\n result:", bin(new)[2:].zfill(36))
        mem[tokens[0]] = new
    line = input()

#print(mem)

sum = 0
for i in mem.values():
    sum += i

print(sum)
