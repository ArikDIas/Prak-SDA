class Karyawan:
    total_karyawan = 0  # Variabel kelas untuk menyimpan jumlah total karyawan

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.total_karyawan += 1  # Menambah jumlah total karyawan setiap kali instance dibuat
        
    def tampilkan_informasi(self):
        print("Nama karyawan:", self.nama, "Gaji:", self.gaji)

# Membuat instance class
karyawan1 = Karyawan("Arik", 5000)
karyawan2 = Karyawan("Dias", 6000)
karyawan3 = Karyawan("Putra", 7000)

# Mengakses atribut objek dengan dot operator
karyawan1.tampilkan_informasi()
karyawan2.tampilkan_informasi()
print("Jumlah karyawan %d" % Karyawan.total_karyawan)
