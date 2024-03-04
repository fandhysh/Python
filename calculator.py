import os

print("=====================")
print("|     CALCULATOR    |")
print("=====================")
print("")


def menu():
    menu = input(
        "1. Penjumlahan\n2. Lingkaran\n3. Persegi\n4. Persegi Panjang\n5. Limas\n\nPilih Opsi : "
    )
    print("")

    match menu:
        case "1":
            penjumlahan()
        case "2":
            lingkaran()
        case "3":
            persegi()
        case "4":
            persegipanjang()
        case "5":
            Llimas()
        case _:
            print("sabar belom ada")


def penjumlahan():
    os.system("cls")
    num1 = int(input("Masukan Angka : "))
    operator = input("Pilih (+, -, *, /) : ")
    num2 = int(input("Masukan Angka : "))

    tambah = num1 + num2
    kurang = num1 - num2
    kali = num1 * num2
    bagi = num1 / num2
    print("---------------------")

    match operator:
        case "+":
            print("Hasil : " + str(tambah))
        case "-":
            print("Hasil : " + str(kurang))
        case "*":
            print("Hasil : " + str(kali))
        case "/":
            print("Hasil : " + str(bagi))
        case _:
            print("DONGO!")

def lingkaran():
    menu = input("1. Keliling\n2. Luas\n\nPilih Opsi : ")
    print("---------------------")

    match menu:
        case "1":
            Klingkaran()
        case "2":
            Llingkaran()
def Klingkaran():
    os.system("cls")
    print("[ Keliling Lingkaran ]")
    print("")
    num1 = 3.14
    num2 = int(input("Masukan jari - jari : "))
    print("---------------------")

    Klingkaran = 2 * num1 * num2
    print("Hasilnya : " + str(round(Klingkaran)))
def Llingkaran():
    os.system("cls")
    print("[ Luas Lingkaran ]")
    print("")
    num1 = 3.14
    num2 = int(input("Masukan jari - jari : "))
    print("---------------------")

    Llingkaran = num1 * (num2 * num2)
    print("Hasilnya : " + str(round(Llingkaran)))

def persegi():
    menu = input("1. Keliling\n2. Luas\n\nPilih Opsi : ")
    print("---------------------")

    match menu:
        case "1":
            Kpersegi()
        case "2":
            Lpersegi()
def Kpersegi():
    os.system("cls")
    print("[ Keliling Persegi ]")
    print("")
    num1 = int(input("Masukan sisi : "))
    print("---------------------")

    Kpersegi = 4 * num1
    print("Hasilnya : " + str(round(Kpersegi)))
def Lpersegi():
    os.system("cls")
    print("[ Luas Persegi ]")
    print("")
    num1 = int(input("Masukan panjang : "))
    num2 = int(input("Masukan lebar : "))
    print("---------------------")

    Lpersegi = num1 * num2
    print("Hasilnya : " + str(round(Lpersegi)))

def persegipanjang():
    menu = input("1. Keliling\n2. Luas\n\nPilih Opsi : ")
    print("---------------------")

    match menu:
        case "1":
            Kpersegipanjang()
        case "2":
            Lpersegipanjang()
def Kpersegipanjang():
    os.system("cls")
    print("[ Keliling Persegi Panjang ]")
    print("")
    num1 = int(input("Masukan panjang : "))
    num2 = int(input("Masukan lebar : "))
    print("---------------------")

    Kpersegipanjang = 2 * (num1 + num2)
    print("Hasilnya : " + str(round(Kpersegipanjang)))
def Lpersegipanjang():
    os.system("cls")
    print("[ Luas Persegi Panjang ]")
    print("")
    num1 = int(input("Masukan panjang : "))
    num2 = int(input("Masukan lebar : "))
    print("---------------------")

    Lpersegipanjang = num1 * num2
    print("Hasilnya : " + str(round(Lpersegipanjang)))

def Llimas():
    os.system("cls")
    print("[ Luas Limas ]")
    print("")
    num1 = int(input("Masukan luas alas : "))
    num2 = int(input("Masukan sisi tegak : "))
    num3 = int(input("Masukan tinggi : "))
    print("---------------------")

    Llimas = (num1 * num1) + (num2 * num1 * num3 / 2)
    print("Hasilnya : " + str(round(Llimas)))


menu()
