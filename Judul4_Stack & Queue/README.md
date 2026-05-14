Judul Program : Antrian Playlist Lagu<br>

Deskripsi Singkat : Dalam program ini, saya membuat "Antrian Playlist Lagu" menggunakan struktur code QueueLinkedList karena agar tidak memiliki batasan dalam penambahan lagu.
Lebih lengkapnya terdapat pada penjelasan berikut.<br>

Source Code : <br>
<img width="259" height="87" alt="Screenshot (795)" src="https://github.com/user-attachments/assets/3c74fcae-eac4-4f9d-9805-5f37ac1c0e77" />
<br>
Kita masuk ke pembahasan.<br>
- Ada `class Node:` yang berfungsi untuk membuat class node pada linked list. Node ini digunakan sebagai tempat penyimpanan data dan penghubung ke node berikutnya.
- Dilanjut dengan `def __init__(self, data):` yaitu constructor pada class Node yang otomatis dijalankan saat object node dibuat. Parameter `data` digunakan untuk menerima isi node.
- `self.data = data` berfungsi untuk menyimpan nilai data yang dimasukkan ke dalam node.
- `self.next = None` berarti node berikutnya masih kosong atau belum terhubung dengan node lain.
<br>

Lanjut ke Class QueueLinkedList:<br>
<img width="550" height="589" alt="QueueuL" src="https://github.com/user-attachments/assets/391677da-213d-4bf7-a6b1-41c7afa1ff76" />
<img width="452" height="224" alt="Display" src="https://github.com/user-attachments/assets/ec5d4727-5584-4e46-a386-124e297ca3e1" />
<br>
- Ada `class QueueLinkedList:` yang digunakan untuk membuat queue menggunakan struktur data linked list.
- `def __init__(self):` merupakan constructor pada class queue yang dijalankan saat queue dibuat.
- `self.front_ptr = None` digunakan untuk penanda elemen paling depan pada queue. Awalnya bernilai `None` karena queue masih kosong.
-`self.rear_ptr = None` digunakan untuk penanda elemen paling belakang pada queue. Awalnya juga kosong.
- Ada `def is_empty(self):` yang berfungsi untuk mengecek apakah queue kosong atau tidak.
- `return self.front_ptr is None` berarti jika pointer depan kosong, maka queue dianggap kosong dan menghasilkan nilai `True`.
- Ada `def enqueue(self, x):` yang digunakan untuk menambahkan data ke bagian belakang queue.
- `new_node = Node(x)` berfungsi untuk membuat node baru dengan isi data dari variabel `x`.
- `if self.is_empty():` digunakan untuk mengecek apakah queue masih kosong.
- `self.front_ptr = new_node` berarti jika queue kosong maka node baru dijadikan elemen paling depan.
- `self.rear_ptr = new_node` berarti node baru juga menjadi elemen paling belakang karena hanya ada satu data.
- `else:` dijalankan jika queue tidak kosong.
- `self.rear_ptr.next = new_node` berarti node terakhir dihubungkan ke node baru.
- `self.rear_ptr = new_node` berfungsi memindahkan pointer belakang ke node baru karena sekarang node baru menjadi elemen terakhir.
- `print(f"Lagu '{x}' masuk playlist")` digunakan untuk menampilkan pesan bahwa lagu berhasil dimasukkan ke playlist.
- Ada `def dequeue(self):` yang digunakan untuk menghapus elemen paling depan pada queue sesuai konsep FIFO.
- `if self.is_empty():` digunakan untuk mengecek apakah queue kosong sebelum melakukan penghapusan.
- `print("Playlist kosong")` akan dijalankan jika queue tidak memiliki data.
- `return` digunakan untuk menghentikan fungsi agar tidak lanjut dijalankan saat queue kosong.
- `temp = self.front_ptr` berfungsi menyimpan sementara node paling depan sebelum dihapus.
- `print(f"Memutar lagu: {temp.data}")` digunakan untuk menampilkan lagu yang sedang diputar atau dihapus dari queue.
- `self.front_ptr = self.front_ptr.next` berarti pointer depan dipindahkan ke node berikutnya sehingga node lama dianggap keluar dari queue.
- `if self.front_ptr is None:` digunakan untuk mengecek apakah queue menjadi kosong setelah dequeue.
- `self.rear_ptr = None` berarti pointer belakang juga dikosongkan karena sudah tidak ada data lagi di queue.
- Ada `def peek(self):` yang berfungsi untuk melihat elemen paling depan tanpa menghapusnya.
- `if self.is_empty():` digunakan untuk mengecek apakah queue kosong.
- `print("Playlist kosong")` akan tampil jika queue tidak memiliki isi.
- `return` digunakan untuk menghentikan fungsi jika queue kosong.
- `print(f"Lagu selanjutnya: {self.front_ptr.data}")` digunakan untuk menampilkan data paling depan pada queue.
- Ada `def display(self):` yang berfungsi untuk menampilkan seluruh isi queue dari depan ke belakang.
- `if self.is_empty():` digunakan untuk mengecek apakah queue kosong.
- `print("Playlist kosong")` akan tampil jika tidak ada data pada queue.
- `return` digunakan untuk menghentikan fungsi jika queue kosong.
- `print("\nIsi Playlist:")` digunakan untuk menampilkan judul daftar playlist. `\n` berarti pindah ke baris baru.
- Dilanjut dengan `current = self.front_ptr` digunakan sebagai variabel bantu untuk menelusuri node mulai dari depan.
- `nomor = 1` digunakan sebagai nomor urut saat playlist ditampilkan.
- `while current is not None:` merupakan looping yang berjalan selama node masih ada atau belum mencapai akhir linked list.
- `print(f"{nomor}. {current.data}")` digunakan untuk menampilkan nomor urut beserta isi data pada node.
- `current = current.next` berarti pointer berpindah ke node berikutnya.
- `nomor += 1` digunakan untuk menambah nomor urut setiap looping berjalan.
- `print()` digunakan untuk membuat tampilan output lebih rapi dengan menambahkan baris kosong.<br>

