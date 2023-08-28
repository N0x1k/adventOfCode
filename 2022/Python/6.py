input = open("6.txt").read()

for i in range(len(input)):
    packet = set()
    for char in input[i:i+14]:
        packet.add(char)
    if len(packet) == 14:
        break

print(i+14)
