# PENYATAAN BREAK
"""
Adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar
dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya. 
"""

for i in range(2):
    print("Perulangan luar :", i)
    for j in range(10):
        print("Perulangan dalam :", j)
        if j == 1:
            break


text = "BARELEK"
for i in text:
    if i == "E":
        break
    print('huruf :', i)
