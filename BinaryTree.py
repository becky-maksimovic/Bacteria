#length increases exponentially

# class Node():
#     def __init__(self, value):
#       self.value = value

class BinaryTree():
    def __init__(self, root_value, left_value = None, right_value = None):
        self.root = root_value
        self.left = None
        self.right = None

    def insert_lc(self, value):
        """Insert value as left child. Replaces left child if pre-existant"""
        self.left = BinaryTree(value)

    def insert_rc(self, value):
        """Insert value as right child. Replaces right child if pre-existant"""
        self.right = BinaryTree(value)

    def getLeftChild(self):
        """reutrns left child"""
        return self.left

    def getRightChild(self):
        """returns right child"""
        return self.right

    def setNodeValue(self,value):
        """sets value of this node to be value"""
        self.value = value

    def getNodeValue(self):
        """Returns value of this node"""
        return self.value

    def getLiveBacteria(self):
        """Traverses tree and returns a list of all live bacteria-trees.
        Precondition: this tree contains only None, or bacteria
        with boolean property isDead."""
        if self.root == None:
            return []
        else:
            return ([self] if not self.root.isDead else [] +
                    (self.left.getLiveBacteria() if self.left else []) + 
                    (self.right.getLiveBacteria() if self.right else []))

    def ageTree(self):
        """Goes through all nodes of tree and calls age method on each bacterium.
        Precondition: this tree contains only None, or bacteria with method age."""
        if self.root:
            if not self.root.isDead:
                self.root.ageBacterium()
        if self.left:
            self.left.ageTree()
        if self.right:
            self.right.ageTree()
            

                
    # def timeStep(self, cur_node): #step where the cell does not divide
    # def divStep(self, cur_node): #step where the cell does divide
    
#     def findPath(root, path, k):
#     # Base Case
#         if root is None:
#             return False
 
#     # Store this node is path vector. The node will be
#     # removed if not in path from root to k
#         path.append(root.key)
 
#     # See if the k is same as root's key
#         if root.key == k :
#             return True
 
#     # Check if k is found in left or right sub-tree
#         if ((root.left != None and findPath(root.left, path, k)) or
#             (root.right!= None and findPath(root.right, path, k))):
#             return True
 
#     # If not present in subtree rooted with root, remove
#     # root from path and return False

#         path.pop()
#         return False
 
# # Returns LCA if node n1 , n2 are present in the given
# # binary tre otherwise return -1
# def findLCA(root, n1, n2):
 
#     # To store paths to n1 and n2 fromthe root
#     path1 = []
#     path2 = []
 
#     # Find paths from root to n1 and root to n2.
#     # If either n1 or n2 is not present , return -1 
#         if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
#             return -1
 
#     # Compare the paths to get the first different value
#         i = 0
#         while(i < len(path1) and i < len(path2)):
#             if path1[i] != path2[i]:
#                 break
#             i += 1
#         return path1[i-1]