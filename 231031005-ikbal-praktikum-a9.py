def judul():
    print("MENGHITUNG LUAS DAN KELILING".center(45))
    print("BANGUN DATAR PERSEGI".center(45))
    print()

def inputan():
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    return panjang,lebar

def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = hasil = (panjang+lebar)*2
    return luas,kel

def tampil(pesan,nilai):
    print(f"Hasil perhitungan nilai {pesan} : {nilai}")

def pilihan():
    pilih = input("Apakah ingin melanjutkan? [y/n] : ")
    if pilih == "y":
        a = True
    else:
        a = False
        print("Sampai Jumpa!")
    return a


a = True
while a:
    judul()                             # Judul
    panjang,lebar = inputan()           # Inputan panjang dan lebar
    luas,kel = hitung(panjang,lebar)    # hitung luas dan keliling
    # cetak atau display
    tampil("luas", luas)
    tampil("keliling",kel)
    a = pilihan()                       # pilihan
    