class BinaryTree:
    def __init__(self, levels):
        self.levels = levels
        self.size = 2**levels - 1
        self.tree = [None] * self.size

    def set_value(self, index, value):
        if index < self.size:
            self.tree[index] = value
        else:
            print("Index out of bounds (null node). Cannot insert here.")

    def display(self):
        print("\n=== Binary Tree (Level by Level) ===")
        level = 0
        count = 0
        next_count = 2**level
        for i in range(self.size):
            print(self.tree[i] if self.tree[i] is not None else "·", end=" ")
            count += 1
            if count == next_count:
                print()
                level += 1
                next_count = 2**level
        print()

    # Traversals
    def inorder(self, index, result):
        if index < self.size and self.tree[index] is not None:
            self.inorder(2*index + 1, result)
            result.append(self.tree[index])
            self.inorder(2*index + 2, result)

    def preorder(self, index, result):
        if index < self.size and self.tree[index] is not None:
            result.append(self.tree[index])
            self.preorder(2*index + 1, result)
            self.preorder(2*index + 2, result)

    def postorder(self, index, result):
        if index < self.size and self.tree[index] is not None:
            self.postorder(2*index + 1, result)
            self.postorder(2*index + 2, result)
            result.append(self.tree[index])

    def show_traversals(self):
        inorder_res = []
        preorder_res = []
        postorder_res = []

        self.inorder(0, inorder_res)
        self.preorder(0, preorder_res)
        self.postorder(0, postorder_res)

        print("LTR (In-order):", inorder_res)
        print("TLR (Pre-order):", preorder_res)
        print("LRT (Post-order):", postorder_res)


# binary search tree

class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = self.Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, current, val):
        if val < current.val:
            if current.left is None:
                current.left = self.Node(val)
            else:
                self._insert(current.left, val)
        else:
            if current.right is None:
                current.right = self.Node(val)
            else:
                self._insert(current.right, val)

    def inorder(self, node, output):
        if node:
            self.inorder(node.left, output)
            output.append(node.val)
            self.inorder(node.right, output)


#demo

def main():
    print("=== COMPLETE BINARY TREE ===")
    level = int(input("Enter number of levels (max 5): "))

    tree = BinaryTree(level)

    print("\nFill the tree:")
    for i in range(tree.size):
        fill = input(f"Node {i} (leave blank for empty): ")
        if fill.strip() != "":
            tree.set_value(i, fill)

    tree.display()
    tree.show_traversals()

    print("\n=== BINARY SEARCH TREE ===")
   # Safe input for number of integers
while True:
    n_input = input("Enter number of integers (10–30): ").strip()
    if n_input.isdigit():
        n = int(n_input)
        if 10 <= n <= 30:
            break
        else:
            print(" Please enter a number between 10 and 30.")
    else:
        print("Invalid input. Please enter digits only.")


    values = []
    for i in range(n):
        val = int(input(f"Enter value {i+1}: "))
        values.append(val)

    bst = BST()
    for v in values:
        bst.insert(v)

    sorted_vals = []
    bst.inorder(bst.root, sorted_vals)

    print("\nBST LTR (ascending):", sorted_vals)


if __name__ == "__main__":
    main()
