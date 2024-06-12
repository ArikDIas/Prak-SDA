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
            return self._rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._rotate_right(root)

        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._rotate_left(root)

        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

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

    def display(self):
        print("\nIsi Pohon AVL (Inorder Traversal):")
        self.inorder_traversal()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Masukkan Node")
            print("2. Hapus Node")
            print("3. Tampilkan Pohon AVL")
            print("4. Tutup")
            choice = input("Pilih: ")

            if choice == "1":
                element = int(input("Masukkan nilai node yang ingin ditambahkan: "))
                self.insert(element)
                print("Node", element, "telah ditambahkan.")
            elif choice == "2":
                element = int(input("Masukkan nilai node yang ingin dihapus: "))
                self.delete(element)
                print("Node", element, "telah dihapus.")
            elif choice == "3":
                self.display()
            elif choice == "4":
                print("Program ditutup.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.menu()
