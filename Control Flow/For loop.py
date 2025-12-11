# PERULANGAN FOR LOOP
# For termasuk sintaks dalam Python yang bersifat definite iteration.
# Definite iteration adalah sebuah proses iterasi atau perulangan ketika jumlah pengulangannya ditentukan secara eksplisit sebelumnya.
# Perulangan for digunakan untuk mengulangi suatu blok kode sejumlah tertentu kali.
# Umumnya digunakan untuk mengulangi elemen-elemen dalam suatu urutan (seperti list, tuple, atau string).
# ⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔

# Contoh for loop dengan `range()`
for x in range(1, 6, 1):
    print(x)

# Contoh for loop dengan list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in num:
    print("nomor :", x)

laptop = ["HP", "MacBook", "Lenovo", "Asus", "Acer", "MSI"]
for x, lp in enumerate(laptop):
    print(f"Indek {x} : {lp}")
