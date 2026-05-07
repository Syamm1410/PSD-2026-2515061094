def sequential_search_sentinel(data, n, target):
    data.append(target)
    i = 0
    while data[i].lower() != target.lower():
        i += 1 
    data.pop()
    if i < n:
        return True, i
    else:
        return False, -1


def main():
    data = ["Fatih", "Ahmad", "Risa", "Amar", "Dimas",  "Hatta", "Fakhri"]
    n = len(data)
    print("\n=== DATA KEHADIRAN MAHASISWA ===")
    print(data)
    print()

    while True:
        target = input("Masukkan nama mahasiswa yang ingin dicek: ")
        if target.isalpha():
            break
        else:
            print("Nama harus berupa huruf!")

    found, index = sequential_search_sentinel(data, n, target)
    print("\n=== HASIL ===")
    if found:
        print(f"{target} HADIR (terdaftar di index ke-{index})\n")
    else:
        print(f"{target} TIDAK HADIR (tidak ada dalam daftar)\n")

if __name__ == "__main__":
    main()