# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.

'''
strat: Hmmmm.. 
--First check if whole line passes
--Then they are small enough to brute force dropping each one and check it
--Tempting to track which index it first fails on and get all leet, but no.
'''

filename = "input02.txt"
#filename = "test02.txt"


def check_line_safe(reports):
    # Tempting to track which index it first fails on and get all leet, but no.
    updown = 0
    prev = -1
    for r in reports:
        if prev == -1:
            prev = r
        else:
            if abs(r - prev) >3 or abs(r-prev) < 1:
                #print (f"too big or small a change")
                return False
            if updown == 0:
                if r > prev:
                    updown = 1
                else:
                    updown = -1
            else:
                if (updown == 1 and r < prev) or (updown == -1 and r > prev):
                    return False
            prev = r
    # still here? then true!
    return True

safecnt = 0
badcnt  = 0 # just for the heck of it
with open(filename, "r") as file:
    for line in file:
        reports = [int(_) for _ in line.split()]
        ok = check_line_safe(reports)
        if ok:
            safecnt += 1  
        else:
            for i in range(len(reports)):
                rcpy = reports[::]
                rcpy.pop(i)
                if check_line_safe(rcpy):
                    ok = True
                    break
            if ok:
                safecnt += 1
            else:
                badcnt += 1

print(f"{badcnt=}")
print(f"{safecnt=}")