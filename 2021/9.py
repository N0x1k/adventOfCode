input = open("9-input.txt").read().split()
a=list()

for i in input:
  a.append(list(map(int,i)))

d=list()
for i in range(len(a)):
  for j in range(len(a[i])):
    if a[i][j] != 9:
      # Locate a low point and store near basin points
      b=True
      e=list()
      if j+1<len(a[i]):
        b = b and (a[i][j] < a[i][j+1])
      if j>0:
        b = b and (a[i][j] < a[i][j-1])
      if i+1<len(a):
        b = b and (a[i][j] < a[i+1][j])
      if i>0:
        b = b and (a[i][j] < a[i-1][j])

      # Operate on a low point  
      if b:
        # print(f"found low point {a[i][j]}\n\n")
        e.append((i,j))
        # iterate on low point neighbours 
        for k in e:
          l=k[0]
          m=k[1]
          # print(f"testing neighbour point: {k} - {a[l][m]}\n\n")
          if m+1<len(a[l]):
            if (a[l][m+1] != 9) and ((l,m+1) not in e):
              e.append((l,m+1))
          if m>0:
            if (a[l][m-1] != 9) and ((l,m-1) not in e):
              e.append((l,m-1))
          if l+1<len(a):
            if (a[l+1][m] != 9) and ((l+1,m) not in e):
              e.append((l+1,m))
          if l>0:
            if (a[l-1][m] != 9) and ((l-1,m) not in e):
              e.append((l-1,m))
          # print(f"basin points so far: {e}\n\n")
        d.append(e)

# Sort from largest basin
d = sorted(d, key=len, reverse=True)

c = len(d[0]) * len(d[1]) * len(d[2])

print(c)


