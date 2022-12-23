p="SHHNCOPHONHFBVNKCFFC"
input = open("14-input.txt").read().split("\n")

rules={}
for x in input:
  k,v=x.split(" -> ")
  rules[k]=v

# Apply rules in x steps
for y in range(10):
  t=""
  for i in range(len(p)-1):
    x=""+p[i]+p[i+1]
    if x in rules:
      t+=p[i]+rules[x]
  t+=p[-1]
  p=t

# Count element occurences
c={}
for ch in p:
  if ch not in c:
    c[ch]=1
  else:
    c[ch]+=1

maxE=max(c,key=c.get)
minE=min(c,key=c.get)

print(f"Max element {maxE} has {c[maxE]}\nMin element {minE} has {c[minE]}\nResult is {c[maxE]-c[minE]}")

# print(len(p))


