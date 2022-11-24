pesanan=str(input("Masukkan daftar pesanan : "))
daftar=pesanan.split(', ')
print("Daftar pesanan :", daftar)
tambah=str(input("Masukkan pesanan yang ingin ditambah : "))
if tambah not in daftar :
    daftar.append(tambah.upper())
    print("Hasil penambahan pada daftar pesanan :", daftar)
else :
   print(tambah.upper(), "sudah berada dalam daftar pesanan.")
