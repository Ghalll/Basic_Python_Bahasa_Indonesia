"""
in dan not in adalah operator keanggotaan (membership operators) pada Python 
yang digunakan untuk memeriksa keberadaan suatu nilai dalam suatu urutan atau koleksi.
"""

kalimat = "Belajar Python sangat menyenangkan"
numbers = [1, 2, 3, 4, 5]

# Operator `in`: untuk memeriksa apakah suatu nilai terdapat dalam urutan atau koleksi tertentu.

print(1 in numbers)         # true
print("java" in kalimat)    # false

# Operator `not in`:  untuk memeriksa apakah suatu nilai tidak terdapat dalam urutan atau koleksi tertentu.

print(1 not in numbers)       # false
print("java" not in kalimat)  # true
