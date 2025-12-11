# Tipe data `list` digunakan untuk menyimpan sejumlah nilai yang dapat diubah (mutable).
# List dalam Python ini serupa, tetapi tak sama dengan array pada bahasa pemrograman lainnya.
# Berikut adalah beberapa karakteristik-nya :
"""
1. Dapat diubah (Mutable):
    List memungkinkan penambahan, penghapusan, dan pengubahan elemen-elemen di dalamnya.
2. Urutan (Ordered):
    Elemen-elemen dalam list memiliki urutan tertentu, yang berarti kita dapat merujuk pada elemen berdasarkan indeksnya.
3. Dapat Menyimpan Berbagai Tipe Data:
    List dapat menyimpan elemen-elemen dengan berbagai tipe data, termasuk numbers, strings, dan bahkan list lainnya.
4. Dinyatakan dengan Tanda Kurung Siku [ ]:
    List dideklarasikan dengan menggunakan tanda kurung siku `[ ]`.
"""
# membuat list
x = [1, 2.3, 'Code', True]
print(type(x))

# mengakses elemen berdasarkan indeks
print(x[2])

# mengubah nilai elemen berdasarkan indeks
x[0]="indonesia"
print(x)

# menambahkan elemen ke dalam list
x.append(100)
print(x)

# menghapus elemen berdasarkan nilai
x.remove(2.3)
print(x)


# konsep indexing merujuk pada pengambilan data dalam Pyhton berdasarkan indeksnya.
hardware = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(hardware[-2])

# konsep slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu.
# syntax : sequence[start:stop:step]
"""
Start merupakan indeks pertama yang ambil.
Stop merupakan indeks terakhir yang ingin ambil.
Step merupakan jumlah elemen yang ingin di lewati di antara setiap elemen slice.
Secara default, nilai step adalah 1
"""
print(hardware[3:7:3])
print(hardware[:2])
print(hardware[5:])