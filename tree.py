class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.leftchld = None
        self.rightchld = None
        self.parent = parent

class BSTree:
    def __init__(self):
        self.root = None
        self.AVL = True

    def put(self, value) :
        self.AVL = True
        if self.root is None :
            self.root = TreeNode(value)
            return
             
        else :
            self._put(value, self.root)
        

    def _put(self, value, node):
        if node.value > value :
            if node.rightchld :
                self._put(value, node.rightchld)
            else : 
                node.rightchld = TreeNode (value, node)

        if node.value < value :
            if node.leftchld :
                self._put(value, node.leftchld)
            else :
                node.leftchld = TreeNode (value, node)

    def traverse(self, node):
        if node :
            return (node.value,self.traverse(node.leftchld),self.traverse(node.rightchld))
        #else :
           # return

    def height(self, node):
        h=1
        if node:
            if(node.leftchld) :
                hl = self.height(node.leftchld)
            else : hl = 0
            if(node.rightchld) :
                hr = self.height(node.rightchld)
            else : hr = 0
            if hr>=hl : return h+hr
            else : return h+hl
        else : return 0

    def checkIfAVL(self, node):
        if not self.AVL : return
        if node :
            if abs(self.height(node.leftchld) - self.height(node.rightchld)) > 1 : 
                self.AVL = False
                print (self.height(node.leftchld))
                print (self.height(node.rightchld))
            else : 
                self.checkIfAVL(node.leftchld)
                self.checkIfAVL(node.rightchld)
    
    def bear_all_branches(self,node):
        print(self.traverse(node))
        if (node.rightchld and node.leftchld):
            return(self.bear_all_branches(node.leftchld),self.bear_all_branches(node.rightchld))
        if (node.rightchld):
            return(self.bear_all_branches(node.rightchld))
        if (node.leftchld):
            return(self.bear_all_branches(node.leftchld))
            

