#  Quiz 1
# angka_awal = 1
# angka = int(input("batas angkanya sampai berapa? "))
# for a in range (angka_awal,angka+1):
#     if a%3==0 and a%5==0:
#         print("FizzBuzz")
#     elif a%3 == 0:
#         print("Fizz")
#     elif a%5==0 :
#         print("Buzz")
#     else:
#         print(a)


# Quiz 2
angka = []
while True:
    a = int(input("Masukkan angka dalam list: \n (Ketik '-888' jika dirasa cukup)\n:"))
    if a == -888:
        break
    angka.append(a)

print(f"Final list anda adalah {angka}")

if len(angka) == 0:
    print("List anda kosong. Tolong isi berapa")
else:
    angka_terbesar = angka[0]
    for a in angka:
        if a > angka_terbesar:
            angka_terbesar = a
    print(f"Angka terbesar adalah {angka_terbesar}")

            