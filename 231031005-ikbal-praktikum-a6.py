a = True

while a:
  pilih = input('Pilihan: ')  
  if pilih == 'ya':
    print('Selamat Datang')
    break
  elif pilih == 'tidak':
    print('Sampai Jumpa')
    break 
else:
  print('Input salah, ulangi lagi')
  a = True

'''
Penjelasan:

a = True
Inisialisasi variabel `a` dengan nilai True. 
Variabel ini akan digunakan untuk mengontrol perulangan while.
 
while a:
Perulangan while akan terus berjalan selama nilai `a` bernilai True.

  pilih = input('Pilihan: ')
Minta input dari user, dan simpan input tersebut ke dalam variabel `pilih`.

 
   if pilih == 'ya':
    print('Selamat Datang')
    break
Jika input user adalah "ya", maka cetak "Selamat Datang" 
dan gunakan perintah `break` untuk menghentikan perulangan `while`.

  elif pilih == 'tidak':
    print('Sampai Jumpa')
    break
Jika input user adalah "tidak", maka cetak "Sampai Jumpa" 
dan hentikan perulangan juga dengan `break`.

else:
  print('Input salah, ulangi lagi')
  a = True
 
Jika input user BUKAN "ya" atau "tidak", maka masuk ke else. 
Cetak pesan input salah, dan tetapkan `a = True` 
agar perulangan `while` terus berjalan.
  
'''