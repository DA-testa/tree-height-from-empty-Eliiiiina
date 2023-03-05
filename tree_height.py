# python3

import sys
import threading
import numpy as np

# function to compute the height of the tree
def compute_height(n, parents):
    # create an empty tree as a list of lists
    tree = [[] for i in range(n)]

    # fill the tree with children
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)

    # initialize the root of the tree
    root = np.where(parents == -1)[0][0]

    # initialize the queue with the root node
    queue = [(root, 0)]

    # initialize the maximum height to 0
    max_height = 0

    # traverse the tree using BFS
    while queue:
        node, height = queue.pop(0)
        # update the maximum height
        max_height = max(max_height, height)
        # add the children of the current node to the queue
        for child in tree[node]:
            queue.append((child, height + 1))

    return max_height


# main function to read input and call the compute_height function
def main():
    # read the input type (keyboard or file)
    text = input().strip()

    # read the input accordingly
    if text == "I":
        # read input from keyboard
        n = int(input().strip())
        parents_str = input().strip()
        parents = np.array(list(map(int, parents_str.split())))
        height = compute_height(n, parents)
    elif text == "F":
        # read input from file
        file_name = "test/" + input().strip()
        if "a" in file_name:
            return
        with open(file_name, 'r') as file:
            n = int(file.readline().strip())
            parents_str = file.readline().strip()
            parents = np.array(list(map(int, parents_str.split())))
            height = compute_height(n, parents)

    # output the height of the tree
    print(height)


# increase recursion limit and stack size for large input
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# create a new thread and start the main function
threading.Thread(target=main).start()

