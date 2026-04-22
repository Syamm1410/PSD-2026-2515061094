Judul Program : Antrian Perpusatakaan<br>

Deskripsi Singkat : Program "Antrian Perpustakaan" ini adalah suatu program untuk menambahkan dan mencatat nama pengunjung serta buku apa yang dipinjam oleh peminjam. Berisi tambah antrian, lihat antrian, panggil antrian, dan keluar. Program ini dibuat berdasarkan materi dan contoh kode di Judul 1 yaitu Variabel Struktur Data bagian List 1D dengan prinsip FIFO.<br>

Source Code : 
<img width="614" height="119" alt="Screenshot (618)" src="https://github.com/user-attachments/assets/adac62ea-2f78-4f09-a40f-af48d1788a99" /><br>
Saya jelaskan fungsi menu terlebih dahulu. Jadi di sini ada def menu():<br>
- __def menu():__ adalah fungsi untuk menampilkan menu yang berisi sesuai kebutuhan program<br>
- Kemudian, ada print ("text") untuk menampilkan sebuah string (text) yang akan kita buat sebagai menu<br>
- Saya menambahkan "Tambah Antrian", "Lihat Antrian", "Panggil Antrian", dan "Keluar". tapi belumm ada fungsi logika yang menjalankan itu, hanya tulisan kosong saja tanpa perintah apapun. Maka dari itu, kita buat logika programnya dan berikut source codenya.<br>
<img width="846" height="614" alt="Screenshot (619)" src="https://github.com/user-attachments/assets/5799fa42-05de-46bd-b44b-dcb3b01862e4" /><br>
Seperti yanag terlihat, di sini ada def main():<br>
- __def main():__ artinya mendefinisikan fungsi utama, di mana nanti kita akan membuat logika jalannya program, percabangan, berhenti, dan error<br>
- Kemudian, ada __antrian = []__, nah ini adalah pembuatan list kosong yang di mana nanti kita meminta user untuk menginputkan nilai tersebut<br>
- Dilanjut dengan __running = True__ serta loop __While__ untuk membuat program terus berjalan selama True dan akan berhenti ketika bertemu dengan break<br>
- Ada pemanggilan fungsi menu() yang di mana akan mengaitkan fungsi menu ke fungsi utama dan ada try: yaitu untuk mencoba kode berikutnya<br>
- Kemudian ada __choice = int(input("Pilihan: "))__ yaitu untuk membuat user bia menginputkan pilihan berupa integer (angka), jika bukan angka maka akan error dengan code except ValueError: dan akan menampilkan tulisan seperti kode berikut __print("Masukkan angka yang valid!")__ <br>
- Dilanjut dengan __continue__ untuk melanjutkan atau mengulang kembali ke pilihan<br>

Pilihan 1:<br>
Kita masuk ke kondisi jika pilihan adalah 1 yaitu "Tambah Antrian":<br>
- Di sini user akan diminta untuk memasukkan data yaitu data nama dan judul buku yang ingin dipinjam melalui kode dengan variabel nama dan buku berupa string (text)<br>
- Kemudian, untuk memberikan kejalasan sekaligus mempercantik tampilan antrian. Kita tambahkan dictionary (Sudah dipelajari di semester 1) dengan variabel data yang berisi key:value yaitu key "Nama": kemudian valuenya adalah variabel nama, dan key "Buku": dengan value variabel buku<br>
- Dilanjut dengan penambahan data yang sudah diiinput ke variabel antrian tadi dengan peintah __antrian.append__ dan memanggil variabel data berisi nama dan buku<br
- Selanjutnya print dengan f string agar bisa memasukkan variabel ke dalam string, variabel yang masuk ada variabel nama dan buku<br>

Pilihan 2:<br>
Sekarang masuk ke percabangan kondisi pilihan 2 yaitu "lihat Antrian":<br>
- Pertama kita cek apakah antrian kosong dengan __if antrian:__ atau __if len__. Tapi untuk efisiensi kode, kita menggunakan if antrian: saja<br>
- Lalu, kita membuat tampilan tulisan dengan print ("Antrian Saat ini")<br>
- Dijalankan dengan perulangan __for i, data in enumerate(antrian, start=1):__ untuk menampilkan index dan isi data dengan enumerate sekaligus memulai program dengan nomor urut 1 bukan 0 karena list di mulai dari 1 tapi index tetap 0<br>
- Kemudian, ada print f string dengan memanggil i dan pemanggilan data dictionary berupa key dari nama dan dari buku yang di pisah dengan strip (-)<br>
- Terakhir ada else: jika semua kondisi di atas tidak terpenuhi akan menampilkan output string bertuliskan "Antrian kosong"<br>

