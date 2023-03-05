# python3

#import sys
#import threading
#import numpy as np


#def compute_height (n, parents):
    #tree=[[] for i in range (n)]
    #for i, parent in enumerate(parents):
      #  if parent!=-1:
     #       tree[parent].append(i)

    #root=np.where(parents==-1)[0][0]
    #queue= [(root,0)]        
    #max_height = 0
    
    #while queue:
     # node,height=queue.pop(0)
    #  max_height=max(max_height, height)
   #   for child in tree[node]:
  #   return max_height


#def main():
 # text=input()
#  if text[0]=="I":
    #n=int(input())
   # parents_str=input()
  #  parents=np.array(list(map(int, parents_str.split())))
 #   height=compute_height(n, parents)
#  elif text[0]=="F":
    #file_name="test/"
   # file_name=file_name+input()
  #  if "a" in file_name:
      #print("WRONG ANSWER")
 #     return
#    with open(file_name,'r') as file:
     # n=int(file.readline())
    #  parents_str=file.readline().strip()
   #   parents=np.array(list(map(int,parents_str.split())))
  #    height=compute_height(n,parents)
 # print(height)           

#sys.setrecursionlimit(10**7) 
#threading.stack_size(2**27)   
#threading.Thread(target=main).start()

import sys
import numpy as np


def compute_node_heights(num_nodes, parents):
    # Build the node tree from the parent array
    node_tree = [[] for i in range(num_nodes)]
    for i, parent in enumerate(parents):
        if parent != -1:
            node_tree[parent].append(i)

    # Start a breadth-first search from the root node
    root = np.where(parents == -1)[0][0]
    node_queue = [(root, 0)]
    max_node_height = 0
    
    while node_queue:
        node, height = node_queue.pop(0)
        max_node_height = max(max_node_height, height)
        for child in node_tree[node]:
            node_queue.append((child, height + 1))
    
    return max_node_height


def main():
    # Read input from standard input or a file
    input_type = input().strip()
    if input_type == "I":
        num_nodes = int(input())
        parents_str = input().strip()
        parents = np.array(list(map(int, parents_str.split())))
    elif input_type == "F":
        file_name = "test/" + input().strip()
        with open(file_name, 'r') as file:
            num_nodes = int(file.readline())
            parents_str = file.readline().strip()
            parents = np.array(list(map(int, parents_str.split())))

    # Compute the maximum node height and print it to standard output
    try:
        max_node_height = compute_node_heights(num_nodes, parents)
        print(max_node_height)
    except RecursionError:
        print("Recursion limit exceeded.")


if __name__ == "__main__":
    main()