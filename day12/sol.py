line = input()
x = 0
y = 0
dir = 0
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

while line != "":
    if (line[0] == "R"):
        dir = int(dir + int(line[1:])/90) % 4
    if (line[0] == "L"):
        dir = int(dir - int(line[1:])/90) % 4
    if (line[0] == "F"):
        x += directions[dir][0] * int(line[1:])
        y += directions[dir][1] * int(line[1:])
    if (line[0] == "N"):
        y += int(line[1:])
    if (line[0] == "E"):
        x += int(line[1:])
    if (line[0] == "S"):
        y -= int(line[1:])
    if (line[0] == "W"):
        x -= int(line[1:])
    line = input()

print(x, y, abs(x)+abs(y))
