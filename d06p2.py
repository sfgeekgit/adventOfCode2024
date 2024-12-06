# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.
#from collections import defaultdict

filename = "input06.txt"  
#filename = "test06.txt"


def gen_path(i,j,dir, map, ret_path = True):
    # brute poor man's cycle detection, it works, gets correct answser for this.
    # could re-do with more proper, such as tort and hare.
    # but if you're reading this then didn't :D
    step_limit = 19999
    steps_taken = 0

    high = len(map)
    wide = len(map[0])
    path = [[0] * wide for _ in range(high)]
    path[i][j] = 1
    next = [i + dir[0], j + dir[1]]
    while next[0] >= 0 and next[0] < high and next[1] >= 0 and next[1] < wide and steps_taken<step_limit:
        steps_taken += 1
        if steps_taken >= step_limit:
            return -1
        
        if map[next[0]][next[1]] != '#':
            i = next[0]
            j = next[1]
            path[i][j] = 1
        else:
            if dir == [-1,0]:
                dir = [0,1]
            elif dir == [0,1]:
                dir = [1,0]
            elif dir == [1,0]:
                dir = [0,-1]
            else:
                dir = [-1,0]
        next = [i + dir[0], j + dir[1]]
        #print(i,j, dir)
        #print(path)


    if steps_taken >= step_limit:
        return -1

    if ret_path:
        return path
    else:
        return steps_taken


#####################

# try brute? Check every possible spot in a bruty way
# slight optimization, take original known path and check every step on it to see if it causes a cycle.
# to check for cycle, useing a dumb brute, just counting steps and stopping after steps are too big
# could do more fancy cycle detection too, maybe will revise with tort and hare or such, if I have time to fool around.

out = 0
map = []

# in the given puzzle, we know they start up ^ 
# so keeping this code simple and using that.

dir = [-1,0]

high = 0
with open(filename, "r") as file:
    for line in file:
        map.append(line[:-1])
        if '^' in line:
            j = line.find('^')
            i = high
        high += 1
wide = len(map[0])

i_start = i
j_start = j

path = gen_path(i,j,dir, map)

for i, row in enumerate(path):
    for j, val in enumerate(row):
        if val == 1:
            if map[i][j] == '.':
                mapcpy = [mr[:] for mr in map]
                foo = list(mapcpy[i])
                foo[j] = '#'
                mapcpy[i] = ''.join(foo)

                stps = gen_path(i_start,j_start,dir, mapcpy, False)
                #print(f"{stps= } {i=} {j=}")
                if stps == -1:
                    out += 1



#print(map)
print(f"{out= }")


