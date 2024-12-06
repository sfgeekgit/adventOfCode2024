# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.
from collections import defaultdict


filename = "input05.txt"  
#filename = "test05.txt"

out = 0

must_after = defaultdict(list)

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
            else:
                ins = line.split(',')
                if len(ins) ==0:
                    print("nope")
                    quit()
                past = []
                good = True
                for p in ins:
                    for seen in past:
                        if p in must_after[seen]:
                            #print(f"wrong order {line=} {ins=} {p=} {past=} {seen=} {must_after[seen]=} ")
                            good = False
                            break
                        
                    past.append(p)
                if good:
                    mp = len(ins) //2
                    midd = int(ins[mp])
                    #print(f"line is good  {line= } {mp= } {midd= }")

                    out += midd

print(f"{out= }")