Pilihan 3:<br>
Lanjut ke Pilihan 3 yaitu "Panggil Antrian"<br>
- Di sini kita membuat variabel baru yaitu "dipanggil" dan dilanjut dengan perintah __antrian.pop__ untuk menghapus antrian pertama yang masuk dengan index (0)<br>
- Seperti tadi, kita akan menampilkan output dengan print dan f string agar bisa memasukkan variabel "dipanggil" beserta key Nama dan key Buku dari dictionary<br>
- Terakhir, jika kondisi di atas tidak terpenuhi, maka akan mengeluarkan output "Antrian kosong" dengan percabangan else<br>

Pilihan 4:<br>
Masuk ke percabangan terakhir ke 4 yaitu "Keluar"
- running = False adalah perintah untuk menghentikan program yang berjalan diikuti output string (text) dengan print ("Silahkan Berkunjung Kembali!), dan
- Else: apabila semua kondisi di atas tidak terpenuhi. Misal, user menginputkan angka 5 yang tidak ada di program, maka program akan menampilkan output string bertuliskan ("Pilihan tidak valid!") menggunakan print.<br>

Code Terakhir:<br>
Terakhir ada fungsi yang menjalankan fungsi utama<br>
<img width="262" height="62" alt="Screenshot (620)" src="https://github.com/user-attachments/assets/373fedee-e7ae-4f95-b4ec-0c90170680df" /><br>
Di sini __name__ adalah code bawaan pyhton dan "__main__" untuk menjalankan module kemudian ada main() untuk memanggil fungsi utama.<br>

Selanjutnya saya akan menampikan Outputnya<br>
Output Program:<br>
<img width="635" height="552" alt="Screenshot (621)" src="https://github.com/user-attachments/assets/d8a0c0ec-0c9f-4d7d-aeeb-edcea3a0bf7c" /><br>
Ini adalah output program jika tidak ada kesalahan penginputan.<br>
- Pertama, kita bisa menambahkan antrian dengan memilih menu nomor 1 dan diikuti penginputan nama serta buku setelahnya lalu akan ditambahkan ke antrian dengan penamaan "Nama - Buku"
- Kedua, kita bisa melihat antrian dengan memilih nomor 2 dan akan tampil list beserta isi data user.nJika ada 10 antrian,maka akan tampil 10 nomor dengan index dimulai dari 0-9<br>
- Ketiga, kita bisa memanggil antrian sesuai nomor urut yang masuk ke list data. Karena menggunakan prinsip FIFO (first In First Out), maka yang pertama kali manginput data akan lebih dulu dipanggil<br>
- Dan yang terakhir, kita bisa keluar program jika semua sudah dijalankan dan program akan berhenti diikuti kalimat "Silahkan Berkunjung Kembali!"<br>

Bagaimana jika input salah? Berikut outputnya:<br>
<img width="638" height="498" alt="Screenshot (622)" src="https://github.com/user-attachments/assets/fb758218-1203-4402-bdb0-e95929c2c637" /><br>
Bisa dilihat, jika input tidak sesuai kondisi, maka akan menampilkan output seperti yang sudah kita buat.

- Di pilihan 1 jika user menginputkan selain integer (angka), maka akan menampilkan tulisan "Masukkan angka ynag valid!" dan kembali ke menu pilihan<br>
- Di pilihan 2 jika sedang tidak ada antrian tapi memilih untuk melihat antrian, maka program akan menampilkan tulisan "Antrian kosong" dan kembali ke menu pilihan<br>
- Di pilihan 3 juga sama. Jika sedang tidak ada antrian tapi memilih untuk memanggil antrian, maka program akan menampilkan tulisan "Antrian kosong" dan kembali semula ke menu pilihan<br>
- Dan akan terus berlanjut sampai ada yang menambah antrian atau memilih keluar di nomor 4 untuk mengenhentikan program.<br>

Link YouTube : https://youtu.be/4ZgssBDGiKY?si=5Tx3DUZOIqqwpBUZ
