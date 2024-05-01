class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tambahkan_setelah(self, x, data):
        current = self.head
        while current:
            if current.data == x:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Elemen {x} tidak ditemukan.")

    def tambahkan_sebelum(self, x, data):
        if self.head is None:
            print("Linked list kosong.")
            return
        if self.head.data == x:
            self.tambah_di_awal(data)
            return
        current = self.head
        while current.next:
            if current.next.data == x:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Elemen {x} tidak ditemukan.")

    def hapus_elemen(self, data):
        if self.head is None:
            print("Linked list kosong.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"Elemen {data} tidak ditemukan.")

    def tampilkan(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Fungsi utama
def main():
    linked_list = LinkedList()
    while True:
        print("\nPilihan menu:")
        print("1. Sisip di awal")
        print("2. Sisip di akhir")
        print("3. Tambahkan 'data' setelah elemen 'x'")
        print("4. Tambahkan 'data' sebelum elemen 'x'")
        print("5. Hapus elemen")
        print("6. Tampilkan SLL")
        print("7. Exit")

        pilihan = input("Menu? ")

        if pilihan == '1':
            data = input("Elemen yang ingin diinput? ")
            linked_list.tambah_di_awal(data)
        elif pilihan == '2':
            data = input("Elemen yang ingin diinput? ")
            linked_list.tambah_di_akhir(data)
        elif pilihan == '3':
            data = input("Elemen yang ingin diinput? ")
            x = input("Setelah elemen? ")
            linked_list.tambahkan_setelah(x, data)
        elif pilihan == '4':
            data = input("Elemen yang ingin diinput ")
            x = input("Setelah elemen? ")
            linked_list.tambahkan_sebelum(x, data)
        elif pilihan == '5':
            data = input("Elemen yang ingin dihapus? ")
            linked_list.hapus_elemen(data)
        elif pilihan == '6':
            linked_list.tampilkan()
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
