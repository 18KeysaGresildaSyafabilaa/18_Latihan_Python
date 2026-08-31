def input_angka():
    return input("Masukkan angka (atau ketik 'close' untuk keluar): ")

def cek_keluar(teks):
    return teks.lower() == "close"

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")

def proses_input():
    while True:
        teks = input_angka()

        if cek_keluar(teks):
            print("Kembali ke menu.")
            break

        angka = int(teks)
        cek_ganjil_genap(angka)

def cek_satu_angka():
    angka = int(input("Masukkan satu angka: "))
    cek_ganjil_genap(angka)

def tentang_program():
    print("\nProgram ini dibuat untuk mengecek apakah")
    print("suatu bilangan termasuk ganjil atau genap.")
    print("Dibuat oleh: gresilda lutcu\n")

def menu():
    print("\n=== PROGRAM CEK GANJIL GENAP ===")
    print("1. Cek satu angka")
    print("2. Cek berulang (banyak angka)")
    print("3. Tentang program")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    return pilihan

def mulai_program():
    while True:
        pilihan = menu()

        if pilihan == "1":
            cek_satu_angka()
        elif pilihan == "2":
            proses_input()
        elif pilihan == "3":
            tentang_program()
        elif pilihan == "4":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan gak valid, coba lagi.")

mulai_program()