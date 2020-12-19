import copy

line = input()

dim = [] # 20 x 20 x 20
initial_layer = []


while line != "":
    initial_layer.append(list(line))
    line = input()

blank_row = ["." for i in range(len(initial_layer[0]))]
blank_layer = [blank_row for i in range(len(blank_row))]
# for i in range(12):
#     initial_layer.append(list(blank + blank))

#dim.append([["." for i in range(len(initial_layer[0]))] for i in range(len(blank_row))])
dim.append(initial_layer)
#dim.append([["." for i in range(len(initial_layer[0]))] for i in range(len(blank_row))])
# for i in range(20):
#     blank_layer = []
#     for j in range(20):
#         blank_layer.append(list(blank))
#     dim.append(blank_layer)

directions = [(-1, -1, -1), (-1, -1, 0), (-1, 0, -1), (0, -1, -1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1), (-1, 0, 0), (0, -1, 0), (0, 0, -1), (-1, 0, 1), (-1, 1, 0), (0, -1, 1), (0, 1, -1), (1, -1, 0), (1, 0, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
#[list(permutations(i)) for i in list(combinations_with_replacement([-1,0,1], 3))]

def printDim():
    for layer in dim:
        print("-" * (len(dim[0]) + 2))
        for row in layer:
            print(row)

#printDim()

active = 0
depth = 1
width = len(dim[0][0])
for cycle in range(6):
    active = 0
    for layer in range(0, depth):
        for row in range(0, width):
            #print(layer, row, width)
            #print(dim[layer][row])
            dim[layer][row].insert(0, ".")
            dim[layer][row].append(".")
            #print(dim[layer][row])
        dim[layer].insert(0, ["." for i in range(width + 2)])
        dim[layer].append(["." for i in range(width + 2)])
    dim.insert(0, [["." for i in range(width + 2)] for i in range(width + 2)])
    dim.append([["." for i in range(width + 2)] for i in range(width + 2)])

    #printDim()

    new_dim = copy.deepcopy(dim)
    width = len(dim[0][0])
    depth += 2
    for layer in range(0, depth):
        for row in range(1, width):
            for cube in range(1, width):
                neighbors = 0
                for dir in directions:
                    # print(layer, row, cube)
                    # print(dir[0],dir[1],dir[2])
                    if layer + dir[0] >= 0 and layer + dir[0] < depth and row + dir[1] >= 0 and row + dir[1] < width and cube + dir[2] >= 0 and cube + dir[2] < width:
                        if dim[layer + dir[0]][row + dir[1]][cube + dir[2]] == "#":
                            # print("found neighbor with", dir[0], dir[1],dir[2])
                            neighbors += 1
                # if layer == 4 and neighbors > 0:
                #     printDim()
                #     print(layer, row, cube, "has", neighbors, "neighbors")
                if dim[layer][row][cube] == "#":
                    if not (neighbors == 2 or neighbors == 3):
                        new_dim[layer][row][cube] = "."
                    else:
                        active += 1
                else:
                    if neighbors == 3:
                        new_dim[layer][row][cube] = "#"
                        active += 1
    dim = new_dim


#printDim()


print(active)
