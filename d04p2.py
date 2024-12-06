# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input04.txt"  
#filename = "test04.txt"

out = 0

# Look for an "A" then check its corners.
# look for "A" everywhere except the edges (row 0, etc)

board = []
with open(filename, "r") as file:
    for line in file:
        board.append(line[:-1])

height = len(board)
wide = len(board[0])


for i in range(1,height-1):
    for j in range(1, wide-1):  
        if board[i][j] == 'A':
            if (board[i-1][j-1] == 'M') and (board[i+1][j+1] == 'S'):
                    if (board[i-1][j+1] == 'M' and board[i+1][j-1] == 'S') or \
                        (board[i-1][j+1] == 'S' and board[i+1][j-1] == 'M'):
                        out += 1

            elif (board[i-1][j-1] == 'S') and (board[i+1][j+1] == 'M'):
                    if (board[i-1][j+1] == 'M' and board[i+1][j-1] == 'S') or \
                        (board[i-1][j+1] == 'S' and board[i+1][j-1] == 'M'):
                        out += 1

            # Attempt to balance complexity of code
            # could be shorter or longer, this middle made sense to me as I wrote it.


print(f"{out= }")