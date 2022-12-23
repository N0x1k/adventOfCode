file = open("5-input.txt")
rawVectors = file.read().split("\n")

lineVectors = list()
diagram = [[0 for i in range(999)] for i in range(999)]

for row in rawVectors:
  line = list()

  for vectorPair in row.split(' -> '):
    line.append(list(map(int,vectorPair.split(','))))

  x1 = int(line[0][0])
  x2 = int(line[1][0])
  y1 = int(line[0][1])
  y2 = int(line[1][1])

  # define mid points to complete the line
  if (x1 > x2) and (y1 == y2):
    for midpoint in [i for i in range(x2+1,x1)]:
      line.append([midpoint,y1])
  elif (x1 > x2) and (y1 > y2):
    midx = [i for i in range(x2+1,x1)]
    midy = [i for i in range(y2+1,y1)]
    for i in range(len(midx)):
      line.append([midx[i],midy[i]])
  elif (x1 > x2) and (y1 < y2):
    midx = [i for i in range(x2+1,x1)]
    midy = [i for i in range(y1+1,y2)]
    for i in range(1,len(midx)+1):
      line.append([midx[i-1],midy[-i]])
  elif (x1 < x2) and (y1 == y2):
    for midpoint in [i for i in range(x1+1,x2)]:
      line.append([midpoint,y1])
  elif (x1 < x2) and (y1 > y2):
    midx = [i for i in range(x1+1,x2)]
    midy = [i for i in range(y2+1,y1)]
    for i in range(1,len(midx)+1):
      line.append([midx[-i],midy[i-1]])
  elif (x1 < x2) and (y1 < y2):
    midx = [i for i in range(x1+1,x2)]
    midy = [i for i in range(y1+1,y2)]
    for i in range(len(midx)):
      line.append([midx[i],midy[i]])
  elif (x1 == x2) and (y1 > y2):
    for midpoint in [i for i in range(y2+1,y1)]:
      line.append([x1,midpoint])
  elif (x1 == x2) and (y1 < y2):
    for midpoint in [i for i in range(y1+1,y2)]:
      line.append([x1,midpoint])

  # print(line)
  
  # fill diagram
  for point in line:
    #print(point)
    diagram[point[0]][point[1]] += 1

# count all points with 2 or more lines crossing
count = 0
for row in diagram:
  for point in row:
    if point > 1:
      count += 1

print("Points with 2+ ", count)

# for i in diagram:
#   print(i)


