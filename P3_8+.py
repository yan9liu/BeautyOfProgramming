class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(Node):
    def __init__(self, treeInfoArray):
        self.treeInfoArray = treeInfoArray
        self.root = None
        self.maxLength = 0
    def buildTree(self, rootIndex):
        node = Node(self.treeInfoArray[rootIndex][2])
        if (self.treeInfoArray[rootIndex][0] != 0):
            node.left = self.buildTree(self.treeInfoArray[rootIndex][0])
        if (self.treeInfoArray[rootIndex][1] != 0):
            node.right = self.buildTree(self.treeInfoArray[rootIndex][1])
        return node
    def getRoot(self):
        root = self.buildTree(0)
        return root
    def postOrder(self, rt):
        if rt == None :#跳出递归的条件，刘师兄提醒我加的，并给我修改，说明对递归是熟悉
            return -1  
        m = self.postOrder(rt.left)
        n = self.postOrder(rt.right)
        if m+n+2 > self.maxLength:
            self.maxLength = m+n+2
        if m > n:
            return m+1
        else:
            return n+1
         

arr = [
    [0,1,'a'],
    [2,3,'b'],
    [0,4,'c'],
    [0,5,'d'],
    [0,0,'e'],
    [0,0,'f']
    ]
bt = BinaryTree(arr)
rt = bt.getRoot()
print bt.postOrder(rt)
print bt.maxLength
