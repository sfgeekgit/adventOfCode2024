# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.
#from collections import defaultdict


filename = "input06.txt"  
#filename = "test06.txt"

out = 0
map = []

# in the puzzle, we know they start up ^

dir = [-1,0]

high = 0
with open(filename, "r") as file:
    for line in file:
        map.append(line[:-1])
        if '^' in line:
            j_start = line.find('^')
            i_start = high
        high += 1
wide = len(map[0])

path = [[0] * wide for _ in range(high)]
path[i_start][j_start] = 1

i = i_start
j = j_start

next = [i + dir[0], j + dir[1]]
while next[0] >= 0 and next[0] < high and next[1] >= 0 and next[1] < wide:
    if map[next[0]][next[1]] != '#':
        i = next[0]
        j = next[1]
        path[i][j] = 1
    else:
        # turn!
        if dir == [-1,0]:
            dir = [0,1]
        elif dir == [0,1]:
            dir = [1,0]
        elif dir == [1,0]:
            dir = [0,-1]
        else:
            dir = [-1,0]
    next = [i + dir[0], j + dir[1]]
    #print(path)

out = sum(sum(_) for _ in path)

print(f"{out= }")