# metode yang dapat digunakan untuk mengubah string menjadi huruf kapital (UPPERCASE) atau huruf kecil (lowercase).
# Kedua metode ini, baik upper() maupun lower() adalah metode bawaan dari string Python.
"""
`upper()` => method yang mengubah string menjadi uppercase
`lower()` => method yang mengubah string menjadi lowercase
"""
kata = "Python Programming"

katabesar = kata.upper()
print(katabesar)

katakecil = kata.lower()
print(katakecil)


# Kategori ini adalah metode dalam string yang dipergunakan untuk menghapus karakter whitespace atau kata yang tidak diinginkan.
"""
`rstrip()` => method yang digunakan untuk menghapus whitespace pada sebelah kanan atau akhir string.
`lstrip()` => method yang digunakan untuk menghapus whitespace pada sebelah kiri atau awal string. 
`strip()`  => method yang digunakan untuk  menghapus whitespace pada bagian awal dan akhir string.
"""
print("Programing          ".rstrip())
print("           Programing".lstrip())
print("         Programing          ".strip())

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))


# Metode-metode awalan dan akhiran dalam string untuk menemukan kata yang di cari
"""
`startswith()` => bertujuan untuk menemukan suatu kata pada awal string. Metode ini mengembalikan nilai True.
`endswith()`   => bertujuan untuk menemukan suatu kata pada akhir string. Metode ini mengembalikan nilai True.
"""
print('Programing Indonesia'.startswith('Programing'))
print('Programing Indonesia'.endswith('Programing'))


# Kategori metode selanjutnya adalah memisah dan menggabung string.
"""
`join()`  => bertujuan untuk menggabungkan kata dari sebuah iterable (seperti list atau tuple) menjadi satu string.
`split()` => bertujuan untuk memisahkan kata/substring berdasarkan delimiter.
"""
list_kata = ["Bahasa", "Programing", "Python"]
print(" ".join(list_kata))

kalimat = "Bahasa Programing Python"
print(kalimat.split())


# Kategori selanjutnya merupakan metode yang bertujuan untuk mengganti elemen string di dalamnya dengan elemen string lainnya.
"""
`replace()` => bertujuan untuk menggantikan semua kemunculan suatu substring dengan substring lainnya dalam sebuah string. 
"""
string = "Ayo belajar Programing"
print(string.replace("Coding", "Pemrograman"))


# Kategori terakhir yang akan kita bahas pada modul kali ini adalah formatting pada string.
"""
`zfill()` => bertujuan untuk menambahkan nilai nol (0) di depan sebuah string dengan panjang tertentu. 
`rjust()` => bertujuan untuk mengisi karakter di sebelah kanan sebuah string dengan karakter tertentu hingga mencapai panjang tertentu.
`ljust()` => bertujuan untuk mengisi karakter di sebelah kiri sebuah string dengan karakter tertentu hingga mencapai panjang tertentu. 
`center()`=> digunakan untuk menempatkan sebuah string di tengah-tengah sebuah string yang lebih panjang dengan mengisi karakter
              tertentu di kiri dan kanan string tersebut hingga mencapai panjang tertentu.
"""
# method zfill()
angka = "90"
print(angka.zfill(3))

# method rjust()
kata1 = "Python"
print(kata1.rjust(20))

# method ljust()
kata2 = "Java Script"
print(kata2.ljust(20))

# method center()
kata3 = "Java Netbeans"
print(kata3.center(20))
