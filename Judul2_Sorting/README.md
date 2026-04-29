Judul Program : Pengurutan Data Mahasiswa Berbasis Insertion Sort<br>

Deskripsi Singkat : Jadi, pengurutan data ini saya ambil dari "Insertion Sort" yang di improvisasi dengan materi minggu lalu yaitu bagian "List", penambahan looping dan juga "Time" untuk mencatat waktu eksekusinya. Di dalam sistem ini ada data mahasiswa berupa nama dan nilai, di mana ketika fungsi insertion sort dijalankan akan muncul nama dan nilai berdasarkan insertion sort dan berbentuk list.<br>

Source Code:
<img width="385" height="166" alt="Screenshot (650)" src="https://github.com/user-attachments/assets/91d6359d-103d-41ee-85a4-e369e59e80dc" /><br>

Bagian pertama yaitu "import time", di sini kita mengimportkan modul Time agar bisa menggunakan fungsi pencatatatan waktu.<br>

Kemudian, masuk ke bagian fungsi Insertion Sort<br>
- Ada __def insertion_sort(arr, n):__ ini untuk mendefinisikan fungsi insertion sort
- __for i__ untuk loop, __in range (1, n):__ menandakan looping dari 1 sampai ke n
- __temp = arr[1]__ adalah array berindex i yang disimpan di variabel temp
- __j = i - 1__ artinya mundur 1 langkah ke belakang. Misal i = 2 berarti j = 1 karena j = i - 1
- Kemudian ada __while j >= 0 and arr[j][1]__ yang di mana selama j masih dalam array rentang (0 - seterusnya) dan lebih besar dari temp[1]: maka akan dilakukan pergeseran data
- Pergeseran di lakukan dengan kode __arr[j + 1]__ karena tadi j di belakang dan ingin di geser, maka ditambah dengan 1 dan sama dengan __arr[j]__
- Setelah di geser, kita kembalikan lagi untuk perbandingan dengan __j -= 1__ yang artinya untuk perbandingan dengan data sebelumnya, fungsi __j -= 1__ sama dengan __j = j - 1__
- Lalu, ditempatkan ditempat yang tepat dengan __arr[j + 1] = temp__. <br>

Selanjutnya masuk ke fungsi utama yang dibagi menjadi 2 bagian agar lebih rapi:<br>
<img width="550" height="376" alt="Screenshot (651)" src="https://github.com/user-attachments/assets/da44bce3-5fcc-44f0-a00b-6251dc6471c6" /><br>
Baik, akan kita jabarkan.
- __def main():__ artinya mendefinisikan fungsi utama
- __try:__ untuk mencoba kode di bawahnya
- __n = int(input("String"))__ untuk meminta user menginputkan nilai atau data berupa angka
- Kemudian, ada __except__ untuk menangkap error dan __ValueError__ adalah fungsi untuk menampilkan error jika input bukan integer
- __print__ untuk menampilkan teks berupa integer dengan ("String")
- __return__ untuk kembali ke kode yang memanggilnya
- Kemudian ada variabel __data = []__ untuk membuat list kosong yang nanti akan diinputkan oleh user
- Lalu __print__ untuk menampilkan instruksi yang bertuliskan seperti kode di atas<br>

Selanjutnya masuk ke Looping Pertama:
- Masuk ke looping __for i in range(n):__ untuk looping sesuai jumlah n
- Dilanjut dengan __while True:__ yang di mana selama program berjalan akan terus berjalan sampai program selesai
- Variabel __nama = input(f")__ untuk meminta user menginputkan data berupa teks
- __if nama.isalpha():__ adalah suatu percabangan untuk menilai error jika ada kesalahan input yaitu input bukan string yang dilanjut dengan __break__ yang artinya akan lanjut ke loop selanjutnya jika kondisi terpenuhi
- __else:__ berarti jika kondisi di atas tidak terpenui, maka akan menampilkan instruksi berupa teks seperti yang tertera di kode.<br>

Kita lanjut ke Looping Kedua:
- Beberapa kode sama seperti __while__ dan __try__, jadi lanjut ke kode berikutnya
- Variabel __nilai = int(input(f"))__ untuk meminta user menginputkan data berupa angka
- Dilanjut dengan __data.apppend__ untuk menambahkan inputan ke dalam variabel data berupa list yang sebelumnya kosong. Data diisi dengan _nama_ dan _nilai_.
- __break__ untuk masuk ke tahap selanjutnya jika kondisi di atas terpenuhi
- Ada __except ValueError__ lagi untuk menangkap error jika inputan bukan angka
- Lalu menampilkan instruksi berupa teks sesuai yang tertera di kode.<br>

Kemudian masuk ke tahap pemanggilan fungsi untuk menampilkan output<br>
<img width="474" height="340" alt="Screenshot (652)" src="https://github.com/user-attachments/assets/5ed4699d-1182-44ba-bb73-a14a8299af37" /><br>
Selanjutnya ada beberapa penambahan yang saya ambil dari materi minggu lalu yaitu list agar hasil lebih rapi<br>

Data sebelum diurutkan:
- __print("\nData sebelum diurutkan: ")__ untuk menampilkan output string
- Kemudian ada fungsi loop __for i, mhs in enumerate(data, start=1):__ untuk mengambil index dan isi data yang di mulai dari 1
- Lalu __print(f"{i}__ agar bisa memasukkan variabel i ke dalam string
- __{mhs[0]}__ = data _nama_
- __{mhs[1]}__ = data _nilai_<br>

Data setelah diurutkan:
- __print__ seperti sebelumnya
- Loop masih sama hanya berbeda di pemanggilan fungsinya saja yaitu __insertion_sort(data, n)__<br>

Data Sebaliknya (Ascending dan Descending di dalam satu output yang sama):<br>
- Membuat variabel baru yaitu __data_kebalikan__ yang di mana akan memanggil variabel __data__ dan di ambil dari belakang dengan __[::-1]__
- Kemudian loop __for__ hanya berbeda dibagian pemanggilan variabel saja yang sebelumnya __(data, start=1):__ menjadi __(data_kebalikan, start=1):__
- __print__ masih sama<br>

Perhitungan waktu eksekusi:
- Karena sudah kita import modul Time di line pertama, selanjutnya kita masuk ke fungsinya
- __start = time.time()__ untuk mencatat waktu sebelum sorting dilakukan
- Dilanjut dengan pemanggilan fungsi __insertion_sort(data, n)__ agar bisa menghitung waktu sorting
- __end =  time.time()__ untuk mencatat waktu setelah sorting dilakukan
- Kemudian __print(f"\nWaktu eksekusi: {end - start} detik")__ untuk menampilkan hasil eksekusi waktu dengan menghitung selisih _end - start_<br>

Terakhir ada pemanggilan fungsi _main_ untuk menjalankan fungsi utama:
- __if name == "main":__ untuk memastikan program berjalan, dan
- __main()__ untuk memanggil fungsi utama agar program berjalan
