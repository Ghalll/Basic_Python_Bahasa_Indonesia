# Tipe data primitif pertama, yakni numbers adalah tipe data angka berupa bilangan bulat, riil, dan kompleks.
# 
"""
1). Integers (`int`) : Bilangan bulat positif atau negatif dan tidak memiliki angka desimal.
    contoh : `1`, `-20`, `999`, dan `0`.
2). Float (`float`) : Bilangan riil yang dapat mewakili bilangan bulat atau bilangan desimal.
    contoh : `3.14`, `-0.5`, `4.01E+1`.
3). Complex (`complex`) : Digunakan untuk merepresentasikan bilangan kompleks.
    contoh : `1+2j`.
"""
x = 6
print(type(x))  # integer 

x = 6.0
print(type(x))  # float

x = 1+2j
print(type(x))  # complexs

# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.
# contoh

var = 10
print(var)          # 10
print(id(var))      # <memory address>

var = 11
print(var)          #11
print(id(var))      # <memory address>
