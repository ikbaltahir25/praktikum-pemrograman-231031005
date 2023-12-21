print("praktikum-a5\n\n")

print("Nama Lengkap : Ikbal")
print("NIM          : 231031005")
print("Prodi        : Sistem Informasi A\n")

nim = ["2","3","1","0","3","1","0","0","5"]
#nim2 = "231031005"
print(nim[1:3])
#print(nim[1:3])

#akses item
print(f"item indeks 0 : {nim[0]}")
print(f"item indeks 4 : {nim[4]}")
print(f"item indeks terakhir : {nim[len(nim)-1]}")

#akses indeks negatif
print(f"item indeks terakhir : {nim[-1]}")
print(f"item indeks pertama : {nim[-len(nim)]}")
print(f"item indeks 6 [-3] : {nim[-3]}")
print(f"item indeks 4 [-5] : {nim[-5]}")
print(f"item indeks 7 [-2] : {nim[-2]}")

#akses indeks batas
print(f"item indeks 1,2,......:\n : {nim[1:]}")
print(f"item indeks 3,4,......:\n  : {nim[3:]}")
print(f"item indeks 0,1,2 :\n : {nim[:3]}")
print(f"item indeks 0,1,2,3 :\n : {nim[:4]}")
print(f"item indeks semua :\n : {nim[:]}")
print(f"item indeks [:8] :\n {nim[:-1]}")
print(f"item indeks [:6] :\n {nim[:-3]}")

#pengirisan
print(f"item indeks 1,2 :\n : {nim[1:3]}")
print(f"item indeks 2,3,4 :\n : {nim[2:5]}")
print(f"item indeks kosong :\n : {nim[3:3]}")
print(f"item indeks [8:8] kosong :\n : {nim[-1:-1]}")
print(f"item indeks [1:8] kosong :\n : {nim[1:-1]}")
print(f"item indeks [2:7] kosong :\n : {nim[2:-2]}")
print()

#print("latihan List")
data = ['Ikbal',2023,'Aktif']
nilai = [90,89,93,97]

print('Nama     : '+ data[0])
print('angkatan :', data[1])
print('status   : '+ data[2])
print()
#>> IKbal status Kuliah: Aktif
print(f'{data[0]} status kuliah : {data[2]}')
#>> Data terbesar nilai adalah: 97
print (f"Data terbesar adalah {max(nilai)}")
#>> Data terkecil nilai adalah: 89
print (f"Data terkecil adalah {min(nilai)}")
#>> Rata-rata nilai adalah: 92.25
print (f"Rata-rata nila adalah {sum(nilai)/len(nilai)}\n")

#print("latihan Tuple")
data = ('Ikbal',2023,'Aktif')
nilai= (90,89,93,97)
print(data[1])
print(data[-1])
print(nilai[1:-1])
print()
#>> Jumlah nilai Ikbal adalah: 4
print(f"Jumlah nilai {data[0]} : {len(nilai)} ")
#>> Data terbesar nilai adalah: 97
print(f"Data terbesar nilai adalah : {max(nilai)}")
#>> Data terkecil nilai adalah: 89
print(f"Data terkecil nilai adalah : {min(nilai)}")
#>> Rata-rata nilai adalah: 92.25
print(f"Rata-rata nilai adalah : {sum(nilai)/len(nilai)}\n")

#print("Latihan Nested List \n")
data = [['Ikbal',2023,'Aktif'],
[94,98,95,97],
[20,22],
['S1-Reguler','Ganjil']]

matkul = ['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ']
sks    = [2,2,2,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'{data[4][0]} dengan jumlah {data[-1][0]} sks\n')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'{data[4][1]} dengan jumlah {data[-1][1]} sks\n')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'{data[4][2]} dengan jumlah {data[-1][2]} sks\n')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'{data[4][3]} dengan jumlah {data[-1][3]} sks\n')
data[4].append('Pengantar Pemrograman')
data[5].append(3)
# print(data)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Pengantar Teknologi Informasi')
data[5].append(3)
data[4].append('Kalkulus Dasar 1')
data[5].append(3)
data[4].append('Sains Terpadu')
data[5].append(3)
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'{data[4][4]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'{data[4][5]} dengan jumlah {data[-1][4]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][6]} dengan jumlah {data[-1][6]} sks\n')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'{data[4][7]} dengan jumlah {data[-1][6]} sks\n')

# Tambahkan 8 nilai masing-masing
data[1].append(98)
data[1].append(95)
data[1].append(92)
data[1].append(97)
print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'Nama Mahasiswa {data[0][0]} dengan NIM {"".join(nim)}')
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[3][1]}')
# >> Jumlah nilai Thomas adalah: 8
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# >> Data terbesar Thomas adalah: 98
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# >> Data terkecil Thomas adalah: 90
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# >> Rata-rata nilai Thomas adalah: 94.625
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/(len(data[1]))}')