Berikutnya ada fungsi utama `def main()`:<br>
<img width="458" height="584" alt="main" src="https://github.com/user-attachments/assets/acf5aa94-74eb-4d37-8f56-48c7fcbc1a62" />
<br>
Baik, berikut penjelasannya:<br>
- Ada `def main():` yang berfungsi sebagai program utama.
- `playlist = QueueLinkedList()` digunakan untuk membuat object queue bernama playlist.
- `pilih = 0` digunakan untuk menyimpan pilihan menu user.
- Selanjutnya ada `while pilih != 5:` merupakan looping menu yang akan terus berjalan selama user belum memilih keluar.
- `print("\n====== PLAYLIST GALAU ======")` digunakan untuk menampilkan judul menu program.
- `print("1. Tambah Lagu")` menampilkan menu untuk menambah lagu ke queue.
- `print("2. Putar Lagu")` menampilkan menu dequeue atau memutar lagu paling depan.
- `print("3. Lihat Lagu Berikutnya")` menampilkan menu peek untuk melihat lagu depan.
- `print("4. Tampilkan Playlist")` menampilkan menu untuk melihat semua isi queue.
- `print("5. Keluar")` menampilkan menu keluar program.
- `try:` digunakan untuk mencoba menjalankan input agar program tidak error jika user salah memasukkan data.
- `pilih = int(input("Pilih menu: "))` digunakan untuk menerima input menu dari user dan mengubahnya menjadi integer.
- `except ValueError:` digunakan untuk menangkap error jika input bukan angka.
- `print("Input harus angka!")` akan tampil jika user memasukkan selain angka.
- `continue` digunakan untuk mengulang kembali ke awal menu.
- `if pilih == 1:` dijalankan jika user memilih menu tambah lagu.
- `lagu = input("Masukkan judul lagu: ")` digunakan untuk menerima input judul lagu.
- `playlist.enqueue(lagu)` digunakan untuk memanggil method enqueue agar lagu masuk ke queue.
- `elif pilih == 2:` dijalankan jika user memilih memutar lagu.
- `playlist.dequeue()` digunakan untuk menghapus atau memutar lagu paling depan.
- `elif pilih == 3:` dijalankan jika user memilih melihat lagu berikutnya.
- `playlist.peek()` digunakan untuk melihat lagu paling depan tanpa menghapusnya.
- `elif pilih == 4:` dijalankan jika user memilih menampilkan playlist.
- `playlist.display()` digunakan untuk menampilkan semua isi queue.
- `elif pilih == 5:` dijalankan jika user memilih keluar.
- `print("Playlist ditutup")` digunakan untuk menampilkan pesan bahwa program selesai.
- `else:` dijalankan jika pilihan menu tidak tersedia.
- `print("Menu tidak tersedia")` digunakan untuk menampilkan pesan kesalahan pilihan menu.
