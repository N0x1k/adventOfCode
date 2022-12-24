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


def trans_guide(guide):
    for i in range(len(guide)):
        if "A" in guide[i]:
            if "A X" == guide[i]:
                guide[i] = "A Z"
            elif "A Y" == guide[i]:
                guide[i] = "A X"
            elif "A Z" == guide[i]:
                guide[i] = "A Y"
        elif "C" in guide[i]:
            if "C X" == guide[i]:
                guide[i] = "C Y"
            elif "C Y" == guide[i]:
                guide[i] = "C Z"
            elif "C Z" == guide[i]:
                guide[i] = "C X"
    return guide


print(f"score is: {score(trans_guide(guide))}")
