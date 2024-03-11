word = input().upper()
rows = int(input())
columns = int(input())
board = []
counter = 0
row = []
column = []

for i in range(rows):
    letterRow = input().replace(' ', '').upper()
    board.append(letterRow)

for i in enumerate(board):
    column.append(board[0][i[0]] + board[1][i[0]] + board[2][i[0]])
    for j in enumerate(i[1]):
        ROW = i[0]
        COLUMN = j[0]
                        

print(board)
                
