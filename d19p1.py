input_file = "test19.txt"
input_file = "input19.txt"

with open(input_file) as f:
    # read the first line
    first_line = f.readline()
    first_line = first_line.strip()
    avails = first_line.split(", ")

    second_line = f.readline() # skip the second line


    impossible_cnt = 0
    can_do_cnt = 0
    for line in f:
        seek = line.strip()
        
        if len(seek) > 0:

            # dp[i] will be True if we can make seek[0:i] using avails
            dp = [False] * (len(seek) + 1)
            dp[0] = True  # empty string is always possible
            
            # For each position in seek
            for i in range(1, len(seek) + 1):
                # Try each available substring
                for substr in avails:
                    # Check if the current substring can be used at this position
                    if (i >= len(substr) and 
                        dp[i - len(substr)] and 
                        seek[i - len(substr):i] == substr):
                        dp[i] = True
                        break
            
            if not dp[len(seek)]:
                impossible_cnt += 1
            else:
                can_do_cnt += 1
                print(f"{seek=} can be made")

print(f"{impossible_cnt= }")
print(f"{can_do_cnt= }")
