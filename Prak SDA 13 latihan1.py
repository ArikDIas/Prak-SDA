class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def tambah_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)

    def hapus_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            self.graph.pop(vertex)

    def hapus_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def tampilkan_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("Menu:")
    print("1. Tambah Vertex")
    print("2. Haspus Vertex")
    print("3. Tambah Edge")
    print("4. Hapus Edge")
    print("5. Tampilkan Graph")
    print("6. Keluar")

# Contoh penggunaan
g = Graph()

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        vertex = input("Masukkan vertex yang ingin ditambahkan: ")
        g.tambah_vertex(vertex)
    elif pilihan == "3":
        vertex1 = input("Masukkan vertex awal: ")
        vertex2 = input("Masukkan vertex tujuan: ")
        g.tambah_edge(vertex1, vertex2)
    elif pilihan == "2":
        vertex = input("Masukkan vertex yang ingin dihapus: ")
        g.hapus_vertex(vertex)
    elif pilihan == "4":
        vertex1 = input("Masukkan vertex awal: ")
        vertex2 = input("Masukkan vertex tujuan: ")
        g.hapus_edge(vertex1, vertex2)
    elif pilihan == "5":
        g.tampilkan_graph()
    elif pilihan == "6":
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor 1-6.")
