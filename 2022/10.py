input_file = open("10.txt").read().split("\n")

cycles = []
x = 1
for line in input_file:
    if line == "noop":
        cycles.append(x)
    else:
        addx = int(line.split(" ")[1])
        cycles.append(x)
        x += addx
        cycles.append(x)

result = []
for i in range(20, 220, 40):
    result.append(cycles[i-1]*i)

print(cycles[219])
print(result)



