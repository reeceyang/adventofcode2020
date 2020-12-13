# see crt.py for the actual solution to part 2
input()

buses = input().split(",")
ids = []
incr = 0
for bus in buses:
    if not bus == "x":
        ids.append((int(bus), incr))
    incr += 1

t = 0
while True:
    works = True
    for id in ids:
        if not (t + id[1]) % id[0] == 0:
            works = False
            break
    if works:
        print(t)
        break
    t += ids[0][0] # make it go faster
