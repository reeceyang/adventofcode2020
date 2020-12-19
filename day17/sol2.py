import copy

line = input()

dim = []
initial_layer = []

while line != "":
    initial_layer.append(list(line))
    line = input()

dim.append([initial_layer])

directions = [(-1, -1, -1, -1), (-1, -1, -1, 0), (-1, -1, 0, -1), (-1, 0, -1, -1), (0, -1, -1, -1), (-1, -1, -1, 1), (-1, -1, 1, -1), (-1, 1, -1, -1), (1, -1, -1, -1), (-1, -1, 0, 0), (-1, 0, -1, 0), (-1, 0, 0, -1), (0, -1, -1, 0), (0, -1, 0, -1), (0, 0, -1, -1), (-1, -1, 0, 1), (-1, -1, 1, 0), (-1, 0, -1, 1), (-1, 0, 1, -1), (-1, 1, -1, 0), (-1, 1, 0, -1), (0, -1, -1, 1), (0, -1, 1, -1), (0, 1, -1, -1), (1, -1, -1, 0), (1, -1, 0, -1), (1, 0, -1, -1), (-1, -1, 1, 1), (-1, 1, -1, 1), (-1, 1, 1, -1), (1, -1, -1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1), (-1, 0, 0, 1), (-1, 0, 1, 0), (-1, 1, 0, 0), (0, -1, 0, 1), (0, -1, 1, 0), (0, 0, -1, 1), (0, 0, 1, -1), (0, 1, -1, 0), (0, 1, 0, -1), (1, -1, 0, 0), (1, 0, -1, 0), (1, 0, 0, -1), (-1, 0, 1, 1), (-1, 1, 0, 1), (-1, 1, 1, 0), (0, -1, 1, 1), (0, 1, -1, 1), (0, 1, 1, -1), (1, -1, 0, 1), (1, -1, 1, 0), (1, 0, -1, 1), (1, 0, 1, -1), (1, 1, -1, 0), (1, 1, 0, -1), (-1, 1, 1, 1), (1, -1, 1, 1), (1, 1, -1, 1), (1, 1, 1, -1), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]


#[list(permutations(i)) for i in list(combinations_with_replacement([-1,0,1], 3))]

def printDim():
    for wlayer in dim:
        print("=====")
        for layer in wlayer:
            print("-----")
            for row in layer:
                print(row)

# printDim()
# quit()

active = 0
depth = 1
wdepth = 1
width = len(dim[0][0][0])
for cycle in range(6):
    active = 0
    for wlayer in range(0, wdepth):
        for layer in range(0, depth):
            for row in range(0, width):
                #print(layer, row, width)
                #print(dim[layer][row])
                dim[wlayer][layer][row].insert(0, ".")
                dim[wlayer][layer][row].append(".")
                # print(dim[wlayer][layer][row])
                # print("buffered row", row, "in layer", layer, "in wlayer", wlayer)
            dim[wlayer][layer].insert(0, ["." for i in range(width + 2)])
            dim[wlayer][layer].append(["." for i in range(width + 2)])
        dim[wlayer].insert(0, [["." for i in range(width + 2)] for i in range(width + 2)])
        dim[wlayer].append([["." for i in range(width + 2)] for i in range(width + 2)])
    dim.insert(0, [[["." for i in range(width + 2)] for i in range(width + 2)] for i in range(wdepth + 2)])
    dim.append([[["." for i in range(width + 2)] for i in range(width + 2)] for i in range(wdepth + 2)])

    # printDim()
    # if cycle == 1:
    #     quit()

    new_dim = copy.deepcopy(dim)
    width = len(dim[0][0][0])
    # print(width)
    depth += 2
    wdepth += 2
    for wlayer in range(0, wdepth):
        for layer in range(0, depth):
            for row in range(1, width):
                for cube in range(1, width):
                    neighbors = 0
                    for dir in directions:
                        # printDim()
                        # print(depth, width, wlayer, layer, row, cube)
                        # print(dir[0],dir[1],dir[2], dir[3])
                        if wlayer + dir[3] >= 0 and wlayer + dir[3] < wdepth and layer + dir[0] >= 0 and layer + dir[0] < depth and row + dir[1] >= 0 and row + dir[1] < width and cube + dir[2] >= 0 and cube + dir[2] < width:
                            if dim[wlayer + dir[3]][layer + dir[0]][row + dir[1]][cube + dir[2]] == "#":
                                # print("found neighbor with", dir[0], dir[1],dir[2])
                                neighbors += 1
                    # if layer == 4 and neighbors > 0:
                    #     printDim()
                    #     print(layer, row, cube, "has", neighbors, "neighbors")
                    if dim[wlayer][layer][row][cube] == "#":
                        if not (neighbors == 2 or neighbors == 3):
                            new_dim[wlayer][layer][row][cube] = "."
                        else:
                            active += 1
                    else:
                        if neighbors == 3:
                            new_dim[wlayer][layer][row][cube] = "#"
                            active += 1
    dim = new_dim


#printDim()


print(active)
