#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
  if nilai<=1:
    return 1
  else:
    return nilai*faktorial(nilai-1)

#Program Utama  
n = int(input("Masukkan nilai: "))

for i in range(n+1):
  print('%2d ! = %d' % (i,faktorial(i)))