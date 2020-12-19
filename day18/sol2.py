def evaluate(expr, start):
    current = 0
    add = True
    c = start
    while c < len(expr):
        if expr[c] == " ":
            c += 1
            continue
        #print(c, expr[c], current)
        if expr[c] == "*":
            result = evaluate(expr, c + 1)
            current *= result[0]
            c = result[1]
            return(current, c)
            #print(c, expr[c], current)
        elif expr[c] == "+":
            c += 1
            continue
        elif expr[c] == "(":
            result = evaluate(expr, c + 1)
            current += result[0]
            c = result[1]
        elif expr[c] == ")":
            # result = evaluate(expr, c + 1)
            # return (current + result[0], result[1])
            return (current, c + 1)
        else:
            current += int(expr[c])
            c += 1
            #print(c, expr[c], current)
    return (current, c + 1)


line = input()

sum = 0

while line != "":
    sum += evaluate(line, 0)[0]
    line = input()

print(sum)
