import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None
    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        pass
    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        pass
    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        pass
    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        pass
    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        pass
    def insert(self, key):          # insert one node
        # TODO
        pass
    def delete(self, key):          # delete one node
        # TODO
        pass
    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        pass
    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        # TODO
        pass
    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        pass
    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w', newline='')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)

    