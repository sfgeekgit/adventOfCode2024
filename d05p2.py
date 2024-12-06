# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.
from collections import defaultdict


filename = "input05.txt"  
#filename = "test05.txt"

out = 0

must_after = defaultdict(list)
must_before = defaultdict(list)

lines = []

reading_rules = True
with open(filename, "r") as file:
    for line in file:
        line = line[:-1]
        if line == '':
            print("Blank line!")
            reading_rules = False

        else:
            if reading_rules:
                [before,after] = line.split("|")
                must_after[after].append(before)
                must_before[before].append(after)
            else:
                ins = line.split(',')
                if len(ins) ==0:
                    print("nope")
                    quit()
                past = []
                need_fix = False
                for p in ins:
                    for seen in past:
                        if p in must_after[seen]:
                            #print(f"wrong order {line=} {ins=} {p=} {past=} {seen=} {must_after[seen]=} ")
                            need_fix = True
                            break
                        
                    past.append(p)

                if need_fix:
                    local_dic = {}
                    for p in ins:
                        #both = list(set(a) & set(b)) # interection of 2 lists 
                        germaine = list(set(must_before[p]) & set(ins)) 
                        local_dic[p] = germaine # germaine like jackson. I crack myself up
                    short_to_long = list(local_dic.keys())
                    short_to_long.sort(key = lambda x: len(local_dic[x]), reverse=True)

                    mp = len(short_to_long) //2
                    midd = int(short_to_long[mp])
                    out += midd

print(f"{out= }")

