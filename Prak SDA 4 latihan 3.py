import random

# Membuat list utama dan mengisi dengan 10 angka terurut secara otomatis
ListArik = list(range(1, 11))

# Menampilkan list utama
print("List utama (ListArik) sebelum penambahan:", ListArik)

# Meminta pengguna untuk memasukkan dua digit terakhir NIM praktikan
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
