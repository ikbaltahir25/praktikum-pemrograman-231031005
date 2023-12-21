password1 = "pass1"
password2 = "pass2" 
password3 = "pass3"

for i in range(3):
    input1 = input("Masukkan password pertama: ")
    if input1 == password1:
        break
    if i == 2:
        print("Login gagal!")
        exit()
        
for i in range(3):
    input2 = input("Masukkan password kedua: ")
    if input2 == password2:
        break
    if i == 2:
        print("Login gagal!")
        exit()

for i in range(3):
    input3 = input("Masukkan password ketiga: ")
    if input3 == password3:
        print("Anda berhasil login!")
        break
    if i == 2:
        print("Login gagal!")
        exit()