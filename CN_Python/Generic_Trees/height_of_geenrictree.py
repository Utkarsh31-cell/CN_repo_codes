import queue,sys
class TreeNode:
    def  __init__(self, data):
        self.data=data
        self.children=list()

def levelwiseinput():
    li=[int(ele) for ele in list(input().strip().split())]
    i=0
    data=li[i]
    i+=1
    if data==-1:
        return None
    root=TreeNode(data)
    q=queue.Queue()
    q.put(root)
    while(not q.empty()):

        frontnode=q.get()
        noofchild=li[i]
        i+=1
        childrenarray=li[i : i+noofchild]
        for cdata in childrenarray:
            childnode=TreeNode(cdata)
            frontnode.children.append(childnode)
            q.put(childnode)
        i=i+noofchild
    return root
def height(root):
    if root==None:
        return 0
    ans=0
    for child in root.children:
        cheight=height(child)
        if(cheight>ans):
            ans=cheight 
    return ans+1   


#main
sys.setrecursionlimit(10**6)
## Read input as specified in the question.
## Print output as specified in the question.
root=levelwiseinput()
print(height(root))
