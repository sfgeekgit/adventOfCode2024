# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input07.txt"  
#filename = "test07.txt"

out = 0

with open(filename, "r") as file:
    for line in file:
        line = line[:-1]
        print(line)
        [res_seek,nums] = line.split(':')
        res_seek = int(res_seek)
        nums = [int(_) for _ in nums.split()]
        is_valid = False
        slots = len(nums)-1
        perms = 3**(slots)
        for p in range(perms):
            cur_val = nums[0]
            ops = ['+'] * slots
            foo = p
            for i in range(slots):
                if foo % 3 == 2: # mult
                    #ops[i] = '*' 
                    cur_val = cur_val * nums[i+1]
                elif foo %3 == 1: # concat
                    cur_val = int(str(cur_val) + str(nums[i+1]))
                else: #add
                    cur_val = cur_val + nums[i+1]                

                foo = foo //3
            
            if cur_val == res_seek:
                is_valid = True
                break

        if is_valid:
            out += res_seek

print(f"{out= }")
