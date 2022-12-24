guide = open("2.txt").read().split("\n")


def score(guide):
    score = 0
    for line in guide:
        if "X" in line:
            score += 1
        elif "Y" in line:
            score += 2
        else:
            score += 3

        if line in ["A X", "B Y", "C Z"]:
            score += 3
        elif line in ["C X", "A Y", "B Z"]:
            score += 6
    return score


def translate_guide(guide):
    xyz = ["X", "Y", "Z"]
    for i in range(len(guide)):
        my_strategy = guide[i].split(" ")[1]
        if "A" in guide[i]:
            guide[i].replace(my_strategy, xyz[xyz.index(my_strategy) - 1])
        elif "C" in guide[i]:
            if xyz.index(my_strategy) + 1 == len(xyz):
                guide[i].replace(my_strategy, xyz[0])
            else:
                guide[i].replace(my_strategy, xyz[xyz.index(my_strategy) + 1])


translate_guide(guide)
print(f"score is: {score(guide)}")
