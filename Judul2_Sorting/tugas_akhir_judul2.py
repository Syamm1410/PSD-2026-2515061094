import time

def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j][1] > temp[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah Mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return
    data = []
    print("Masukkan data Mahasiswa: ")
    for i in range(n):
        while True:
                nama = input(f"Nama Mahasiswa {i + 1}: ")
                if nama.isalpha():
                    break
                else:
                    print("Nama harus berupa huruf!")

        while True:
            try:
                nilai = int(input(f"Nilai Mahasiswa {i + 1}:"))
                data.append((nama, nilai))
                break
            except ValueError:
                print("Nilai harus berupa angka!")
    print("\nData sebelum diurutkan: ")
    for i, mhs in enumerate(data, start=1):
        print(f"{i}. {mhs[0]} - {mhs[1]}")

    insertion_sort(data, n)
    print("\nData setelah diurutkan: ")
    for i, mhs in enumerate(data, start=1):
        print(f"{i}. {mhs[0]} - {mhs[1]}")

    data_kebalikan = data[::-1]
    print("\nData sebaliknya: ")
    for i, mhs in enumerate(data_kebalikan, start=1):
        print(f"{i}. {mhs[0]} - {mhs[1]}")

    start = time.time()
    insertion_sort(data, n)
    end = time.time()
    print(f"Waktu eksekusi: {end - start} detik")

if __name__ == "__main__":
    main()