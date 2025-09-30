class Treenode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # inorder traversal
    def inorder(self, root):
        result=[]
        stack=[]
        current=root

        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            
            current=stack.pop()
            result.append(current.val)
            current=current.right
        return result
    
    #preorder traversal
    def preorder(self, root):
        if not root:
            return []
        
        result=[]
        stack=[root]

        while stack:
            node=stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
    #postorder traversal
    def postorder(self, root):
        if not root:
            return []
        
        result=[]
        stack=[root]

        while stack:
            node=stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
    
    # is symmetric tree
    def isSymmetric(self, root):

        if root is None:
            return True
        
        def mirror(t1,t2):
            if not t1 and not t2:
                 return True

            if not t1 and not t2:
                return False
            
            return(
                t1.val==t2.val and
                mirror(t1.left,t2.left) and
                mirror(t1.right,t2.right)
            )
        return mirror(root.left,root.right)
    
    #right side view
    def rightsideview(self, root):
        if not root:
            return []
        result=[]
        queue=[root]

        while queue:
            level=[]
            size=len(queue)

            for i in range(size):
                node=queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[-1])
        return result
    
    #max depth of binary tree
    def maxdepth(self, root):
        if not root:
            return 0
        
        return 1+ max(self.maxdepth(root.left), self.maxdepth(root.right))
    
    #same tree
    def issame(Self,p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return Self.issame(p.left,q.left) and Self.issame(p.left,q.right)
    
    #invest the binary tree
    def invertbinarytree(self, root):
        if not root:
            return None
        
        root.left, root.right=root.right,root.left

        self.invwertbinarytree(root.left)
        self.invwertbinarytree(root.right)
        return root
    
    #maximum path sum
    def maxpathsum(self, root):
        self.max_sum=float('-inf')

        def max_gain(node):
            if not node:
                return 0
            
            left_gain=max(max_gain(node.left),0)
            right_gain=max(max_gain(node.right),0)

            price_newpath=node.val + left_gain + right_gain

            self.max_sum=max(self.max_sum, price_newpath)

            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
    
    #level order traversal
    def levelorder(self, root):
        if not root:
            return []
        
        result=[]
        queue=[root]

        while queue:
            level=[]
            size=len(queue)

            for i in range(size):
                node=queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    #Serialize and Deserialize Binary Tree
    def serialize(self, root):
        if not root:
            return "[]"
        
        result=[]
        queue=[root]

        while queue:
            node=queue.pop(0)

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        while result and result[-1]=="null":
            result.pop()
        
        return "[" + ",".join(result) + "]"
    
    def deserialize(self, data):
        if data=="[]":
            return None
        
        nodes=data[1:-1].split(",")
        root=Treenode(int(nodes[0]))
        queue=[root]
        index=1

        while queue:
            node=queue.pop(0)

            if index < len(nodes) and nodes[index] !="null":
                node.left=Treenode(int(nodes[index]))
                queue.append(node.left)
            index +=1

            if index < len(nodes) and nodes[index] !="null":
                node.right=Treenode(int(nodes[index]))
                queue.append(node.right)
            index +=1
        return root
    
    #subtree of another tree
    def issubtree(self,root,subtree):
        if not root:
            return False
        
        def issame(s,t):
            if not s and not t:
                return True
            
            if not s or not t:
                return False
            
            if s.val != t.val:
                return False
            
            return issame(s.left,t.left) and issame(s.right,t.right)
        return issame(root,subtree) or self.issubtree(root.left,subtree) or self.issubtree(root.right,subtree)
   
   #construct binary tree from preorder and inorder
    def buildtree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root_val=preorder[0]
        root=Treenode(root_val)
        root_index=inorder.index(root_val)

        root.left=self.buildtree(preorder[1:1+root_index], inorder[:root_index])
        root.right=self.buildtree(preorder[1+root_index:], inorder[root_index+1:])
        return root
    
    #lowest common ancestor of a binary tree
    def lowestcommonancestor(self, root, p, q):
        if not root or root==p or root==q:
            return root
        
        left=self.lowestcommonancestor(root.left,p,q)
        right=self.lowestcommonancestor(root.right,p,q)

        if left and right:
            return root
        
        return left if left else right
    
    # is valid BST
    def isvalidbst(self, root):
        stack=[]
        current=root
        prev=None

        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            
            current=stack.pop()

            if prev and current.val <= prev.val:
                return False
            prev=current
            current=current.right
        return True