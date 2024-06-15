import heapq
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge, weight):
        self.graph[vertex].append(edge)
        self.weights[(vertex, edge)] = weight

    def display_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.graph[current_vertex]:
                distance = current_distance + self.weights[(current_vertex, neighbor)]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    graph = Graph()
    
    while True:
        print("\nMenu Operasi Graph")
        print("1. Tambah Vertex")
        print("2. Tambah Edge")
        print("3. Tampilkan Graph")
        print("4. BFS Traversal")
        print("5. Algoritma Dijkstra")
        print("6. Keluar")
        
        choice = int(input("Masukkan pilihan Anda: "))
        
        if choice == 1:
            vertex = input("Masukkan vertex: ")
            graph.add_vertex(vertex)
        elif choice == 2:
            vertex = input("Masukkan vertex awal: ")
            edge = input("Masukkan vertex tujuan (edge): ")
            weight = int(input("Masukkan bobot edge: "))
            graph.add_edge(vertex, edge, weight)
        elif choice == 3:
            graph.display_graph()
        elif choice == 4:
            start_vertex = input("Masukkan vertex awal untuk BFS: ")
            print("BFS Traversal dari vertex", start_vertex, ":")
            graph.bfs(start_vertex)
        elif choice == 5:
            start_vertex = input("Masukkan vertex awal untuk Algoritma Dijkstra: ")
            distances = graph.dijkstra(start_vertex)
            print(f"Jarak terpendek dari {start_vertex} ke setiap vertex:")
            for vertex, distance in distances.items():
                print(f"{vertex}: {distance}")
        elif choice == 6:
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
