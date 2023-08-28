input = open("3.txt").read().split("\n")

score_card = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def first(input, score_card):
    result = []
    for backpack in input:
        divider = int(len(backpack)/2)
        for item in backpack[0:divider]:
            if item in backpack[divider:]:
                result.append(score_card.index(item))
                break
    return result


def second(input, score_card):
    result = []
    i = 0
    while i < len(input):
        for item in input[i]:
            if item in input[i+1] and item in input[i+2]:
                result.append(score_card.index(item))
                i = i + 3
                break
    return result


print(sum(first(input, score_card)))
print(sum(second(input, score_card)))
