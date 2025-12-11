# Tipe data `dictionary` digunakan untuk menyimpan pasangan kunci-nilai (key-value pairs).
# Dalam dictionary, setiap kunci harus unik, dan nilainya dapat berupa berbagai tipe data. 
# Berikut adalah beberapa karakteristik-nya :
"""
1. Pasangan Kunci-Nilai:
    Setiap elemen dalam dictionary adalah pasangan kunci-nilai. Kunci berperan sebagai identifier
    yang unik untuk setiap nilai dalam dictionary.
2. Dapat Diubah (Mutable):
    Anda dapat menambahkan, mengubah, atau menghapus pasangan kunci-nilai setelah dictionary dibuat.
3.  Tidak Terurut (Unordered):
    Elemen-elemen dalam dictionary tidak memiliki urutan tertentu. Artinya, Anda tidak dapat mengakses elemen berdasarkan indeks.
4. Dinyatakan dengan Kurung Kurawal { }:
    Dictionary dideklarasikan dengan menggunakan tanda kurung kurawal { },
    dan setiap pasangan kunci-nilai dipisahkan oleh tanda titik dua :.
"""
# Membuat Dictionary
data = {'name':"Ghaly", 'age':20, 'major':"Sistem Komputer", 'online':True}
print(type(data))
print(data)

# Mengakses nilai berdasarkan kunci
print("Nama Saya :", data['name'])
print("Umur Saya :", data['age'])

# Menambahkan pasangan kunci-nilai baru
data['Semester'] = 5
print(data)

# Mengubah nilai berdasarkan kunci
data['age'] = 19

# Menghapus pasangan kunci-nilai
del data['online']
print(data)