# Kategori selanjutnya bertujuan untuk melakukan pengecekan pada string.
"""
`isupper()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string berupa huruf besar (uppercase) atau tidak. 
`islower()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string berupa huruf kecil (lowercase) atau tidak.
`isalpha()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string adalah huruf (alphabetical) atau tidak.
`isalnum()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string adalah huruf atau angka (alphanumeric) atau tidak.
`isdecimal()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string adalah digit desimal atau tidak.
`isspace()` => digunakan untuk memeriksa apakah semua karakter dalam sebuah string adalah karakter spasi (whitespace) atau tidak.
`istitle()` => digunakan untuk memeriksa apakah setiap kata di dalam sebuah string dimulai dengan huruf kapital dan diikuti oleh huruf kecil.
"""
kata = 'Programing'

print(kata.isupper())
print(kata.islower())
print(kata.isalpha())
print(kata.isalnum())
print(kata.isdecimal())
print(kata.isspace())
print(kata.istitle())
