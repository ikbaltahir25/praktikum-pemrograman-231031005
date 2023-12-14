print("praktikum-a2\n\n")

print("Nama Lengkap : Ikbal")
print("NIM          : 231031005")
print("Prodi        : Sistem Informasi A\n")

# INI OPERATOR ASSIGMENT
a=19
print("Nilai a adalah=",a)
a+=3
print("Nilai a+=3 sekarang adalah=",a)

a=19
print("Nilai a adalah=",a)
a-=3
print("Nilai a-=3 sekarang adalah=",a)

a=19
print("Nilai a adalah=",a)
a*=2
print("Nilai a*=2 sekarang adalah=",a)

a=19
print("Nilai a adalah=",a)
a/=2
print("Nilai a/=2 sekarang adalah=",a)

a=3
print("Nilai a adalah=",a)
a**=2
print("Nilai a**=2 sekarang adalah=",a)

a=35
print("Nilai a adalah=",a)
a%=32
print("Nilai a%=32 sekarang adalah=",a)

a=35
print("Nilai a adalah=",a)
a//=32
print("Nilai a//=32 sekarang adalah=",a)

# tugas melanjutkan untuk operator selanjutnya line 25-line 59

# OR
b=True
print("Nilai b = ",b)
b|=False
print("Nilai b|=False akan menjadi",b)
b=False
print("Nilai b =",b)
b|=False
print("Nilai b|=False akan menjadi",b)

# AND
b=True
print("Nilai b =",b)
b&=False
print("Nilai b&=False akan menjadi",b)
b=False
print("Nilai b =",b)
b&=False
print("Nilai b&=False akan menjadi",b)

# XOR
b=True
print("Nilai b =",b)
b^=False
print("Nilai b^=False akan menjadi",b)
b=False
print("Nilai b =",b)
b^=False
print("Nilai b^=False akan menjadi",b)

# Shifting
c=0b0100
print("Nilai c =",format(c,   "04b"))
c>>=1
print("Nilai c>>=1 akan menjadi",format(c,   "04b"))
c=0b0100
c<<=1
print("Nilai c<<=1 akan menjadi",format(c,   "04b"))

# OPERATOR PERBANDINGAN
a=9
b=13
print("\n---------- Besar dari 5")
hasil=a > 5
print(a,"> 5 adalah",hasil)
hasil=b > 5
print(b,"> 5 adalah",hasil)

print("\n---------- Kecil dari 5")
hasil=a < 5
print(a,"< 5 adalah",hasil)
hasil=b < 5
print(b,"< 5 adalah",hasil)

print("\n---------- Besar atau Sama dari 5")
hasil=a >= 5
print(a,">= 5 adalah",hasil)
hasil=b >= 5
print(b,">= 5 adalah",hasil)

print("\n---------- Kecil atau Sama dari 5")
hasil=a <= 5
print(a,"<= 5 adalah",hasil)
hasil=b <= 5
print(b,"<= 5 adalah",hasil)

print("\n---------- Sama dari 5")
hasil=a == 5
print(a,"== 5 adalah",hasil)
hasil=b == 5
print(b,"== 5 adalah",hasil)

print("\n---------- Tidak Sama dari 5")
hasil=a != 5
print(a,"! 5 adalah",hasil)
hasil=b != 5
print(b,"! 5 adalah",hasil)

#OPERATOR LOGIKA
a = True
b = False
print("\n==========AND=========")

hasil = a and a
print(a,"and",a,"hasilnya=",hasil)

hasil = a and b
print(a,"and",b,"hasilnya=",hasil)

hasil = b and a
print(b,"and",a,"hasilnya=",hasil)

hasil = b and b
print(b,"and",b,"hasilnya=",hasil)

print("\n==========OR=========")
hasil = a or a
print(a,"or",a,"hasilnya=",hasil)

hasil = a or b
print(a,"or",b,"hasilnya=",hasil)

hasil = b or a
print(b,"or",a,"hasilnya=",hasil)

hasil = b or b
print(b,"or",b,"hasilnya=",hasil)

print("\n==========XOR=========")

hasil = a ^ a
print(a,"xor",a,"hasilnya=",hasil)

hasil = a ^ b
print(a,"xor",b,"hasilnya=",hasil)

hasil = b ^ a
print(b,"xor",a,"hasilnya=",hasil)

hasil = b ^ b
print(b,"xor",b,"hasilnya=",hasil)

print("\n==========NOT=========")

hasil = not a
print("not",a,"hasilnya=",hasil)
hasil = not b
print("not",b,"hasilnya=",hasil)

#OPERATOR MEMBERSHIP
print("\n===================IN")
nama ="ikbal"

test ="ik"
cek = test in nama
print(test,"terdapat di",nama,"adalah",cek)

test ="ki"
cek = test in nama
print(test,"terdapat di",nama,"adalah",cek)

test1 = "a"
test2 = "i"
test3 = "u"
test4 = "e"
test5 = "0"

cek = test1 in nama
print(test1,"terdapat di",nama,"adalah",cek)
cek = test2 in nama
print(test2,"terdapat di",nama,"adalah",cek)
cek = test3 in nama
print(test3,"terdapat di",nama,"adalah",cek)
cek = test4 in nama
print(test4,"terdapat di",nama,"adalah",cek)
cek = test5 in nama
print(test5,"terdapat di",nama,"adalah",cek)

print("\n===================NOT IN")
cek = test1 not in nama
print(test1,"tidak terdapat di",nama,"adalah",cek)
cek = test2 not in nama
print(test2,"tidak terdapat di",nama,"adalah",cek)
cek = test3 not in nama
print(test3,"tidak terdapat di",nama,"adalah",cek)
cek = test4 not in nama
print(test4,"tidak terdapat di",nama,"adalah",cek)
cek = test5 not in nama
print(test5,"tidak terdapat di",nama,"adalah",cek)