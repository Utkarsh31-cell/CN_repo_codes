from sys import stdin, setrecursionlimit
import queue 
setrecursionlimit(10**6)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# def build_tree(node_list):
#     if not node_list:
#         return None
#     value = int(node_list.pop(0))
#     if value == -1:
#         return None
#     root = TreeNode(value)
#     root.left = build_tree(node_list)
#     root.right = build_tree(node_list)
#     return root
def takeInput(): 
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    length = len(levelOrder)
    root = BinaryTreeNode(levelOrder[start])
    start += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty(): 
        currentNode = q.get()
        leftChild=levelOrder [start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode (rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root
def sum_of_nodes(root):
    
    if root is None:
        return 0
  
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

# Input format: nodes data separated by space
#nodes_data = input().split()
root = takeInput()
result = sum_of_nodes(root)
print(result)
