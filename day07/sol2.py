line = input()

bags = {}
while line != "":
    tokens = line.split()
    color = tokens[0] + " " + tokens[1]
    current = ""
    inside = []
    number = 0
    for i in range(2, len(tokens)):
        if i % 3 == 2:
            number = int(tokens[i])
        elif i % 3 == 0:
            current = tokens[i]
        else:
            current += " " + tokens[i]
            inside.append((number, current))
            current = ""
    bags[color] = inside
    line = input()

def search(color): # bags inside of color bag
    total = 0
    if len(bags[color]) == 0:
        return 0;
    for bag in bags[color]:
        total += bag[0] * search(bag[1]) + bag[0]
    return total

print(search("shiny gold"))
