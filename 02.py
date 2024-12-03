# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.

from collections import Counter

filename = "input01.txt"

list1 = []
list2 = []
with open(filename, "r") as file:
    for line in file:
        [a,b] = line.split()
        list1.append(int(a))
        list2.append(int(b))

# test data
#list1 = [3,4,2,1,3,3]
#list2 = [4,3,5,3,9,3]

#list1.sort()
#list2.sort()

cnt2 = Counter(list2)

sim = 0
for i in range(len(list1)):
    sim += list1[i] * cnt2[list1[i]]

print(sim)