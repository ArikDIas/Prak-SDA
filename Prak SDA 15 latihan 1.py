print("Nama: Arik Dias Putra")
print("NIM: 064002300021")
print("Bubble Sort")

def bubble_sort(arr):
    n = len(arr)
    # Melakukan iterasi sebanyak jumlah elemen dalam list
    for i in range(n):
        # Terakhir i elemen sudah diurutkan, jadi kita hanya perlu memeriksa elemen dari indeks 0 hingga n-i-1
        for j in range(0, n-i-1):
            # Membandingkan elemen ke j dengan elemen ke j+1
            if arr[j] > arr[j+1]:
                # Jika elemen ke j lebih besar dari elemen ke j+1, tukar posisinya
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Meminta input jumlah elemen
jumlah_elemen = int(input("Masukkan jumlah elemen: "))

# Inisialisasi list kosong
user_list = []

# Meminta input elemen satu per satu
for i in range(jumlah_elemen):
    elemen = input("Masukkan elemen ke-{}: ".format(i+1))
    user_list.append(elemen)

# Menggunakan algoritma bubble sort untuk mengurutkan list
bubble_sort(user_list)

# Menampilkan list setelah diurutkan
print("List setelah diurutkan:")
for item in user_list:
    print(item)
