input_stacks = open("5-stacks.txt").read().split("\n")
stacks = [[], [], [], [], [], [], [], [], []]

input_instructions = open("5-input.txt").read().split("\n")

for line in input_stacks:
    space_count = 0
    stack_id = 0
    for i in range(len(line)):
        if line[i] == " ":
            space_count += 1
            if space_count == 4:
                space_count = 0
                stack_id += 1
            continue
        if line[i] == "[":
            stacks[stack_id].append(line[i+1])
            stack_id += 1
            space_count = 0

for instruction in input_instructions:
    count = int((instruction.split("move ")[1])[0:2])
    from_index = int((instruction.split("from ")[1])[0])
    to_index = int((instruction.split("to ")[1])[0])

    # # First
    # for c in range(count):
    #     tmp = stacks[from_index - 1].pop(0)
    #     stacks[to_index -1].insert(0, tmp)

    # Second
    tmp = stacks[from_index - 1][0:count]
    for c in range(count):
        stacks[from_index - 1].pop(0)
    stacks[to_index - 1][:0] = tmp

result = []
for stack in stacks:
    result.append(stack[0])

print(result)
