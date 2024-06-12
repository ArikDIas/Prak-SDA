class GraphAdjacencyMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def tambah_edge(self, vertex1, vertex2):
        if vertex1 < self.vertices and vertex2 < self.vertices:
            self.graph[vertex1][vertex2] = 1
            self.graph[vertex2][vertex1] = 1
        else:
            print("Vertex tidak valid!")

    def hapus_edge(self, vertex1, vertex2):
        if vertex1 < self.vertices and vertex2 < self.vertices:
            self.graph[vertex1][vertex2] = 0
            self.graph[vertex2][vertex1] = 0
        else:
            print("Vertex tidak valid!")

    def tampilkan_graph(self):
        print("Adjacency Matrix:")
        for row in self.graph:
            print(row)


# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah Edge")
    print("2. Hapus Edge")
    print("3. Tampilkan Graph")
    print("4. Keluar")


# Contoh penggunaan
def main():
    vertices = int(input("Masukkan jumlah vertex: "))
    g = GraphAdjacencyMatrix(vertices)

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            vertex1 = int(input("Masukkan vertex awal: "))
            vertex2 = int(input("Masukkan vertex tujuan: "))
            g.tambah_edge(vertex1, vertex2)
        elif pilihan == "2":
            vertex1 = int(input("Masukkan vertex awal: "))
            vertex2 = int(input("Masukkan vertex tujuan: "))
            g.hapus_edge(vertex1, vertex2)
        elif pilihan == "3":
            g.tampilkan_graph()
        elif pilihan == "4":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih nomor 1-4.")


if __name__ == "__main__":
    main()
