def evaluate(expr, start):
    current = 0
    add = True
    c = start
    while c < len(expr):
        #print(expr[c], current)
        if expr[c] == " ":
            c += 1
            continue
        if expr[c] == "*":
            add = False
            c += 1
        elif expr[c] == "+":
            add = True
            c += 1
        elif expr[c] == "(":
            result = evaluate(expr, c + 1)
            if add:
                current += result[0]
            else:
                current *= result[0]
            c = result[1]
        elif expr[c] == ")":
            return (current, c + 1)
        else:
            if add:
                current += int(expr[c])
            else:
                current *= int(expr[c])
            c += 1
    return (current, c + 1)


line = input()

sum = 0

while line != "":
    sum += evaluate(line, 0)[0]
    line = input()

print(sum)
