# String merupakan karakter yang berurutan.
#  variabel bernilai string tentu diawali dengan single quote (‘’) atau double quote (“”).
"""
5). String (`str`) : Digunakan untuk merepresentasikan teks atau karakter.
    contoh : `"Hello, World!"`, `'Pyhton'`.
"""
x = 'Programing'
print(type(x))
"""
Output: 
<class 'str'>
"""
# Variabel x yang menyimpan teks “Programing” adalah variabel dengan data bertipe string.

#  dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)
"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# String merupakan urutan karakter yang setiap karakternya memiliki indeks.
# dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing.
x = 'Programing'
print(x[0])

""" 
Output:
D
"""
# Pada kode di atas, diambil indeks ke-0 dari string “Programing” yakni huruf “D”.

# Tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.
x = 'Programing'
x[0] = 'F'

""" 
Output:
TypeError: 'str' object does not support item assignment
"""

# Dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.
x = 'Programing'
print(x[2:])

"""
Output:
ograming
"""
