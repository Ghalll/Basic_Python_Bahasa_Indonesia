# ELSE SETELAH FOR
# Pada Python juga dikenal else setelah for yang berfungsi untuk perulangan bersifat pencarian.
# Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.

angka = [1, 2, 3, 4, 5]
for num in angka:
    if num == 7:
        print("Angka ditemukan:", num)
        break
else:
    print("Angka tidak ditemukan")
