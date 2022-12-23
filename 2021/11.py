input = open("11-input.txt").read().split()
f=[0]
n=[
  (1,0),
  (0,1),
  (1,1),
  (-1,0),
  (0,-1),
  (-1,-1),
  (1,-1),
  (-1,1)
]

def flash(x,y):
  f[0]+=1
  flashed.append((x,y))
  p[x][y]=0

def evalNeighbours(i,j):
  for k, l in n:
    newx=i+k
    newy=j+l
    if (newx>=0) and (newy>=0):
      if (newx,newy) not in flashed:
        try:
          p[newx][newy]+=1
          if p[newx][newy] > 9:
            flash(newx,newy)
            evalNeighbours(newx,newy)
        except IndexError:
          pass

# create 2d list of octopuses
p=[]
for i in input:
  p.append([int(c) for c in i])

# number of steps to count
for s in range(100):
  flashed=[]

  for i, l in enumerate(p):
    for j in range(len(l)):
      if (i,j) not in flashed:
        p[i][j]+=1
        if p[i][j] > 9:
          flash(i,j)
          evalNeighbours(i,j)

  # print(f"\nAfter Step {s}")
  # for x in p:
  #   print(x)

print(f)