# Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE.
# Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi dan menghasilkan nilai true.
"""
4). Boolean (`bool`) :  tipe data yang hanya bernilai TRUE atau FALSE.
    contoh : `True`, `False`.
"""
# Hanya ada beberapa nilai yang akan dianggap bernilai false sebagai berikut.
"""
1. Nilai yang sudah didefinisikan bernilai salah: None dan False.
2. Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
3. Urutan (sequence) dan koleksi (collection) yang kosong: “”, (), {}, set(), range(0). 
"""
x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""