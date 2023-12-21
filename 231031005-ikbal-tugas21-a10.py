#Tugas 2  (program penjumlahan waktu)
awal = input("Masukkan waktu awal (HH:MM): ")
tambah_jam = int(input("Tambah berapa jam: "))  
tambah_menit = int(input("Tambah berapa menit: "))

# pisahkan jam dan menit
jam_awal, menit_awal = map(int, awal.split(':'))

# jumlahkan jam
jam_akhir = jam_awal + tambah_jam

# jumlahkan menit
menit_akhir = menit_awal + tambah_menit

# atur ulang menit jika >= 60
if menit_akhir >= 60:
    jam_akhir += menit_akhir // 60
    menit_akhir %= 60

# atur ulang jam jika >= 24  
if jam_akhir >= 24:
    jam_akhir %= 24

print(f"Waktu sekarang: {jam_akhir:02d}:{menit_akhir:02d}")

#Tugas 2  (program selisih waktu)
awal = input("Masukkan waktu awal (HH:MM): ")
kurang_jam = int(input("Kurang berapa jam: "))  
kurang_menit = int(input("Kurang berapa menit: "))

# pisahkan jam dan menit
jam_awal, menit_awal = map(int, awal.split(':'))

# kurangi jam  
jam_akhir = jam_awal - kurang_jam

# kurangi menit
menit_akhir = menit_awal - kurang_menit

# jika menit < 0, pinjam 60 menit dari jam sebelumnya
if menit_akhir < 0:
    jam_akhir -= 1
    menit_akhir += 60

# jika jam < 0, pinjam 24 jam dari hari sebelumnya
if jam_akhir < 0:
    jam_akhir += 24

print(f"Waktu sekarang: {jam_akhir:02d}:{menit_akhir:02d}")
