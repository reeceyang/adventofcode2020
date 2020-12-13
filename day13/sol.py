earliest = int(input())
buses = input().split(",")
#ids = []
smallest = (earliest, 0)
for bus in buses:
    if not bus == "x":
        id = int(bus)
        if id - (earliest % id) < smallest[0]:
            smallest = (id - (earliest % id), id)

print(smallest[0], smallest[1], smallest[0] * smallest[1])
