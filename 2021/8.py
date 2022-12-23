input = open("8-input.txt").read().split("\n")

a=list()
d=list()
for line in input:
  a.append(line.split(" | "))

display_orig = ['a','b','c','d','e','f','g']
display = ['a','b','c','d','e','f','g']

s = 0
for i in a:
  b = [
  "abcefg",    # 0
  "cf",        # 1  
  "acdeg",     # 2
  "acdfg",     # 3
  "bcdf",      # 4  
  "abdfg",     # 5  
  "abdefg",    # 6
  "acf",       # 7
  "abcdefg",   # 8  
  "abcdfg"     # 9  
  ]
  c = sorted(i[0].split(), key=len)
  d = i[1].split()

  # identify 'a' wiring
  display[0] = (set(c[1]).difference(c[0])).pop()

  # identify 'g' wiring and 9 index
  for i in range(6,9):
    if set(c[2]).issubset(c[i]):
      display[6] = ((set(c[i]).difference(c[2])).difference(display[0])).pop()
      nineIndex = i

  # identify 'e' wiring
  display[4] = (set(c[9]).difference(c[nineIndex])).pop()

  # identify 'd' wiring and 2 index
  for i in range(3,6):
    if len(set(c[2]).intersection(c[i])) == 2:
      display[3] = (set(c[i]).difference(set(c[1]).union(display[6],display[4]))).pop()
      twoIndex = i

  # identify 'b' wiring and 3&5 indexes
  for i in range(3,6):
    if i != twoIndex:
      if len(set(c[0]).intersection(c[i])) == 2:
        display[1] = (set(c[2]).difference(c[i])).pop()
      else:
        fiveIndex = i
  
  # indetify 'c' wiring
  display[2] = (set(c[0]).difference(c[fiveIndex])).pop()

  # identify 'f' wiring
  display[5] = (set(c[0]).difference(display[2])).pop()

  # assign new display wiring to template numbers for comparison
  for i in range(len(b)):
    e=list(b[i])
    for j in range(len(e)):
      e[j] = display[display_orig.index(e[j])]
    b[i] = set("".join(e))

  # translate coded digits
  f=""
  for i in d:
    for j in range(len(b)):
      if len(b[j].symmetric_difference(i)) == 0:
        f += str(j)

  # print(f"source:\n{c}\n\ncoded digits:\n{d}\n\ndictionary:\n{b}\n\nresult:{f}")

  s += int(f)

print(s)
