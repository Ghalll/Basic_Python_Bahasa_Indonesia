# Konversi data (data conversion atau data casting) merujuk pada proses mengubah tipe data satu ke tipe data lain.
# Python menyediakan beberapa fungsi dan metode untuk melakukan konversi data.

"""
Konversi Tipe Data Built-in:
Python menyediakan beberapa fungsi built-in untuk konversi tipe data, seperti int(), float(), str(), dan lainnya.
"""
angka = 10
teks_angka = str(angka)  # Mengubah integer ke string
float_angka = float(angka)  # Mengubah integer ke float
print(teks_angka)
print(float_angka)


"""
Konversi Tipe Data dengan Metode:
"""
teks_angka = "123"
angka = int(teks_angka)  # Mengubah string ke integer
print(angka)


"""
Konversi List, Tuple, Set:
Anda dapat menggunakan fungsi list(), tuple(), dan set() untuk mengonversi antara list, tuple, dan set.
"""
daftar_angka = [1, 2, 3]
tupel_angka = tuple(daftar_angka)  # Mengubah list ke tuple
set_angka = set(daftar_angka)  # Mengubah list ke set
print(tupel_angka)
print(set_angka)


"""
Konversi Dictionary:
Fungsi dict() dapat digunakan untuk mengonversi tuple pasangan kunci-nilai ke dictionary.
"""
pasangan_kunci_nilai = [("a", 1), ("b", 2)]
dictionary = dict(pasangan_kunci_nilai)  # Mengubah tuple ke dictionary
print(dictionary)
