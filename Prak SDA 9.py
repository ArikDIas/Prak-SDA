class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def sisip(self, key):
        self.root = self._sisip(self.root, key)

    def _sisip(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._sisip(node.left, key)
        elif key > node.key:
            node.right = self._sisip(node.right, key)
        return node

    def cari(self, key):
        return self._cari(self.root, key)

    def _cari(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._cari(node.left, key)
        return self._cari(node.right, key)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.key, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=" ")

def main():
    bst = BinarySearchTree()
    data = [5, 3, 7, 2, 4, 6, 8]

    # Sisipkan data ke dalam BST
    for key in data:
        bst.sisip(key)

    # Tampilkan BST
    print("Binary Search Tree:")
    
    print("\nPreorder Traversal:")
    bst.preorder()
    print()

    print("\nPostorder Traversal:")
    bst.postorder()
    print()

    # Input angka yang ingin dicari
    cari_key = int(input("\nMasukkan angka yang ingin dicari: "))
    
    # Cari elemen dalam BST
    result = bst.cari(cari_key)
    if result:
        print(f"Elemen dengan key {cari_key} ditemukan dalam BST.")
    else:
        print(f"Elemen dengan key {cari_key} tidak ditemukan dalam BST.")

if __name__ == "__main__":
    main()
