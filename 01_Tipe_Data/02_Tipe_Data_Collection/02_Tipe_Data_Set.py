# Tipe data `set` digunakan untuk menyimpan kumpulan nilai unik tanpa urutan tertentu.
# Set mirip dengan himpunan dalam matematika dan memungkinkan operasi-operasi himpunan seperti penyatuan, irisan, dan perbedaan.
# Dapat dimanfaatkan untuk menghilangkan duplikat pada suatu data.
# Berikut adalah beberapa karakteristik-nya :
"""
1. Unik:
    Set hanya menyimpan nilai unik. Jika Anda mencoba menambahkan elemen yang sudah ada, set tidak akan mengganti nilai yang sudah ada.
2. Tidak Terurut (Unordered):
    Elemen-elemen dalam set tidak memiliki urutan tertentu. Artinya, Anda tidak dapat mengakses elemen berdasarkan indeks.
3. Dinyatakan dengan Tanda Kurung Kurawal `{ }`:
    Set dideklarasikan dengan menggunakan tanda kurung kurawal `{ }`.
4. Operasi Himpunan:
    Set mendukung operasi-operasi himpunan seperti penyatuan (union), irisan (intersection), dan perbedaan (difference).
"""
# Membuat set
x = {1,2,7,2,3,13,3}
print(x)

# Menambahkan elemen ke dalam set
x.add(200)
print(x)

# Menghapus elemen dari set
x.remove(200)
print(x)

# Operasi Himpunan
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

uni = set1.union(set2)  # Penyatuan
print("union:", uni)

iri = set1.intersection(set2)   # Irisan
print("Intersection:", iri)

beda = set1.difference(set2)    # Perbedaan
print("Difference:", beda)

