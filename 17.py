import pdb

input = "target area: x=85..145, y=-163..-108"
# input = "target area: x=20..30, y=-10..-5"
tx1, tx2 = map(int,(((input.split()[2]).replace("x=","")).replace(",","")).split(".."))
ty1, ty2 = map(int,((input.split()[3]).replace("y=","")).split(".."))
x,y=(0,0)

# find y hitting the target
a = False
maxyStep = 0
dys = {}
for i in range(300,-200,-1):
  dy = i
  # print(f"testing dy {i}")
  for j in range(800):
    y += dy
    # print(f"step {j}, y={y}")
    if (y >= ty1) and (y <= ty2):
      # print(f"y hit found, initial dy: {i}, max y: {maxy}")
      maxyStep = max(j, maxyStep)
      if i not in dys:
        dys[i] = [j]
      else:
        dys[i].append(j)
    dy -= 1
  y = 0
  maxy = 0
  # pdb.set_trace()
  if a: break

a = False
dxs = {}
for k in range(300):
  dx = k
  for l in range(maxyStep+1):
    x += dx
    if (x >= tx1) and (x <= tx2):
      # print(f"x hit found, initial dx: {k}")
      if k not in dxs:
        dxs[k] = [l]
      else:
        dxs[k].append(l)
    if dx > 0:
      dx -= 1
  x = 0
  if a: break

res=set()
for y,ys in dys.items():
  for i in ys:
    for x,xs in dxs.items():
      if i in xs:
        res.add((x,y))

# print(res)
print(len(res))