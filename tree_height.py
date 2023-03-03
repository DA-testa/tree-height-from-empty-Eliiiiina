# python3

#import sys
#import threading
#import numpy


#def compute_height(n, parents):
    # Write this function
 #   max_height = 0
    # Your code here
  #  return max_height


#def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
 #   pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
import sys
import threading
import numpy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(n, parents):
    # Create a list of n nodes
    nodes = [Node(i) for i in range(n)]

    # Find the root node and add children to their parent nodes
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    return root

def compute_height(node):
    # Base case: if node has no children, its height is 1
    if not node.children:
        return 1

    # Recursive case: find the height of each child, and return the max height + 1
    heights = [compute_height(child) for child in node.children]
    return max(heights) + 1

def main():
    # Read input from stdin
    n = int(input())
    parents = list(map(int, input().split()))

    # Build the tree
    root = build_tree(n, parents)

    # Compute the height and print the result
    height = compute_height(root)
    print(height)

# Increase recursion limit and stack size for large inputs
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()