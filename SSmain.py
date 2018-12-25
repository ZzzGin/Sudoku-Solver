import SS

print("Input the board by rows, '.' as a blank.")
board = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    input_r = input("row" + str(i) + ": ")
    for c in input_r:
        board[i].append(c)
for b in board:
    print(b)
print("Calculating...")
s = SS.Solution()
r = s.solveSudoku(board)
for r_s in r:
    print(r_s)