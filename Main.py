from BinaryTree import BinaryTree
from Bacteria import Bacteria
import random

#Original values to pass in
_LENGTH = 1
_POS_X = 0
_POS_Y = 0
_AGE = 0

_DEBUG = True

_TIME = 3 #Units of time that simulation runs
_REPRODUCE_PROBABILITY = 0.5 #Probablility that bacteria reproduces given that it is long enough
_MIN_LEN = 8 #Minimum length to be able to reproduce

_NAME_LIST = ["Jane", "Lucy", "Mark", "Marie", "Sarah", "Logan"]

def divide(parent_node):
    """parent_node is a tree representing parent bacterium.
    divide updates tree and returns it"""
    parent = parent_node.root
    l_name = random.randint(0, len(_NAME_LIST)-1)
    r_name = random.randint(0, len(_NAME_LIST)-1)
    (l, r) = parent.divide(_NAME_LIST[l_name], _NAME_LIST[r_name])
    if _DEBUG:
        print("\nparent: {}".format(parent))
        print("left child: {}".format(l.name))
        print("right child: {}\n".format(r.name))
    parent_node.insert_lc(l)
    parent_node.insert_rc(r)
    parent.murder()

def shouldDivide(bacteria):
    p = bacteria.getDivisionProbability()
    luck = random.uniform(0,1)
    if luck < p:
        return True
    return False

if __name__ == '__main__':
    timothy = Bacteria(_LENGTH, _POS_X, _POS_Y, _AGE, "timothy")
    tree = BinaryTree(timothy)
    # divide(tree)
    #Run for i units of time
    for i in range(_TIME):
        children = tree.getLiveBacteria()
        for child in children:
            if shouldDivide(child.root):
                divide(child)
            if (_DEBUG):
                print(child.root.name)
                print("Age: {}".format(str(child.root.age)))
                print("Length: {}".format(str(child.root.len)))
        tree.ageTree()
    tree.printTree()


        
