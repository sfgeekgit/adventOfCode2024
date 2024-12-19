input_file = "test19.txt"
input_file = "input19.txt"

with open(input_file) as f:
    # read the first line
    first_line = f.readline()
    first_line = first_line.strip()
    avails = first_line.split(", ")

    second_line = f.readline() # skip the second line

    total_cnt = 0
    impossible_cnt = 0
    for line in f:
        seek = line.strip()
        if len(seek) == 0:
            continue

        # Thanks to some "modern programming" here.
        
        # dp[i] will store the number of ways to make seek[0:i] using avails
        dp = [0] * (len(seek) + 1)
        dp[0] = 1  # empty string can be made in exactly one way
        
        # For each position in seek
        for i in range(1, len(seek) + 1):
            # Try each available substring
            for substr in avails:
                # Check if the current substring can be used at this position
                if (i >= len(substr) and 
                    seek[i - len(substr):i] == substr):
                    dp[i] += dp[i - len(substr)]
        
        if dp[len(seek)] == 0:
            impossible_cnt += 1
        else:
            print(f"{seek} can be made in {dp[len(seek)]} ways")
            total_cnt += dp[len(seek)]

print(f"{total_cnt=}")
