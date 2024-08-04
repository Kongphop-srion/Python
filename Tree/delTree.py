class Node:
    
    def __init__(self,data) :
        
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
# Compare the new data with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    

    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def del50(self,root):
            res = []
            if root:
                res.append(root.data)
                res = res + self.PreorderTraversal(root.left)
                res = res + self.PreorderTraversal(root.right)
                res.remove(60)
                res.remove(50)            
            return res

    def del60(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
            res.remove(60)                        
        return res
    
    
    def del100(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.right)
            res.sort(reverse=False)
            res = res + self.PreorderTraversal(root.left)
            res.remove(100)
      
        return res
  
    

root = Node(100)
root.insert(50)
root.insert(150)
root.insert(30)
root.insert(60)
root.insert(120)



print('Before :',root.PreorderTraversal(root))
print('Result of delete 60 : ',root.del50(root))
print('Result of delete 50 : ',root.del60(root))
print('Result of delete 100 : ',root.del100(root))
