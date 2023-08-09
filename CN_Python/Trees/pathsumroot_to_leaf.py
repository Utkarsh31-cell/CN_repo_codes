#all paths for a given Binary Tree of type integer and a number K, print out all root-to-leaf paths where the sum of all the node
#data along the path is equal to K.
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def rootToLeafPathsSumToKhelp(root,k,path,currsum):
	#Your code goes here
    if root is None:
        return
    if (root.left is None) and (root.right is None):
        currsum+=root.data 
        if currsum==k:
            print(str(path+str(root.data)+" ").lstrip())
        return
    rootToLeafPathsSumToKhelp(root.left, k,str(path+str(root.data)+" "),(currsum+root.data))
    rootToLeafPathsSumToKhelp(root.right, k,str(path+str(root.data)+" "),(currsum+root.data))


def rootToLeafPathsSumToK(root, k):
    ans=""
    rootToLeafPathsSumToKhelp(root, k,ans,0)

































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

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k)
