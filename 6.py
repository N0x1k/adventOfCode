file = open("6-input.txt")
school = list(map(int,file.read().split(",")))

print(len(school))

for i in range(80):
  
  for i in range(len(school)):

    # spawn new fish and reset timer
    if school[i] == 0:
      school[i] = 6
      school.append(8)
    else:
      school[i] -= 1
  
#   print(school)

print(len(school))