count = 0 
batas = 5 
while count < batas : 
    print(f"Menjalankan Program ke-{count+1}") 
    count += 1

"""variabel count akan digunakan untuk melacak berapa kali perulangan while sudah berjalan"""
#count = 0 
"""menetapkan nilai batas atau maksimal jumlah perulangan adalah 5"""
#batas = 5 
"""perulangan while ini akan terus berjalan selama variabel count masih di bawah nilai batas, 
dalam hal ini nilai batas adalah lima. Jadi selama count belum mencapai angka 5, perulangan akan terus berlanjut.
Ini yang akan menjadi batasan agar perulangan berhenti setelah lima kali"""
#while count < batas :
'''Bagian ini mencetak pesan ke layar dengan format string f"" yang dilewatkan variabel `count`. 
    Karena index dimulai dari 0 sedangkan iterasi dimulai dari 1, 
    maka kita tambahkan `count+1` agar print index iterasinya dimulai dari 1.'''
    #print(f"Menjalankan Program ke-{count+1}") 
'''Setelah mencetak pesan, 
    tambahkan nilai `count` sebesar 1 agar pada akhirnya nanti
    nilai count bisa mencapai batas dan keluar dari perulangan.'''
    #count += 1