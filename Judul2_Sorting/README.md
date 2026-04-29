Judul Program : Pengurutan Data Mahasiswa Berbasis Insertion Sort<br>

Deskripsi Singkat : Jadi, pengurutan data ini saya ambil dari "Insertion Sort" yang di improvisasi dengan materi minggu lalu yaitu bagian "List", dan saya tambahkan juga "Time" untuk mencatat waktu eksekusinya. Di dalam sistem ini ada data mahasiswa berupa nama dan nilai, di mana ketika fungsi insertion sort dijalankan akan muncul nama dan nilai berdasarkan insertion sort dan berbentuk list.<br>

Source Code:
<img width="385" height="166" alt="Screenshot (650)" src="https://github.com/user-attachments/assets/91d6359d-103d-41ee-85a4-e369e59e80dc" /><br>

Bagian pertama yaitu "import time", di sini kita mengimportkan modul Time agar bisa menggunakan fungsi pencatatatan waktu.<br>

Kemudian, masuk ke bagian fungsi Insertion Sort<br>
- Ada def insertion_sort(arr, n): ini untuk mendefinisikan fungsi insertion sort
- for i untuk loop, in range (1, n): menandakan looping dari 1 sampai ke n
- temp = arr[1] adalah array berindex i yang disimpan di variabel temp
- j = i - 1 artinya mundur 1 langkah ke belakang. Misal i = 2 berarti j = 1 karena j = i - 1
- Kemudian ada while j >= 0 and arr[j][1] yang di mana selama j masih dalam array rentang (0 - seterusnya) dan lebih besar dari temp[1]: maka akan dilakukan pergeseran data
- Pergeseran di lakukan dengan kode arr[j + 1] karena tadi j di belakang dan ingin di geser, maka ditambah dengan 1 dan sama dengan arr[j]
- Setelah di geser, kita kembalikan lagi untuk perbandingan dengan j -= 1 yang artinya untuk perbandingan dengan data sebelumnya, fungsi j -= 1 sama dengan j = j - 1
- Lalu, ditempatkan ditempat yang tepat dengan arr[j + 1] = temp. <br>

