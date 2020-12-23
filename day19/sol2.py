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

rules["8"] = [["42"],["42","8"]]
rules["11"] = [["42","31"],["42","11","31"]]
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
            for i in range(len(sub_rules)):
                result = check(current, sub_rules[i])
                if result == False:
                    works = False
                    break
                elif result == "end":
                    if i < len(sub_rules) - 1: # not the last sub rule
                        works = False
                        break
                    return True
                elif result == True:
                    return True
                else:
                    current = result
                    if current == "":
                        return "end" # tbh I'm not sure why this works
            if works:
                return current
        return False

line = input()
total = 0
matches = []
while line != "":
    if check(line, "0") == True:
        total += 1
        matches.append(line)
    line = input()

print(total)
#print(matches)
