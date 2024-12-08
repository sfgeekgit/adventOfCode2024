# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.
from collections import defaultdict


filename = "input08.txt"  
#filename = "test08b.txt"
#filename = "test08.txt"

out = 0

map = defaultdict(list)
i=0
wide = False
with open(filename, "r") as file:
    for line in file:
        line = line[:-1]
        chars = list(line)
        if wide == False:
            wide = len(chars)
        for j, c in enumerate(chars):
            if c != '.':
                map[c].append([i,j])


        i+= 1

high = i
# in bounds is  >= 0 and < wide  (or high) but NOT <= wide or high 
#   0 <= j < wide # valid
#   0 <= i < high # valid

new_nodes = set()

for let in map.keys():
    print(let)
    for idx, [i_a, j_a] in enumerate(map[let]):
        #print(idx, i_a, j_a)
        if idx <= (len(map[let]) -1):
            idxb = idx +1
            while idxb < len(map[let]):
                [i_b, j_b] = map[let][idxb]
                #print(f"{idxb=} {i_a=} {j_a=} {i_b=} {j_b=}  {map[let]=}")
                idxb += 1

                i_dist = abs(i_a - i_b)
                j_dist = abs(j_a - j_b)
                if i_a < i_b:
                    i_dist = 0 - i_dist
                if j_a < j_b:
                    j_dist = 0 - j_dist

                i_n1 = i_a
                j_n1 = j_a

                i_n2 = i_b
                j_n2 = j_b

                while (0 <= i_n1 < high) and (0 <= j_n1 < wide):
                    new_nodes.add((i_n1, j_n1))
                    i_n1 += i_dist
                    j_n1 += j_dist

                i_dist = 0 - i_dist
                j_dist = 0 - j_dist

                while (0 <= i_n2 < high) and (0 <= j_n2 < wide):
                    new_nodes.add((i_n2, j_n2))
                    i_n2 += i_dist
                    j_n2 += j_dist


                '''
                if i_a > i_b:
                    i_n1 = i_a + i_dist
                    i_n2 = i_b - i_dist
                else:
                    i_n1 = i_a - i_dist
                    i_n2 = i_b + i_dist

                if j_a > j_b:
                    j_n1 = j_a + j_dist
                    j_n2 = j_b - j_dist
                else:
                    j_n1 = j_a - j_dist
                    j_n2 = j_b + j_dist
                #print(f"{j_a=} {j_b=} {j_n1=} {j_dist=}")

                new1 = (i_n1, j_n1)
                new2 = (i_n2, j_n2)

                if  (0 <= i_n1 < high) and (0 <= j_n1 < wide): # valid
                    new_nodes.add(new1)
                if  (0 <= i_n2 < high) and (0 <= j_n2 < wide): # valid
                    new_nodes.add(new2)
                '''
                #print(new_nodes)
                #quit()

print(new_nodes)
print(len(new_nodes))
                
#   0 <= j < wide # valid
#   0 <= i < high # valid