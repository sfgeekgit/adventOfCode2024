# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input09.txt"  
#filename = "test09.txt"
#filename = "test09a.txt"


def make_disk(files, frees):
    out = []
    for i, fv in enumerate(files):
        sr = str(i) * int(fv)
        sr = [i, int(fv)]
        out.append(sr)
        if i < len(frees):
            sr = [-1, int(frees[i])]
            out.append(sr)
    return out

def get_checksum(disk):
    out = 0
    for i, val in enumerate(disk):
        if val >= 1:
            out += i*val
    return out

def uncomp_disk(disk):
    new_disk = []
    for [val, cnt] in disk:
        for i in range(cnt):
            new_disk.append(val)
    return new_disk

def get_checksum_pairs(disk):
    out = 0
    i = 0
    for [val,cnt] in disk:
        if val >= 1:
            for j in range(i, i+cnt):                
                out += j*val
        i += cnt
    return out

with open(filename, "r") as file:
    for line in file:
        line = line.rstrip('\n')
        chars = []
        chars = list(line)
        # am I missing an obvious way to filter every other item? Oh well
        file_size, free_size = [], []
        for i, val in enumerate(chars):
            if i %2==0:
                file_size.append(int(val))
            else:
                free_size.append(int(val))

        # let's just re-create the simple example,
        # make a line of text, hope the real one fits in memory too?
        disk = make_disk(file_size, free_size)

        lp = 0
        rp = len(disk) -1
        new_disk = []
        while rp > 0: # should this be < or <= ??
            lp = 0


            while rp >= lp and not(disk[rp][0] >=0 and disk[rp][1] > 0):
                rp -=1
            [rval, rcnt] = disk[rp]


            while lp <= rp and not(disk[lp][0] == -1 and disk[lp][1] >= rcnt):
                lp +=1
            [lval, lcnt] = disk[lp]
            if lp < rp:
                # found lp, now copy from rp
                if lcnt == rcnt:
                    disk[lp][0] = rval
                    disk[rp][0] = -1
                elif lcnt > rcnt: # fill partial, and add new node for remaining space and rp+=1 to account for new node
                    disk[rp][0] = -1
                    disk[lp] = [-1, lcnt-rcnt]
                    new_node = [rval, rcnt]
                    # insert new node after [lp]
                    disk = disk[0:lp] + [new_node] + disk[lp:]                     
                    rp += 1 # account for new node
                #else:
                    #print(f"no space found for {rp=} {disk[rp]=} {rval=} {rcnt=}")

            rp -=1
 
'''
new_disk = uncomp_disk(disk)
print(f"{new_disk=}")
vis = ''
for val in new_disk:
    if val == -1:
        vis += '.'
    else:
        vis += str(val)
print(vis)
print("\n\n")
'''
cs = get_checksum_pairs(disk)
print(f"{cs=}")