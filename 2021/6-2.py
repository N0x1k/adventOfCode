file = open("6-input.txt")
schoolSource = list(map(int,file.read().split(",")))

school = [0 for i in range(9)]

for fish in schoolSource:
  school[fish] += 1

for i in range(256):

  tmpSchool = [0 for i in range(9)]
  for j in range(len(school)):

    # spawn new fish and reset timer
    if j == 0:
      tmpSchool[6] += school[j]
      tmpSchool[8] += school[j]
    else:
      tmpSchool[j-1] += school[j]
  school = tmpSchool

# sum of school is all fish
count = 0
for fish in school:
  count += fish
print('Total number of fish: ', count)