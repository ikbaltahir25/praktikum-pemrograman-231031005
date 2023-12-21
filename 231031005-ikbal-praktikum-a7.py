max_masukkan = 3
password = "si23a"

while max_masukkan > 0:
    p = input("Masukkan Password: ")  
    if p == password:
        print("Selamat Anda Login!")
        break
    max_masukkan -= 1  
    if max_masukkan > 0:
    	print(f"Password Salah!\nKesempatan anda tersisa {max_masukkan} kali")
else:
    	print("Anda kehabisan kesempatan")
         
'''
Penjelasan : 

1. `max_masukkan = 3` : Mendefinisikan jumlah maksimal percobaan input password adalah 3 kali
2. `password = "si23a"` : Mendefinisikan password yang benar adalah "si23a"
3. `while max_masukkan > 0`: Membuat perulangan selama nilai max_masukkan masih lebih besar dari 0. 
    Loop akan berhenti jika max_masukkan bernilai 0.
4. `p = input("Masukkan Password: ")`: Minta input password dari user
5. `if p == password`: Periksa apakah password input (p) sama dengan password yang sudah ditentukan.
6. `print("Selamat Anda Login!")`: Jika password benar, tampilkan pesan login sukses
7. `break`: Keluar dari perulangan jika password sudah benar
8. `max_masukkan -= 1`: Kurangi nilai max_masukkan agar percobaan berkurang 1
9. `if max_masukkan > 0`: Periksa apakah masih ada kesempatan input lagi 
10. Tampilkan sisa kesempatan jika masih ada kesempatan input lagi
11. `else`: jika kesempatan habis, tampilkan pesan kehabisan kesempatan

'''