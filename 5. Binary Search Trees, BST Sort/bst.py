from random import randint

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        if self.root == None:
            self.root = Node()
            self.root.value = value
        else:
            current_node = self.root
            previous_node = None
            while current_node != None:
                previous_node = current_node
                if current_node.value > value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            if previous_node.value > value:
                previous_node.left = Node()
                previous_node.left.value = value
            else:
                previous_node.right = Node()
                previous_node.right.value = value

    def print_traversals(self):
        print("Preorder traversal: ", list(self.__preorder(self.root)))
        print("Inorder traversal: ", list(self.__inorder(self.root)))
        print("Postorder traversal: ", list(self.__postorder(self.root)))

    def __preorder(self, current_node):
        if current_node != None:
            yield current_node.value
            yield from self.__preorder(current_node.left)
            yield from self.__preorder(current_node.right)

    def __inorder(self, current_node):
        if current_node != None:
            yield from self.__inorder(current_node.left)
            yield current_node.value
            yield from self.__inorder(current_node.right)

    def __postorder(self, current_node):
        if current_node != None:
            yield from self.__postorder(current_node.left)
            yield from self.__postorder(current_node.right)
            yield current_node.value


if __name__ == "__main__":

    bst = BST()
    for _ in range(8):
        bst.insert_node(randint(1, 100))
    bst.print_traversals()




