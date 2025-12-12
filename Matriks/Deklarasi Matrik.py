# Ada 2 cara untuk mendeklarasikan matriks
"""
1). Deklarasi sekaligus inisialisasi nilai matriks.
    ▶️ Cara pertama adalah mendeklarasikan matriks sekaligus menginisialisasikan nilainya dengan ukuran N baris dan M Kolom (NxM).
        cara ini dilakukan ketika telah mengetahui nilai yang diberikan.
2). Deklarasi dengan nilai default.
    ▶️ Cara kedua adalah mendeklarasikan matriks dengan nilai default.
        Cara kedua ini melibatkan list comprehension yang sama seperti pada materi array.
        cara kedua ini menggunakan dua metode sekaligus, yakni nested list dan nested for.

"""
# Contoh deklarasi matrik biasa
matriks = [[1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1]]
print(matriks)

# Contoh deklarasi matrik dengan nilai default
mat = [[0 for j in range(4)] for i in range(3)]
print(mat)


# Cara Mengakses elemen matrik = <namamatriks>[<nbrs>][<nkol>]
print(matriks[1][3])