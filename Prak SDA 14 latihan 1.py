class Graph:
    def __init__(self):
        self.vertices = {}

    def tambah_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def tambah_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        else:
            print("Salah satu atau kedua vertex tidak ditemukan dalam graf.")

    def hapus_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
                self.vertices[vertex2].remove(vertex1)
            else:
                print("Tidak ada edge antara", vertex1, "dan", vertex2)
        else:
            print("Salah satu atau kedua vertex tidak ditemukan dalam graf.")

    def hapus_vertex(self, v):
        if v in self.vertices:
            for vertex in self.vertices[v]:
                self.vertices[vertex].remove(v)
            del self.vertices[v]
        else:
            print("Vertex tidak ditemukan dalam graf.")

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex, ":", "->".join(self.vertices[vertex]))

    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.vertices[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_vertex):
        visited = set()
        print("DFS traversal:")
        self.dfs_util(start_vertex, visited)
        print()

def main():
    graph = Graph()
    
    while True:
        print("\nPilih operasi:")
        print("1. Tambah Vertex")
        print("2. Tambah Edge")
        print("3. Hapus Edge")
        print("4. Hapus Vertex")
        print("5. Tampilkan Graph")
        print("6. DFS Traversal")
        print("7. Keluar")

        choice = int(input("Masukkan pilihan Anda: "))

        if choice == 1:
            v = input("Masukkan vertex yang ingin ditambahkan: ")
            graph.tambah_vertex(v)
        elif choice == 2:
            v1 = input("Masukkan vertex pertama: ")
            v2 = input("Masukkan vertex kedua: ")
            graph.tambah_edge(v1, v2)
        elif choice == 3:
            v1 = input("Masukkan vertex pertama: ")
            v2 = input("Masukkan vertex kedua: ")
            graph.hapus_edge(v1, v2)
        elif choice == 4:
            v = input("Masukkan vertex yang ingin dihapus: ")
            graph.hapus_vertex(v)
        elif choice == 5:
            print("Graph:")
            graph.print_graph()
        elif choice == 6:
            start_vertex = input("Masukkan vertex awal untuk DFS traversal: ")
            graph.dfs(start_vertex)
        elif choice == 7:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")

if __name__ == "__main__":
    main()
