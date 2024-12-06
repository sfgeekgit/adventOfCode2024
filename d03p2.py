# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input03.txt"  
#filename = "test03c.txt"
#filename = "test03_2.txt"

out = 0

openchars = ['mul(', 'do(','don\'t(']

enabled = True

with open(filename, "r") as file:
    for line in file:
        lp = 0
        cur_str = ''
        while lp < len(line):
            char = line[lp]
            if cur_str == 'mul(':
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
            elif cur_str == 'do(':
                if char == ')':
                    enabled = True
                cur_str = ''

            elif cur_str == 'don\'t(':
                if char == ')':
                    enabled = False
                cur_str = ''
            
            else:
                cur_str += line[lp]
                if enabled == True:
                    valid_cmds = openchars
                else:
                    valid_cmds = ['do(']

                valid = False
                for cmd in valid_cmds:
                    if cur_str == cmd[:len(cur_str)]:
                        valid = True
                if valid == False:
                    cur_str = ''

            lp +=1
            #print(f"{lp=} {char=} {cur_str=}")
        #print(line)
print(f"{out= }")
