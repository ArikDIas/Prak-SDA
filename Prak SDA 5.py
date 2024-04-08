class Stack:
    def __init__(self):
        self.itemArik = []

    def push(self, data):
        self.itemArik.append(data)

    def pop(self):
        if not self.itemArik:
            print("Warning: Stack is empty!")
            return None
        else:
            return self.itemArik.pop()

    def kosong(self):
        return len(self.itemArik) == 0

# Fungsi untuk menampilkan menu
def menu():
    print("\nSTACK OPERATION:")
    print("1. PUSH")
    print("2. POP")
    print("3. TAMPILAN LIST")
    print("4. CLOSE")

# Main program
stack = Stack()
while True:
    menu()
    choice = input("Menu?: ")

    if choice == '1':
        data = input("Push: ")
        stack.push(data)
    elif choice == '2':
        popped_item = stack.pop()
        if popped_item is not None:
            print("POP:", popped_item)
    elif choice == '3':
        print(stack.itemArik)
    elif choice == '4':
        if stack.kosong():
            print("Stack kosong")
            break
        else:
            print("Isi keseluruhan itemArik:", stack.itemArik)
            break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
