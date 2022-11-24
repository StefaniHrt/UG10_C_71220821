print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")
pertama=int(input("Masukkan angka pertama:"))
kedua=int(input("Masukkan angka kedua:"))
pilihan=int(input("Pilihan Anda:"))
if pilihan==1 :
    print("hasil:", pertama+kedua)
elif pilihan==2 :
    print("hasil:", pertama-kedua)
elif pilihan==3 :
    print("hasil:", pertama*kedua)
elif pilihan==4 :
    print("hasil:", pertama/kedua)
