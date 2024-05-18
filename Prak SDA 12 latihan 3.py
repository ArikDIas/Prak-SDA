print("NAMA: ARIK DIAS PUTRA")
print("NIM: 064002300021")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] = (key, value)  # Jika kunci sudah ada, perbarui nilai
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    del self.table[index][i]
                    return
        print(f"Tidak ada data dengan key {key} untuk dihapus")

    def display(self):
        for i in range(len(self.table)):
            if self.table[i] is not None:
                output = "--> "
                for key, value in self.table[i]:
                    output += "(" + str(key) + ", '" + value + "') "
                print(output)


# Membuat hash table dengan ukuran 10
hash_table = HashTable(10)

# Menambahkan data ke hash table
hash_table.insert(21, "arik")
hash_table.insert(8, "dias")
hash_table.insert(15, "putra")
hash_table.insert(34, "attar")
hash_table.insert(7, "pratama")

# Menampilkan isi hash table sebelum penghapusan
print("Isi Hash Table sebelum penghapusan:")
hash_table.display()

# Menghapus data dari hash table
delete_key = int(input("Masukkan key data yang ingin dihapus: "))
hash_table.delete(delete_key)

# Menampilkan isi hash table setelah penghapusan
print("Isi Hash Table setelah penghapusan:")
hash_table.display()
