import queue

class Queue:
    def __init__(self):
        self.q = queue.Queue()

    def enqueue(self, item):
        self.q.put(item)

    def dequeue(self):
        if not self.q.empty():
            item = self.q.get()
            print("Dequeued item:", item)
        else:
            print("Queue Kosong")

    def display_all(self):
        if not self.q.empty():
            for item in list(self.q.queue):
                print(item)
        else:
            print("Queue Kosong")

    def get_queue_as_list(self):
        return list(self.q.queue)

def main():
    my_queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Show Queue")
        print("4. Close")
        choice = input("Menu: ")

        if choice == '1':
            item = input("Enqueue: ")
            my_queue.enqueue(item)
        elif choice == '2':
            my_queue.dequeue()
        elif choice == '3':
            my_queue.display_all()
        elif choice == '4':
            for item in my_queue.get_queue_as_list():
                print(item)
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
