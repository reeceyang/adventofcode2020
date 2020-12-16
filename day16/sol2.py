import math

rules = {}
possible = {}

line = input()
while line != "":
    field, ranges = line.split(":")[0], line.split(":")[1].strip();
    ranged = (int(ranges.split(" or ")[0].split("-")[0]), int(ranges.split(" or ")[0].split("-")[1]), int(ranges.split(" or ")[1].split("-")[0]), int(ranges.split(" or ")[1].split("-")[1]))
    rules[field] = ranged
    possible[field] = []
    line = input()

input() #your ticket:
input()
mine = [191,139,59,79,149,83,67,73,167,181,173,61,53,137,71,163,179,193,107,197]
input() #
input() #nearby tickets:

line = input()
tickets = []
while line != "":
    tickets.append([int(x) for x in line.split(",")])
    line = input()

for field in rules:
    for i in range(20):
        ok = True
        for row in tickets:
            val = row[i]
            if not ((val <= rules[field][1] and val >= rules[field][0]) or (val <= rules[field][3] and val >= rules[field][2])):
                ok = False
        if ok:
            possible[field].append(i)

done = []
for i in range(20): # gradually narrow down location of each field
    for field in rules:
        if len(possible[field]) == 1 and not field in done:
            for other in rules:
                if other != field and possible[field][0] in possible[other]:
                    possible[other].remove(possible[field][0])
            done.append(field)


for i in possible:
    print(i, possible[i])

print([mine[int(x[0])] for x in possible.values()]) # just calculate the product by hand lol
