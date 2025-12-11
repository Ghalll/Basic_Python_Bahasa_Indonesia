# ELSE SETELAH WHILE
# Blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah.

num = 0
while num < 4:
    print("Programing Indonesia")
    num += 1
else:
    print("nilai num melebihi 4")

count = 0
while count < 3:
    print("Programing Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


# jika menggunakan `break` akan seperti berikut
n = 5
while n > 0:
    print("Indonesia")
    n -= 1
    break
else:
    print("yayayay")
