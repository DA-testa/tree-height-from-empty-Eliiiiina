# python3

import threading


def compute_height(n, parents):
    tree = [[] for i in range(n)]
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)

    root = parents.index(-1)
    queue = [(root, 0)]
    max_height = 0

    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height + 1))
    return max_height


def main():
    text = input()
    if text[0] == "I":
        n = int(input())
        parents_str = input()
        parents = list(map(int, parents_str.split()))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = "test/"
        file_name = file_name + input()
        if "a" in file_name:
            return
        with open(file_name, 'r') as file:
            n = int(file.readline())
            parents_str = file.readline().strip()
            parents = list(map(int, parents_str.split()))
            height = compute_height(n, parents)
    print(height)


threading.stack_size(2**27)
threading.Thread(target=main).start()
