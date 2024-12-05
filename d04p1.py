# Just a quick one off the get the answer
# Nothing fancy, skipping input checks, etc.


filename = "input04.txt"  
#filename = "test04.txt"

out = 0

# Um, try just every direction in order, forward, down, up, backward, then the 4 diagonals...
# Could do fancier, but simple is good.

board = []
with open(filename, "r") as file:
    for line in file:
        board.append(line[:-1])
        # check forward counts
        out += line.count('XMAS')
        # backwards
        out += line.count('SAMX')

height = len(board)
wide = len(board[0])

for i in range(height-3):
    for j in range(wide):  
        # down
        if board[i][j] == 'X':
            if board[i+1][j] == 'M':
                if board[i+2][j] == 'A':
                    if board[i+3][j] == 'S':
                        out += 1
        # up
        if board[i][j] == 'S':
            if board[i+1][j] == 'A':
                if board[i+2][j] == 'M':
                    if board[i+3][j] == 'X':
                        out += 1
        # down right
        if board[i][j] == 'X' and (j < (wide-3)):
            if board[i+1][j+1] == 'M':
                if board[i+2][j+2] == 'A':
                    if board[i+3][j+3] == 'S':
                        out += 1
        # up left
        if board[i][j] == 'S' and (j < (wide-3)):
            if board[i+1][j+1] == 'A':
                if board[i+2][j+2] == 'M':
                    if board[i+3][j+3] == 'X':
                        out += 1
        # down left
        if board[i][j] == 'X' and (j >= 3):
            if board[i+1][j-1] == 'M':
                if board[i+2][j-2] == 'A':
                    if board[i+3][j-3] == 'S':
                        out += 1
        # up right
        if board[i][j] == 'S' and (j >= 3):
            if board[i+1][j-1] == 'A':
                if board[i+2][j-2] == 'M':
                    if board[i+3][j-3] == 'X':
                        out += 1
            

print(f"{out= }")