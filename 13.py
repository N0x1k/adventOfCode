input = open("13-input.txt").read().split()
folds = open("13-folds.txt").read().split("\n")

p=[["." for i in range(1311)] for j in range(895)]

for l in input:
  x,y=map(int,l.split(','))
  p[y][x]="#"

for f in folds:
  f,s=(f.split()[2]).split("=")
  if f == "y":
    # fold by y axes
    p1=p[:int(s):]
    p2=p[int(s)::]

    x2=0
    for x1 in p2[::-1]:
      y2=0
      for y1 in x1:
        if y1=="#":
          p1[x2][y2]=y1
        y2+=1
      x2+=1

  else:
    # fold by x axes
    p1=[]
    for l in p:
      l1=l[:int(s):]
      l2=l[int(s)::]
      x1=0
      for x2 in l2[::-1]:
        if x2=="#":
          l1[x1]=x2
        x1+=1
      p1.append(l1)
  p=p1

for x in p1:
  print(x)
