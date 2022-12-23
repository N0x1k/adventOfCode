file = open("3-input.txt")
report1 = file.read().split()
report2 = report1

# oxygen generator rating
for i in range(12):
  ones=0
  zeroes=0
  nextline=list()

  for line in report1:
    if line[i] == "1":
      ones += 1
    else:
      zeroes += 1

  if ones >= zeroes:
    dominant = "1"
  else:
    dominant = "0"

  for line in report1:
    if line[i] == dominant:
      nextline.append(line)
  
  if len(nextline) == 1:
    oxygen=nextline[0]
    break
  else:
    report1=nextline

#print(report2)

# CO2 scrubber rating
for i in range(12):
  ones=0
  zeroes=0
  nextline=list()

  for line in report2:
    if line[i] == "1":
      ones += 1
    else:
      zeroes += 1

  if zeroes <= ones:
    dominant = "0"
  else:
    dominant = "1"

  for line in report2:
    if line[i] == dominant:
      nextline.append(line)
  
  if len(nextline) == 1:
    co2=nextline[0]
    break
  else:
    report2=nextline

print(int(oxygen,2)*int(co2,2))