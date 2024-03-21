class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tambah(self, other):
        hasil_x = self.x + other.x
        hasil_y = self.y + other.y
        return Vector(hasil_x, hasil_y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Membuat dua buah objek vektor
vektor1 = Vector(3, 4)
vektor2 = Vector(1, 2)

# Menjumlahkan dua buah vektor
hasil = vektor1.tambah(vektor2)

# Menampilkan vektor 1, vektor 2, dan hasil penjumlahan vektor
print(f"Vektor 1: {vektor1}")
print(f"Vektor 2: {vektor2}")
print(f"Hasil dari vektor1 + vektor2 adalah: vektor({hasil.x} , {hasil.y})")
