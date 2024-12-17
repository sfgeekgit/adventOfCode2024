#input = [125, 17]
input = [5910927, 0, 1, 47, 261223, 94788, 545, 7771]

stones = input
blinks = 6
blinks = 25
blinks = 75

# Memoization dictionary to store the number of resulting stones for a given stone and number of blinks
memo = {}

def process_stone(s, remaining_blinks):
    if (s, remaining_blinks) in memo:
        return memo[(s, remaining_blinks)]
    
    if remaining_blinks == 0:
        result_len = 1
    elif s == 0:
        result_len = process_stone(1, remaining_blinks - 1)
    else:
        ss = str(s)
        digs = len(ss)
        if digs % 2 == 0:
            mid = digs // 2
            a, b = int(ss[:mid]), int(ss[mid:])
            result_len = process_stone(a, remaining_blinks - 1) + process_stone(b, remaining_blinks - 1)
        else:
            result_len = process_stone(s * 2024, remaining_blinks - 1)
    
    memo[(s, remaining_blinks)] = result_len
    return result_len

def blink(stones, remaining_blinks):
    total_stones = 0
    for s in stones:
        total_stones += process_stone(s, remaining_blinks)
    return total_stones

total_stones = blink(stones, blinks)
#print(f"{memo=}")

print("Final number of stones:") 
print(f"{total_stones=}")