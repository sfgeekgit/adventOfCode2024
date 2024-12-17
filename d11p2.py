from collections import Counter

input = [125, 17]
input = [5910927, 0, 1, 47, 261223, 94788, 545, 7771]

stones = input
blinks = 25
blinks = 75

# gotta do this as a counter.
# every zero -> a one, no need to count each zero seperatly
# wow, that runs fast.
# (beat my head against dynamic programing for a while, but this is so much faster and also simpler and better)
# how often does real, actual dynamic programing solve actual problems in production?
stones = Counter(input)

def blink(stonescnt):
    new_stones = Counter([])
    for v, cnt in stonescnt.items():
        if v == 0:
            new_stones[1] += cnt
        else:
            ss = str(v)
            digs = len(str(ss))
            if digs %2 ==0:
                a = ss[:digs//2]
                b = ss[digs//2:]
                new_stones[int(a)] += cnt
                new_stones[int(b)] += cnt
            else:
                new_stones[(v*2024)] += cnt



    return new_stones

for b in range(1, blinks+1):
    #print(f"before: {b=}  {stones=}")
    stones = blink(stones)
    #print(f"after {len(stones)=}")

out = sum(stones.values())

print(f"{out= }")