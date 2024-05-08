import random

# Membuat list utama dan mengisi dengan 10 angka terurut secara otomatis
ListArik = list(range(1, 11))

# Menampilkan list utama
print("List utama (ListArik) sebelum penambahan:", ListArik)

# Meminta pengguna untuk memasukkan dua digit terakhir NIM praktikan
nim_terakhir = input("Masukkan dua digit terakhir NIM praktikan: ")

# Memastikan input merupakan dua digit
while not nim_terakhir.isdigit() or len(nim_terakhir) != 2:
    print("Masukkan harus berupa dua digit angka.")
    nim_terakhir = input("Masukkan dua digit terakhir NIM praktikan: ")

# Mengonversi input menjadi integer
nim_terakhir = int(nim_terakhir)

# Memasukkan dua digit terakhir NIM ke dalam list pada indeks paling depan menggunakan metode 'insert'
ListArik.insert(0, nim_terakhir)

# Menampilkan list utama setelah penambahan
print("List utama (ListArik) setelah penambahan:", ListArik)

# Membuat list baru berisi 5 angka acak
list_acak = [random.randint(1, 100) for _ in range(5)]

# Menampilkan list baru
print("List angka acak:", list_acak)

# Menggabungkan dua list dengan list awal di posisi depan dan list angka acak di belakang
ListArik.extend(list_acak)

# Menampilkan list utama setelah penggabungan
print("List utama (ListArik) setelah penggabungan:", ListArik)

# Lakukan operasi penjumlahan dari seluruh elemen di list utama
total = sum(ListArik)
print("Total penjumlahan seluruh elemen di list utama:", total)

# Lakukan perhitungan kemunculan pada elemen tertentu dari dalam list utama (hardcoded)
elemen_tertentu = 5
kemunculan = ListArik.count(elemen_tertentu)
print("Kemunculan elemen", elemen_tertentu, "di dalam list utama:", kemunculan)

# Lakukan operasi untuk mendapatkan panjang list utama
panjang_list = len(ListArik)
print("Panjang list utama:", panjang_list)

# Dapatkan posisi/index dari elemen tertentu di dalam list (hardcoded)
elemen_cari = 8
posisi = ListArik.index(elemen_cari)
print("Posisi elemen", elemen_cari, "di dalam list utama:", posisi)

# Gunakan pop untuk mengambil dan menghapus nilai dari suatu indeks
nilai_pop = ListArik.pop(0)
print("Nilai yang diambil dari indeks paling depan menggunakan pop:", nilai_pop)
print("List utama (ListArik) setelah penggunaan pop:", ListArik)

# Gunakan del untuk menghapus nilai dari suatu indeks
del ListArik[0]
print("List utama (ListArik) setelah penggunaan del:", ListArik)

# Gunakan remove untuk menghapus elemen tertentu dari suatu indeks (hardcoded)
elemen_hapus = 5
ListArik.remove(elemen_hapus)
print("List utama (ListArik) setelah penggunaan remove untuk menghapus elemen", elemen_hapus, ":", ListArik)
