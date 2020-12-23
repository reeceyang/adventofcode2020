rules = {}

line = input()
while line != "":
    tokens = line.split();
    if tokens[1][0] == "\"":
        rules[tokens[0].strip(":")] = tokens[1].strip("\"")
    else:
        sub_rules = []
        sub_rule = []
        for i in range(1, len(tokens)):
            if tokens[i] == "|":
                sub_rules.append(sub_rule.copy())
                sub_rule.clear()
            else:
                sub_rule.append(tokens[i])
            if i == len(tokens) - 1:
                sub_rules.append(sub_rule.copy())
        rules[tokens[0].strip(":")] = sub_rules
    line = input()

#print(rules)

def check(s, rule):
    if rules[rule] == "a":
        if s[0] == "a":
            return s[1:]
        else:
            return False
    elif rules[rule] == "b":
        if s[0] == "b":
            return s[1:]
        else:
            return False
    else:
        for sub_rules in rules[rule]:
            works = True
            current = s
            for sub_rule in sub_rules:
                result = check(current, sub_rule)
                if result == False:
                    works = False
                    break
                else:
                    current = result
                    if current == "":
                        return True
            if works:
                return current
        return False

line = input()
total = 0
while line != "":
    if check(line, "0") == True:
        total += 1
    line = input()

print(total)
