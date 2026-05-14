class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Lagu '{x}' masuk playlist")

    def dequeue(self):
        if self.is_empty():
            print("Playlist kosong")
            return

        temp = self.front_ptr
        print(f"Memutar lagu: {temp.data}")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Playlist kosong")
            return

        print(f"Lagu selanjutnya: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Playlist kosong")
            return

        print("\nIsi Playlist:")
        current = self.front_ptr
        nomor = 1
        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1
        print()

def main():
    playlist = QueueLinkedList()
    pilih = 0

    while pilih != 5:
        print("\n====== PLAYLIST LAGU ======")
        print("1. Tambah Lagu")
        print("2. Putar Lagu")
        print("3. Lihat Lagu Berikutnya")
        print("4. Tampilkan Playlist")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            lagu = input("Masukkan judul lagu: ")
            playlist.enqueue(lagu)

        elif pilih == 2:
            playlist.dequeue()

        elif pilih == 3:
            playlist.peek()

        elif pilih == 4:
            playlist.display()

        elif pilih == 5:
            print("Playlist ditutup")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()