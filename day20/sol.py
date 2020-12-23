edges = {}

new_tile = True
while True:
    line = input()
    if line == "":
        if new_tile == True:
            break
        else:
            new_tile = True
            continue
    else:
        new_tile = False
    id = line.split()[1].strip(":")
    up = input()
    left = up[0]
    right = up[-1]
    for i in range(8):
        line = input()
        left += line[0]
        right += line[-1]
    down = input()
    left += down[0]
    right += down[-1]
    #print(up, right, down, left)
    if up in edges:
        edges[up].append(id)
    elif up[::-1] in edges:
        edges[up[::-1]].append(id)
    else:
        edges[up] = [id]

    if right in edges:
        edges[right].append(id)
    elif right[::-1] in edges:
        edges[right[::-1]].append(id)
    else:
        edges[right] = [id]

    if down in edges:
        edges[down].append(id)
    elif down[::-1] in edges:
        edges[down[::-1]].append(id)
    else:
        edges[down] = [id]

    if left in edges:
        edges[left].append(id)
    elif left[::-1] in edges:
        edges[left[::-1]].append(id)
    else:
        edges[left] = [id]

#print(edges)

appearances = {} # track which ids are singular in the edges
for edge in edges.values():
    if len(edge) == 1:
        if edge[0] in appearances:
            appearances[edge[0]] += 1
        else:
            appearances[edge[0]] = 1

#print(appearances)

product = 1
for id in appearances:
    if appearances[id] == 2:
        product *= int(id)

print(product)
