file = open("1-input.txt")
inputs = list(map(int,file.read().split()))

triples=list()

for x in range(len(inputs)):
  try:
    triples.append(inputs[x]+inputs[x+1]+inputs[x+2])
  except:
    break

result=0

for y in range(len(triples)-1):
  if triples[y+1] > triples[y]:
    result += 1

print(result)
