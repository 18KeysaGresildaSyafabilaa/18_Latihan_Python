angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")    
while True:
    angka = input("Masukkan angka (atau ketik 'close' untuk keluar): ")

    if angka.lower() == "close":
        print("Program dihentikan.")
        break

    angka = int(angka)

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")