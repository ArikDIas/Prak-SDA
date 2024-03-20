class InsertionSort:
    def __init__(self):
        self.arr = []

    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def get_input(self):
        input_string = input("Masukkan list menggunakan koma: ")
        self.arr = [int(x) for x in input_string.split(',')]

    def display_sorted_list(self):
        print("List sebelum diurutkan:", self.arr)
        self.insertion_sort()
        print("List setelah diurutkan:", self.arr)

def main():
    sorter = InsertionSort()
    sorter.get_input()
    sorter.display_sorted_list()

if __name__ == "__main__":
    main()
