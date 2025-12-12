# Operasi Matriks pada Python
"""
Dalam matematika ataupun pemrograman, operasi matriks dapat melibatkan dua matriks sekaligus atau pun satu matriks saja.
Beberapa operasi tersebut di antaranya sebagai berikut.
  A. OPERASI 1 MATRIKS
    -Menghitung total semua elemen matriks.
    -Mengalikan elemen matriks dengan konstanta.
    -Transpose matriks.
    -Inverse matriks.
    -Menentukan determinan, dan sebagainya.
  B. OPERASI 2 MATRIKS
    -Menambahkan dua matriks.
    -Mengalikan dua matriks.
    -Pembagian dua matriks, dan sebagainya.
"""
matrik1 = [[5, 0],
          [1, -5]]
result = [[0 for j in range(2)] for i in range(2)]

for i in range(len(matrik1)):
  for j in range(len(matrik1[0])):
    result[i][j] = matrik1[i][j] * 2

print(result)
