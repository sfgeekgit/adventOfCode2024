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
        binn = len(nums)-1
        perms = 2**(binn)
        for p in range(perms):
            cur_val = nums[0]
            #ops = ['+'] * binn
            foo = p
            for i in range(binn):
                if foo % 2 == 1: # mult
                    #ops[i] = '*' 
                    cur_val = cur_val * nums[i+1]
                else: #add
                    cur_val = cur_val + nums[i+1]                
                if cur_val > res_seek: # only gets bigger in current puzzle
                  break

                foo = foo //2
            if cur_val == res_seek:
                is_valid = True
                break

        if is_valid:
            out += res_seek

print(f"{out= }")
