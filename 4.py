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

for draw in draws:

  for board in range(len(boards)):
    countList = [0]*5
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
        print("This row won!")
        print(boards[board])
        break
    if count == 0:
      break
    for columnSum in countList:
      if columnSum == 0:
        print("This column won!")
        print(boards[board])
        break
  if count == 0:
    break
  for columnSum in countList:
      if columnSum == 0:
        break

# count score
score = 0
for winner in boards[board]:
  for row in winner:
    if row != "":
      score += int(row)

print(score*int(draw))
