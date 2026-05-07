Judul Program : Data Kehadiran Mahasiswa<br>

Deskripsi Singkat : Program ini dibuat untuk mencari nama di dalam list daftar kehadiran, apakah si A hadir atau tidak hadir akan tampil dalam program ini. Program ini dibuat dengan metode searching yaitu Sequential Search Sentinel karena di dalam implementasi ini dataset-nya kecil dan lebih sederhana menggunakan metode searching ini. Lengkapnya akan dijelaskan sebagai berikut.<br>

Source Code:
Kita masuk ke bagian defini fungsi liner search sentinel ini.
<img width="441" height="179" alt="Screenshot (702)" src="https://github.com/user-attachments/assets/a038140e-d970-4e20-b6ce-433f95ac6d58" />
Kita bahas satu persatu:
- Ada __def sequential_search_sentinel(data, n, target):__ ini untuk mendefinisikan fungsi dari sequential search sentinel beserta parameternya.<br>
- Dilanjut dengan __data.append(target)__ yaitu penambahan target di batas index agar tidak selalu mencari walaupun sudah melewati batasnya, jadi target ini sebagai batas atau penjaga agar tidak lewat lebih dari index atau jumlah data.
- __i = 0__ berarti menandakan index dimulai dari 0
- __while data[i].lower() != target.lower():__ ini adalah looping yang di mana menekankan bahwa selama data index masih dan belum mencapai target, maka akan lanjut mencari ke index selanjutnya dengan __i += 1__ yang berarti posisi index sekarang ditambah dengan 1, misal index 0 + 1 = 1, begitupun seterusnya. __lower__ di sana berfungsi sebagai pengubah string dalamlist berubah menjai huruf kecil, ini meminimalisir kesalahan input oleh user.
- __data.pop()__ berarti untuk menghapus elemen terakhir dalam list tanpa tidak merusak elemen yang lain
- Kemudian, __if i < n:__ yang berfungsi untuk mengecek apakah index ini masih dibawah jumlah n, jika iya maka fungsi akan dikembalikan ke index dengan kode __return True__, dan jika tidak __else:__ maka tidak ada dalam index yang ditandai dengan -1 pada kode __return False, -1__.<br>

Baik, kita masuk ke fungsi utama:
<img width="594" height="393" alt="Screenshot (703)" src="https://github.com/user-attachments/assets/ffd93be6-f643-481c-84b0-f7256e8c852b" />
Fungsi utama yaitu fungsi yang berfungsi menjalankan program searching ini.

- Ada __def main():__ yang berarti mendefinisikan fungsi utama
- Dilanjut dengan pembuatan variabel __data =[]__ yang berisi data seperti di kode tersebut
- Kemudian, ada __n = len(data)__ yaitu variabel n yang berisi len untuk menghitung jumlah elemen yang ada pada variabel data
- Lalu, ada __print__ untuk menampilkan string maupun menampilkan list data dan _print()_ = \n, sama sama membuat baris baru
- __while True:__ di sini adalah looping yang jika kondisi True maka tidak akan berhenti sampai bertemu dengan __break__
- __target = input ("str")__ untuk meminta input dari user dan akan masuk ke variabel target
- Lalu, ada percabangan kondisi yaitu __if target.isalpha():__ yang artinya jika input dalam variabel target adalah huruf, maka __break__ yaitu loop berhenti dan lanjut ke fungsi berikutnya. Jika __else:__ dalam arti input diluar dari huruf, maka akan menampilkan peringatan dengan __print ("str")__ seperti di kode
- Kemudian, ada variabel __found__ dan __index__ yang di mana mereka memanggil fungsi dari __sequential_search_sentinel__ beserta parameternya __(data, n, target)__
- Ada __print__ lagi untuk memperindah tampilan output
- Dilanjut dengan percabangan (if-else), yaitu __if found:__ yang artinya jika ditemukan, maka __print(f"{target} HADIR (terdaftar di index ke-{index})\n")__ yang berarti akan menampilkan output berupa nama yang dicari dan posisi nama tersebut di dalam list data. Jika tidak ditemukan yaitu __else:__ maka __print(f"{target} TIDAK HADIR (tidak ada dalam daftar)\n")__ yang berarti akan menampilkan output berkebalikan, yaitu tidak hadir dan tidak ada dalam posisi daftar.
- Kemudian, ada __if __name__ == "__main__":__ untuk menandakan bahwa program ini berjalan secara langsung, dan
- __main()__ yaitu pemanggilan fungsi main agar program ini bisa berjalan.<br>

Output:<br>
Di bawah ini adalah output jika input benar
<img width="409" height="122" alt="Screenshot (704)" src="https://github.com/user-attachments/assets/881e70c7-daf1-4d72-84ce-29cf8af7ec56" />
Bisa dilihat, output akan menampilkan teks yang sudah kita buat beserta dengan list data yang berisi daftar kehadiran. Untuk mencari nama siapa yang hadir dan tidak hadir hanya perlu menginputkan nama dibagian "Masukkan nama yang ingin di cek:" menggunakan huruf besar ataupun kecil tidak masalah selagi nama tetap sama. Lalu, akan ditampilkan bahwa si A hadir dan terdaftar pada index ke sekian.<br>

Bagaimana jika input salah?<br>
<img width="476" height="183" alt="Screenshot (705)" src="https://github.com/user-attachments/assets/5864a308-2b70-4d0a-9ac0-a555f4f79ba5" />
Kode di atas menunjukkan bahwa jika input bukan berupa huruf melainkan berupa angka ataupun gabungan dari huruf dan angka, maka program akan kembali looping sampai kondisi input berupa huruf terpenuhi dan lanjut ke fungsi berikutnya. Di sini kita masukkan nama dan ternyata nama tersebut tidak ada di list data, maka akan keluar output berupa nama yang dicari beserta keterangan bahwa si B tidak hadir dan tidak terdaftar dalam list data.<br>

Link YouTube: 

