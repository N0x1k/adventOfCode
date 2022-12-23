input = open("10-input.txt").read().split()

chunks = {
  '(':')',
  '[':']',
  '{':'}',
  '<':'>'
}

score = {
  ')':1,
  ']':2,
  '}':3,
  '>':4
}

e=list()

for line in input:
  b=list()
  for i in line:
    if i in chunks:
      b.append(i)
    elif (chunks[b[-1]] == i):
      b.pop()
    else:
      # print(f"Expected '{chunks[b[-1]]}', but found '{i}' instead")
      break
  else:
    d=0
    for j in b[::-1]:
      d = d*5+score[chunks[j]]
    e.append(d)

e.sort()
print(e[len(e)//2])
