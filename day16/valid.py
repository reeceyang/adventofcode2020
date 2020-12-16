rules = {}

line = input()
while line != "":
    field, ranges = line.split(":")[0], line.split(":")[1].strip();
    range = (int(ranges.split(" or ")[0].split("-")[0]), int(ranges.split(" or ")[0].split("-")[1]), int(ranges.split(" or ")[1].split("-")[0]), int(ranges.split(" or ")[1].split("-")[1]))
    rules[field] = range
    line = input()

input() #your ticket:
input() #191,139,59,79,149,83,67,73,167,181,173,61,53,137,71,163,179,193,107,197
input() #
input() #nearby tickets:

line = input()
rate = 0
while line != "":
    all_valid = True
    for x in line.split(","):
        val = int(x)
        valid = False
        for ranges in rules.values():
            if (val < ranges[1] and val > ranges[0]) or (val < ranges[3] and val > ranges[2]):
                valid = True
                break
        if not valid:
            rate += val
            all_valid = False
    if all_valid:
        print(line)
    line = input()
