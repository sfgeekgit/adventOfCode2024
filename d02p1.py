# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.

filename = "input02.txt"
#filename = "test02.txt"


safecnt = 0
badcnt  = 0 # just for the heck of it
with open(filename, "r") as file:
    for line in file:
        reports = [int(_) for _ in line.split()]
        ok = True
        updown = 0
        prev = -1
        for r in reports:
            if prev == -1:
                prev = r
            else:
                if abs(r - prev) >3 or abs(r-prev) < 1:
                    #print (f"too big or small a change")
                    ok = False
                    break
                if updown == 0:
                    if r > prev:
                        updown = 1
                    else:
                        updown = -1
                else:
                    if (updown == 1 and r < prev) or (updown == -1 and r > prev):
                        ok = False
                        break
                prev = r
        if ok:
            safecnt += 1  
        else:
            badcnt += 1

print(f"{badcnt=}")
print(f"{safecnt=}")



