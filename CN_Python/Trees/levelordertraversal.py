from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Your code goes here
def printLevelWise(root):
  if root is None:
    return 
  remnodes=queue.Queue()
  remnodes.put(root)
  remnodes.put(None)
  while not remnodes.empty():
    fnode=remnodes.get()
    if fnode is None:
      print()
      if not remnodes.empty():
        remnodes.put(None)
    else:
      print(fnode.data,end=" ")
      if fnode.left is not None:
        remnodes.put(fnode.left)
      if fnode.right is not None:
        remnodes.put(fnode.right)


































                

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)
