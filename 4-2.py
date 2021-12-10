file1 = open("4-input-draw.txt")
draws = file1.read().split(',')

file2 = open("4-input.txt")
boardsSource = file2.read().split('\n')

#print(boardsSource)

boards = list()
matrix = list()

# Create board matrices
for line in boardsSource:
  if len(matrix) < 5:
    matrix.append(line.split())
  else:
    boards.append(matrix)
    matrix = list()

#print(boards)
winners = list()

for draw in draws:

  for board in range(len(boards)):
    countList = [0,0,0,0,0]
    for row in boards[board]:
      count = 0
      for number in range(len(row)):
        # remove all drawn numbers from boards
        if row[number] == draw:
          row[number] = ""
        elif row[number] != "":
          # count sums of rows in boards
          count += int(row[number])
          # count sums of columns in boards
          countList[number] += int(row[number])
      # if a board has empty row, it's a winning board
      if count == 0:
        if board not in winners:
          winners.append(board)
          winDraw = draw
        break
    for columnSum in countList:
      if columnSum == 0:
        if board not in winners:
          winners.append(board)
          winDraw = draw

# print('the last winning board:')
# print(boards[winners[-1]])
# print('winner arr')
# print(winners)

# count score
score = 0
for board in boards[winners[-1]]:
  for row in board:
    if row != "":
      score += int(row)

print(score*int(winDraw))
