file = open("3-input.txt")
report = file.read().split()

ones=[0,0,0,0,0,0,0,0,0,0,0,0]
zeroes=[0,0,0,0,0,0,0,0,0,0,0,0]

for line in report:
  for i in range(len(line)):
    if line[i] == '0':
      zeroes[i] += 1
    else:
      ones[i] += 1

gamma = ""
epsilon = ""

for j in range(len(ones)):
  if ones[j] > zeroes[j]:
    gamma += "1"
    epsilon += "0"
  else:
    gamma += "0"
    epsilon += "1"

print(ones)
print(zeroes)
print(int(gamma,2)*int(epsilon,2))