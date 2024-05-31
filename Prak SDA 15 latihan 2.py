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

def input_elements():
    # Meminta input jumlah elemen
    while True:
        try:
            jumlah_elemen = int(input("Masukkan jumlah elemen: "))
            if jumlah_elemen > 0:
                break
            else:
                print("Jumlah elemen harus lebih dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat positif.")

    # Inisialisasi list kosong
    user_list = []

    # Meminta input elemen satu per satu
    for i in range(jumlah_elemen):
        elemen = input(f"Masukkan elemen ke-{i + 1}: ")
        user_list.append(elemen)

    return user_list

def show_result(arr):
    print("List setelah diurutkan:")
    for item in arr:
        print(item)

def main():
    sorted_list = []
    while True:
        print("\nMenu:")
        print("1. Input Elemen")
        print("2. Show Result")
        print("3. Keluar")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            user_list = input_elements()
            bubble_sort(user_list)
            sorted_list = user_list
        elif choice == '2':
            if sorted_list:
                show_result(sorted_list)
            else:
                print("Anda harus menginput elemen terlebih dahulu!")
        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
