# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input03.txt"  
#filename = "test03c.txt"

out = 0

openchars = 'mul('
with open(filename, "r") as file:
    for line in file:
        lp = 0
        cur_str = ''
        while lp < len(line):
            char = line[lp]
            if len(cur_str) < len(openchars):
                cur_str += line[lp]
                #if cur_str == 'mul('[:len(cur_str)]:
                if cur_str == openchars[:len(cur_str)]:
                    pass
                else:
                    cur_str = ''
            elif cur_str == openchars:
                i,j = 0,0
                is_good = True
                num_a, num_b, cc  = '', '', ''
                while i <= 3 and is_good == True and cc != ',':
                    cc = line[lp+i]
                    if cc.isdigit():
                        num_a += cc
                        i += 1
                    elif cc ==',' and i > 0:
                        i += 1
                    else:
                        is_good = False
                        cur_str = ''
                    
                if cc==',' and i >0:
                    while j <= 3 and is_good == True:
                        ccc = line[lp+i+j]
                        if ccc.isdigit():
                            num_b += ccc
                            j += 1
                        elif ccc == ')' and j > 0:
                            j += 1
                            #print(f"---preadd --- {out=} {num_a=} {num_b=}")
                            out = out + (int(num_a) * int(num_b))
                            lp = lp +i + j -1
                            is_good = False
                            cur_str = ''
                        else:
                            is_good = False
                            cur_str = ''
            else:
                cur_str = ''

            lp +=1
            #print(f"{lp=} {char=} {cur_str=}")
        #print(line)
print(f"{out= }")
