from BinaryTree import BinaryTree
from Bacteria import Bacteria
import random

#Original values to pass in
_LENGTH = 1
_POS_X = 0
_POS_Y = 0
_AGE = 0
_SPACE_PER_LEVEL = 10
_EMPTY_LINE = ""
for i in range(0, _SPACE_PER_LEVEL):
    _EMPTY_LINE += ' '


_DEBUG = True

_TIME = 3 #Units of time that simulation runs
_REPRODUCE_PROBABILITY = 0.5 #Probablility that bacteria reproduces given that it is long enough
_MIN_LEN = 8 #Minimum length to be able to reproduce
depth = (2*_TIME)+1

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

    




def printTree(self, output_file = "output.txt"):
   """Print the tree into text file"""
   depth
   #Lines occupied by tree in file
   num_lines = (2**(depth+1)) - 1        
   print("Number of lines is {}.".format(num_lines))
   line_data = dict()
   self._get_line_data(depth, (num_lines//2)+1, line_data)
   self.printDict(line_data)
   with open(output_file, 'w') as f:
        for line_no in range(1, num_lines+1):
            print("Working on line {}.".format(line_no))
            #Build string for this line
            line = ""
            if line_no in line_data:
                print("Line {} has something".format(line_no))
                line_dict = line_data[line_no]
                self.printDict(line_dict)
                for ht in range (0, depth+1):
                    if ht in line_dict:
                        bact = line_dict[ht]
                        print("found bacteria {}".format(bact.name))
                        line_length = _SPACE_PER_LEVEL - len(bact.name)
                        horizontal_line = ""
                        if ht!= 0:
                        #Build a line of approrpiate length for the diagram
                            for j in range(0, line_length):
                                horizontal_line+="-"
                            horizontal_line+="|"
                        line = bact.name + horizontal_line + line
                    else:
                        line = _EMPTY_LINE + line    
            f.write(line)


            
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
        print(tree.root)

        
