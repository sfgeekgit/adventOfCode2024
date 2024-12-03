print("hello")
filename = "input01.txt"

list1 = []
list2 = []
with open(filename, "r") as file:
    for line in file:
        [a,b] = line.split()
        list1.append(int(a))
        list2.append(int(b))

#list1 = [3,4,2,1,3,3]
#list2 = [4,3,5,3,9,3]

list1.sort()
list2.sort()
print(list1[0], len(list1))
print(list2[0], len(list2))
dist = 0
for i in range(len(list1)):
    dist += abs(list1[i] - list2[i])

print(dist)