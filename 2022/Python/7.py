class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []

    def add_node(self, obj):
        self.children.append(obj)

    def get_node(self, node_name):
        path = node_name.split("/")
        node = self
        for target in path:
            for child in node.children:
                if child.name == target:
                    node = child
                    break
            else:
                raise Exception(f"No child found with name {target} in node {node.name}")

        return node

    def count_sizes(self):
        for child in self.children:
            child.count_sizes()

    def get_all_dir_nodes(self):
        nodes = []
        for child in self.children:
            nodes.append(child)
            nodes.extend(child.get_all_dir_nodes())
        return nodes


class Node:
    def __init__(self, name, size=0, is_dir=True):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children = []

    def add_node(self, obj):
        self.children.append(obj)

    def __str__(self):
        return str(self.name)

    def count_sizes(self):
        for child in self.children:
            if child.is_dir and child.children:
                child.count_sizes()
            self.size += child.size

    def get_all_dir_nodes(self):
        nodes = []
        for child in self.children:
            if child.is_dir:
                nodes.append(child)
            if child.children:
                nodes.extend(child.get_all_dir_nodes())
        return nodes


input_file = open("7.txt").read().split("\n")
file_system = Tree("root")
file_system.add_node(Node("root_node"))
cursor = "root_node"
line_no = 0

# populate tree from input
while line_no < len(input_file):
    split_line = input_file[line_no].split(" ")

    # move cursor
    if split_line[1] == "cd":
        if split_line[2] == "..":
            tmp = cursor.split("/")
            tmp.pop()
            cursor = "/".join(item for item in tmp)
        else:
            cursor = cursor + "/" + split_line[2]
        line_no += 1

    # create children
    elif input_file[line_no] == "$ ls":
        line_no += 1
        while line_no < len(input_file):
            if input_file[line_no][0] == "$":
                break
            size, name = input_file[line_no].split(" ")
            if size == "dir":
                file_system.get_node(cursor).add_node(Node(name))
            else:
                file_system.get_node(cursor).add_node(Node(name, int(size), False))
            line_no += 1

# calculate sizes of dirs
file_system.count_sizes()

first_result = 0
target_size = 30000000 - (70000000 - file_system.get_node("root_node").size)
second_results =[]
for node in file_system.get_all_dir_nodes():
    # first part
    if node.size < 100000:
        first_result += node.size

    # second part
    if node.size > target_size:
        second_results.append(node.size)

print(f'First part: {first_result}')
print(f'Second part: {min(second_results)}')
