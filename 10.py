input = open("10-input.txt").read().split()

openingChars = ['(','[','{','<']
closingChars = [')',']','}','>']
score = {
  ')':1,
  ']':2,
  '}':3,
  '>':4
}

isOpening = lambda a : a in openingChars
e=list()

for line in input:
  b=list()
  kill=False
  for i in line:
    if isOpening(i):
      b.append(i)
    else:
      for j in range(1,len(b)+1):
        if (closingChars.index(i) == openingChars.index(b[-j])):
          b.pop(-j)
          break
        else:
          print(f"Expected '{closingChars[openingChars.index(b[-j])]}', but found '{i}' instead")
          kill=True
          break
    if kill:
      break
  if kill:
    continue
  # print("unfinished line, counting score")
  # Complete unfinished line and count score
  d=0
  for j in range(1,len(b)+1):
    # print(f"{closingChars[openingChars.index(b[-j])]}")
    d = d*5+score[closingChars[openingChars.index(b[-j])]]
  e.append(d)

print(e)
e = sorted(e)
print(e[len(e)//2])
