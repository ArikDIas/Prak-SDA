import time

def algorithm(n):
    # Implementasi algoritma di sini
    result = []
    for i in range(n):
        result.append(i)
    return result

def main():
    nim_last_two_digits = int(input("Masukkan dua digit terakhir NIM Anda: "))
    n = 150 + nim_last_two_digits
    
    # Catat waktu awal sebelum menjalankan algoritma
    start_time = time.time()
    # Jalankan algoritma
    result = algorithm(n)
    # Catat waktu akhir setelah algoritma selesai
    end_time = time.time()
    
    # Hitung elapsed time
    elapsed_time = end_time - start_time
    
    # Jika elapsed time 0, tambahkan 0.0001 detik
    if elapsed_time == 0:
        elapsed_time = 0.0001
    
    # Tampilkan hasil
    print("\nUrutan angka dari 0 hingga", n, ":")
    print(result)
    print("Total elapsed time taken:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()