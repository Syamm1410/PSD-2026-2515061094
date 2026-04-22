def menu():
    print ("\n===ANTRIAN PERPUSTAKAAN===")
    print ("1. Tambah Antrian")
    print ("2. Lihat Antrian")
    print ("3. Panggil Antrian")
    print ("4. Keluar")

def main():
    antrian = []
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if choice == 1:
            nama = input("Masukkan Nama Peminjam: ")
            buku = input("Masukkan Judul Buku: ")
            data = {"Nama": nama, "Buku": buku}
            antrian.append((data))
            print(f"{nama} telah ditambahkan ke antrian untuk buku '{buku}'.")

        elif choice == 2:
            if antrian:
                print("Antrian saat ini:")
                for i, data in enumerate(antrian, start=1):
                    print(f"{i}. {data['Nama']} - {data['Buku']}")
            else:
                print("Antrian kosong!")

        elif choice == 3:
            if antrian:
                dipanggil = antrian.pop(0)
                print(f"{dipanggil['Nama']} dipanggil untuk meminjam buku '{dipanggil['Buku']}'.")
            else:
                print("Antrian kosong!")

        elif choice == 4:
            running = False
            print("Silahkan Berkunjung Kembali!.")

        else:
            print("Pilihan tidak valid!")
            continue

if __name__ == "__main__":
    main()