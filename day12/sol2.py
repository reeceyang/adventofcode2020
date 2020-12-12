line = input()
x = 0
y = 0
wx = 10
wy = 1

while line != "":
    if line == "R90" or line == "L270":
        tempx = wx
        wx = wy
        wy = -tempx
    if line == "L90" or line == "R270":
        tempx = wx
        wx = -wy
        wy = tempx
    if line == "L180" or line == "R180":
        wx = -wx
        wy = -wy
    if line[0] == "F":
        x += wx * int(line[1:])
        y += wy * int(line[1:])
    if line[0] == "N":
        wy += int(line[1:])
    if line[0] == "E":
        wx += int(line[1:])
    if line[0] == "S":
        wy -= int(line[1:])
    if line[0] == "W":
        wx -= int(line[1:])
    line = input()

print(x, y, abs(x)+abs(y))
