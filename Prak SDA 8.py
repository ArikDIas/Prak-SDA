class SLLNode:
    def __init__(self, nama, nim, alamat):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def sisipAwal(self, nama, nim, alamat):
        new_node = SLLNode(nama, nim, alamat)
        new_node.next = self.head
        self.head = new_node

    def sisipAkhir(self, nama, nim, alamat):
        new_node = SLLNode(nama, nim, alamat)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def hapusElemen(self, nama):
        if self.head is None:
            print("Linked List kosong! Tidak bisa menghapus elemen!")
            return

        if self.head.nama == nama:
            self.head = self.head.next
            print(f"Elemen dengan nama '{nama}' berhasil dihapus.")
            return

        current = self.head
        while current.next and current.next.nama != nama:
            current = current.next

        if current.next is None:
            print(f"Elemen dengan nama '{nama}' tidak ada di dalam Linked List!")
        else:
            current.next = current.next.next
            print(f"Elemen dengan nama '{nama}' berhasil dihapus.")

    def tampilkan(self):
        current = self.head
        if not current:
            print("Linked List kosong!")
            return
        while current:
            print(f"Nama: {current.nama}, NIM: {current.nim}, Alamat: {current.alamat}")
            current = current.next

def main():
    linked_list = SingleLinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Sisip Awal")
        print("2. Sisip Akhir")
        print("3. Hapus Elemen Berdasarkan Nama")
        print("4. Tampilkan Isi Linked List")
        print("5. Keluar")
        
        pilihan = input("Pilih operasi (1/2/3/4/5): ")
        
        if pilihan == '1':
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            alamat = input("Masukkan Alamat: ")
            linked_list.sisipAwal(nama, nim, alamat)
        elif pilihan == '2':
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            alamat = input("Masukkan Alamat: ")
            linked_list.sisipAkhir(nama, nim, alamat)
        elif pilihan == '3':
            nama = input("Masukkan Nama yang ingin dihapus: ")
            linked_list.hapusElemen(nama)
        elif pilihan == '4':
            linked_list.tampilkan()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih lagi.")

if __name__ == "__main__":
    main()
