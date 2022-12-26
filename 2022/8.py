import numpy

trees = [[tree for tree in line] for line in open("8.txt").read().split("\n")]
tree_score = []

for i in range(len(trees)):
    for j in range(len(trees[i])):
        # skip edge trees as they will have score 0
        if i == 0 or j == 0 or i == (len(trees) - 1) or j == (len(trees[i]) - 1):
            continue

        i_length = len(trees)
        j_length = len(trees[i])
        inc = 1
        tmp_score = [0, 0, 0, 0]
        up = False
        down = False
        left = False
        right = False
        while True:
            if (i - inc) >= 0 and not up:
                tmp_score[0] += 1
                if trees[i - inc][j] >= trees[i][j]:
                    up = True
            else:
                up = True
            if (i + inc) < i_length and not down:
                tmp_score[1] += 1
                if trees[i + inc][j] >= trees[i][j]:
                    down = True
            else:
                down = True
            if (j - inc) >= 0 and not left:
                tmp_score[2] += 1
                if trees[i][j - inc] >= trees[i][j]:
                    left = True
            else:
                left = True
            if (j + inc) < j_length and not right:
                tmp_score[3] += 1
                if trees[i][j + inc] >= trees[i][j]:
                    right = True
            else:
                right = True
            if up and down and left and right:
                break
            inc += 1

        # print(f'i: {i}, j: {j}, score: {tmp_score}')
        tree_score.append(numpy.prod(tmp_score))

# print(tree_score)
print(max(tree_score))
