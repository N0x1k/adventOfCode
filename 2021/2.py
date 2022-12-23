file = open("2-input.txt")
course = file.read().split("\n")

horizontal = 0
aim = 0
depth = 0

for x in course:
  if x.split()[0] == 'forward':
    horizontal += int(x.split()[1])
    depth += int(x.split()[1])*aim
    continue
  if x.split()[0] == 'down':
    aim += int(x.split()[1])
    continue
  if x.split()[0] == 'up':
    aim -= int(x.split()[1])

print(horizontal*depth)