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
