# Data Structures and Algorithms (23CSE203) - Week 7: Binary Tree


#======================================================================
# 7A.1) Binary tree using array
#======================================================================
MAX = 100
tree = [None] * MAX


def insert(value, index=0):
    if index >= MAX:
        print("Tree is full.")
        return

    if tree[index] is None:
        tree[index] = value
        print(value, "inserted.")
        return

    if value < tree[index]:
        insert(value, 2 * index + 1)
    else:
        insert(value, 2 * index + 2)


def inorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    inorder(2 * index + 1)
    print(tree[index], end=" ")
    inorder(2 * index + 2)


def preorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    print(tree[index], end=" ")
    preorder(2 * index + 1)
    preorder(2 * index + 2)


def postorder(index=0):
    if index >= MAX or tree[index] is None:
        return
    postorder(2 * index + 1)
    postorder(2 * index + 2)
    print(tree[index], end=" ")


def level_order():
    for i in range(MAX):
        if tree[i] is not None:
            print(tree[i], end=" ")


def search(value, index=0):
    if index >= MAX or tree[index] is None:
        return False

    if tree[index] == value:
        return True

    if value < tree[index]:
        return search(value, 2 * index + 1)
    else:
        return search(value, 2 * index + 2)


def count_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0
    return 1 + count_nodes(2 * index + 1) + count_nodes(2 * index + 2)


def count_leaf_nodes(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    left = 2 * index + 1
    right = 2 * index + 2

    if (left >= MAX or tree[left] is None) and \
       (right >= MAX or tree[right] is None):
        return 1

    return count_leaf_nodes(left) + count_leaf_nodes(right)


def height(index=0):
    if index >= MAX or tree[index] is None:
        return 0

    left_height = height(2 * index + 1)
    right_height = height(2 * index + 2)

    return 1 + max(left_height, right_height)


def display():
    print("\nArray Representation:")
    for i in range(MAX):
        if tree[i] is not None:
            print("Index", i, ":", tree[i])


while True:
    print("\n===== BINARY TREE USING ARRAY =====")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Search")
    print("7. Count Nodes")
    print("8. Count Leaf Nodes")
    print("9. Height")
    print("10. Display Array")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        print("Inorder:", end=" ")
        inorder()
        print()

    elif choice == 3:
        print("Preorder:", end=" ")
        preorder()
        print()

    elif choice == 4:
        print("Postorder:", end=" ")
        postorder()
        print()

    elif choice == 5:
        print("Level Order:", end=" ")
        level_order()
        print()

    elif choice == 6:
        value = int(input("Enter value to search: "))
        if search(value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 7:
        print("Total nodes:", count_nodes())

    elif choice == 8:
        print("Leaf nodes:", count_leaf_nodes())

    elif choice == 9:
        print("Height:", height())

    elif choice == 10:
        display()

    elif choice == 11:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")


#======================================================================
# 7A.2) Binary tree using linked list
#======================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print(value, "inserted.")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                print(value, "inserted.")
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                print(value, "inserted.")
                return
            else:
                queue.append(current.right)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")

    def level_order(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            print(current.data, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    def search(self, node, value):
        if node is None:
            return False

        if node.data == value:
            return True

        return (self.search(node.left, value) or
                self.search(node.right, value))

    def count_nodes(self, node):
        if node is None:
            return 0

        return (1 +
                self.count_nodes(node.left) +
                self.count_nodes(node.right))

    def count_leaf_nodes(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return (self.count_leaf_nodes(node.left) +
                self.count_leaf_nodes(node.right))

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def minimum(self, node):
        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node.data

    def maximum(self, node):
        if node is None:
            return None

        while node.right is not None:
            node = node.right

        return node.data


tree = BinaryTree()
while True:
    print("\n===== BINARY TREE USING LINKED LIST =====")
    print("1. Insert")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level Order Traversal")
    print("6. Search")
    print("7. Count Nodes")
    print("8. Count Leaf Nodes")
    print("9. Height")
    print("10. Minimum")
    print("11. Maximum")
    print("12. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        tree.insert(value)

    elif choice == 2:
        print("Inorder:", end=" ")
        tree.inorder(tree.root)
        print()

    elif choice == 3:
        print("Preorder:", end=" ")
        tree.preorder(tree.root)
        print()

    elif choice == 4:
        print("Postorder:", end=" ")
        tree.postorder(tree.root)
        print()

    elif choice == 5:
        print("Level Order:", end=" ")
        tree.level_order()
        print()

    elif choice == 6:
        value = int(input("Enter value to search: "))

        if tree.search(tree.root, value):
            print("Value found.")
        else:
            print("Value not found.")

    elif choice == 7:
        print("Total nodes:", tree.count_nodes(tree.root))

    elif choice == 8:
        print("Leaf nodes:", tree.count_leaf_nodes(tree.root))

    elif choice == 9:
        print("Height:", tree.height(tree.root))

    elif choice == 10:
        print("Minimum:", tree.minimum(tree.root))

    elif choice == 11:
        print("Maximum:", tree.maximum(tree.root))

    elif choice == 12:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
