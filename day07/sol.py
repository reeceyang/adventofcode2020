line = input()

counter = 1
bags = {}
bags_dp = {} #-1 can't contain, 0 don't know, 1 can contain
while line != "":
    tokens = line.split()
    color = tokens[0] + " " + tokens[1]
    current = ""
    inside = []
    bags_dp[color] = 0
    for i in range(2, len(tokens)):
        if i % 3 == 2:
            continue
        elif i % 3 == 0:
            current = tokens[i]
        else:
            current += " " + tokens[i]
            inside.append(current)
            if current == "gold shiny":
                bags_dp[color] = 1;
            current = ""
    bags[color] = inside
    line = input()

total = 0
def search(color, original): # check if color can contain shiny gold
    if bags_dp[color] == 1:
        return True
    elif bags_dp[color] == -1:
        return False
    else:
        for bag in bags[color]:
            if bag == "shiny gold" or bags_dp[bag] == 1:
                print("found shiny gold")
                bags_dp[color] = 1
                return True
        for bag in bags[color]:
            if search(color, original):
                bags_dp[color] = 1
                return True
    bags_dp[color] = -1
    return False


for color, inside in bags.items():
    if search(color, color):
        total += 1

for color, inside in bags_dp.items():
    print(inside)

print(total)
