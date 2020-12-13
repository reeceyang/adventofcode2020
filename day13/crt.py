#https://brilliant.org/wiki/chinese-remainder-theorem/

buses = input().split(",")
ids = []
incr = 0
N = 1
for bus in buses:
    if not bus == "x":
        ids.append((int(bus), int(bus) - incr)) # t cong to -1 mod bus id
        print((int(bus), int(bus) - incr))
        N *= int(bus)
    incr += 1
print(N)
x = 0
for id in ids:
    y = int(N / id[0])
    z = pow(y, id[0] - 2, id[0])
    x += y * z * (id[1] % id[0])

print(x % N)
