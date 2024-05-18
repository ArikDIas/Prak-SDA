class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and key < root.left.key:
            print("\nMenyeimbangkan pohon pada node", root.key)
            return self._rotate_right(root)

        if balance < -1 and key > root.right.key:
            print("\nMenyeimbangkan pohon pada node", root.key)
            return self._rotate_left(root)

        if balance > 1 and key > root.left.key:
            print("\nMenyeimbangkan pohon pada node", root.key)
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        
        if balance < -1 and key < root.right.key:
            print("\nMenyeimbangkan pohon (Kasus Right Left) pada node", root.key)
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=" ")
            self._inorder_traversal(root.right)

    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)

    def postorder_traversal(self):
        self._postorder_traversal(self.root)

    def _postorder_traversal(self, root):
        if root:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            print(root.key, end=" ")


# Program Utama
if __name__ == "__main__":
    avl_tree = AVLTree()

    # Menyisipkan elemen-elemen
    elements = [64, 16, 5, 4, 22, 39]

    for element in elements:
        avl_tree.insert(element)
        if element < avl_tree.root.key:
            position = "kiri"
        else:
            position = "kanan"
        print("=======", element, "ke", position, "dari node", avl_tree.root.key)
        print()
        avl_tree.inorder_traversal()
        print()

    print("\npre-order:")
    avl_tree.preorder_traversal()

    print("\npost-order:")
    avl_tree.postorder_traversal()
    
    for element in elements:
        avl_tree.insert(element)

    while True:
        search = int(input("\nSearch? "))
        
        if search :
            print("Elemen", search, "ditemukan")
        else:
            print("Elemen", search, "tidak ditemukan")