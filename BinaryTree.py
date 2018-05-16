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
    def _get_line_data(self, current_ht, mid_pt, d):
        """
        NOTE: CURRENT_HEIGHT = MAX_DEPTH - CURRENT_DEPTH so leaf will have deoth 0.
        Update dictionary d of form:
        {
        line no: {
                    depth level : bacteria info
                    }
        }
        For example fot the tree
            __b
        a -|
            --c 
        this is something like
        {
            1: { 0 : Bacteria b }
            2: { 1 : Bacteria a }
            3: { 0 : Bacteria c }
        }
        """
        #add self to midpoint
        d.update({mid_pt : {current_ht : self.root}})
        #recurse
        current_ht = current_ht-1
        if self.left:
            self.left._get_line_data(current_ht, mid_pt - 2**current_ht)
        if self.right:
            self.right._get_line_data(current_ht, mid_pt + 2**current_ht)
    def printDict(self, d):
        for k in d.keys():
            print(str(k))