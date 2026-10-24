# batas_atas = int(input("hitung mundur dari? "))
# batas_bawah = int(input("sampai berapa? "))
# if batas_atas < batas_bawah:
#     print ("hey hey ini salah yaaa")
# for a in range (batas_atas, batas_bawah-1, -1):
#     print(a)


a = input("Masukkan Nama: ")
kebalikan = ""

for huruf in a:
    kebalikan = huruf + kebalikan
print("Kebalikannya dari", a, "adalah", kebalikan)



