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
        while lp < rp: # should this be < or <= ??
            # get next free mem:

            while lp <= rp and not(disk[lp][0] == -1 and disk[lp][1] > 0):
                for i in range(disk[lp][1]) : new_disk.append(disk[lp][0])
                lp +=1
            while rp >= lp and not(disk[rp][0] >=0 and disk[rp][1] > 0):
                rp -=1
            [lval, lcnt] = disk[lp]
            [rval, rcnt] = disk[rp]

            if rcnt <= lcnt:
                for i in range(rcnt) : new_disk.append(rval)
                disk[lp][1] -= rcnt
                rp -= 1
            else:
                for i in range(lcnt) : new_disk.append(rval)
                disk[rp][1] -= lcnt
                lp += 1


# last one
[rval, rcnt] = disk[rp]
for i in range(rcnt) : new_disk.append(rval)


cs = get_checksum(new_disk)
print(f"{cs=}")
