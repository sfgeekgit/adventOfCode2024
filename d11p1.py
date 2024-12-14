input = [125, 17]
input = [5910927, 0, 1, 47, 261223, 94788, 545, 7771]

stones = input
blinks = 25

def blink(stones):
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
        else:
            ss = str(s)
            digs = len(str(ss))
            
            if digs %2 ==0:
                a = ss[:digs//2]
                b = ss[digs//2:]
                new_stones.extend([int(a), int(b)])
            else:
                new_stones.append(s * 2024)    

    return new_stones

for b in range(1, blinks+1):
    print(f"before: {b=} {stones=}")
    stones = blink(stones)
    print(f"after {len(stones)=}")
    print("\n")

print(f"{len(stones)= }")