from copy import deepcopy

p="SHHNCOPHONHFBVNKCFFC"
input = open("14-input.txt").read().split("\n")

r={}
c={}
for x in input:
  k,v=x.split(" -> ")
  r[k]=[v,0]
  if v not in c:
    c[v]=0

# count initial state
for j in range(len(p)-1):
  x=""+p[j]+p[j+1]
  r[x][1]+=1
  c[p[j]]+=1

c[p[-1]]+=1

# Apply rules in x steps
r2=deepcopy(r)
for i in range(40):
  for k,v in r.items():
    if v[1]>0:
      nk1=""+k[0]+v[0]
      nk2=""+v[0]+k[1]
      r2[nk1][1]+=v[1]
      r2[nk2][1]+=v[1]
      r2[k][1]-=v[1]
      c[v[0]]+=v[1]
  r=deepcopy(r2)

# for k,v in r.items():
#   print(f"'{k}' : {v}")
maxE=max(c,key=c.get)
minE=min(c,key=c.get)
# print(f"Max is '{maxE}': {c[maxE]}\nMin is '{minE}': {c[minE]}")
print(c[maxE]-c[minE])
