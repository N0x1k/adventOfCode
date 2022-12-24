input = open("4.txt").read().split("\n")

count1 = 0
count2 = 0
for line in input:
    set1, set2 = line.split(",")
    set1x, set1y = set1.split("-")
    set2x, set2y = set2.split("-")
    set1 = {*range(int(set1x), int(set1y)+1)}
    set2 = {*range(int(set2x), int(set2y)+1)}

    if set1.issubset(set2) or set1.issuperset(set2):
        count1 += 1

    if len(set1.intersection(set2)) > 0:
        count2 += 1

print(f"first: {count1}")
print(f"second: {count2}")
