''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!
Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Ikbal',
            '231031005',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '25-Mei-2005']

MK =   [['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta IPTEK dan IMTAQ','Pengantar Pemrograman','Pengantar Teknologi Informasi','Kalkulus Dasar I','Sains Terpadu'],
        [2,2,2,2,3,3,3,3],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

sp = 73
aa = (Bio[0].upper())
print(aa.center(sp))
ab = (Bio[2].upper())
print(ab.center(sp))
ac = (Bio[3].upper())
print(ac.center(sp))
ad = (Bio[-3].upper()+" "+Bio[-4][0:4]+"/"+Bio[-4][5:9])
print(ad.center(sp))
print()
print()

ae = (Bio[-4][0:4])
print(f"""
Nama Lengkap      : {Bio[4].upper()}
NIM               : {Bio[5]}
Program/Prodi     : {Bio[6]}/{Bio[7]}
Tahun Masuk       : {ae+"-"+Bio[-3].capitalize()}
Status            : {Bio[-2].capitalize()}
      """)
print()
print("-"*sp)
print("No.Kode"+"|".center(12)+"Mata Kuliah".center(31)+"|"+"SKS".center(7)+"|"+"Nilai (0-4)".center(13)+"|")
print("-"*sp)
print("1"+"  "+MK[2][0].ljust(9)+"|"+" "+MK[0][0].ljust(36)+"|"+"2".center(7)+"|"+"3.50".rjust(13)+"|")
print("2"+"  "+MK[2][1].ljust(9)+"|"+" "+MK[0][1].ljust(36)+"|"+"2".center(7)+"|"+"3.00".rjust(13)+"|")
print("3"+"  "+MK[2][2].ljust(9)+"|"+" "+MK[0][2].ljust(36)+"|"+"2".center(7)+"|"+"3.75".rjust(13)+"|")
print("4"+"  "+MK[2][3].ljust(9)+"|"+" "+MK[0][3].ljust(36)+"|"+"2".center(7)+"|"+"4.00".rjust(13)+"|")
print("5"+"  "+MK[2][4].ljust(9)+"|"+" "+MK[0][4].ljust(36)+"|"+"3".center(7)+"|"+"3.75".rjust(13)+"|")
print("6"+"  "+MK[2][5].ljust(9)+"|"+" "+MK[0][5].ljust(36)+"|"+"3".center(7)+"|"+"3.50".rjust(13)+"|")
print("7"+"  "+MK[2][6].ljust(9)+"|"+" "+MK[0][6].ljust(36)+"|"+"3".center(7)+"|"+"3.75".rjust(13)+"|")
print("8"+"  "+MK[2][7].ljust(9)+"|"+" "+MK[0][7].ljust(36)+"|"+"3".center(7)+"|"+"3.00".rjust(13)+"|")
print("-"*sp)

af = sum(MK[1])
print(f'''                                        Total SKS :   {sum(MK[1])}''')
print("-"*sp)
print("Summary :")
print(f"""Jumlah Mata Kuliah              : {len(MK[0])} Mata Kuliah""")
print(f"Nilai Tertinggi                 : {max(MK[-1])} ({MK[2][3]} - {MK[0][3]})")
print(f"Nilai Tertinggi                 : {min(MK[-1])} ({MK[2][1]} dan {MK[2][7]} - {MK[0][1]} dan {MK[0][7]} )")
rt = [MK[1][0] * MK[3][0],
         MK[1][1] * MK[3][1],
         MK[1][2] * MK[3][2],
         MK[1][3] * MK[3][3],
         MK[1][4] * MK[3][4],
         MK[1][5] * MK[3][5],
         MK[1][6] * MK[3][6],
         MK[1][7] * MK[3][7]]
rataan = sum(rt)/sum(MK[1])
print(f"IP Kumulatif                    : {rataan}")
print()
print("Parepare, 25 Oktober 2023".rjust(70))
print()
print()
print()
print(('-'*22).rjust(68))
print(Bio[4].rjust(60))

