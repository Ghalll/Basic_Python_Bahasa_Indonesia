# Tipe data collection merupakan tipe data yang menyimpan satu atau lebih data primitif sebagai satu kelompok.
# berikut tipe datanya:
"""
1). List (`list`) : kumpulan data terurut (ordered sequence) yang dapat diubah (mutable).
    List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya.
    nilai yang diawali dengan kurung siku “[]” akan dianggap sebagai data bertipe list.
    Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0.
    contoh : x = [1, 2.2, 'Programing', true]

2). Tuple (`tuple`) : adalah jenis dari list yang tidak dapat diubah elemennya.
    tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat.
    Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.
    contoh : x = (1, "Programing", 1+3j)

3). Set (`set`) : adalah kumpulan item bersifat unik (tanpa duplikat), tanpa urutan (unordered collection),
    dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.
    pada set tidak bisa melakukan indeksing karena set tidak memiliki indeks.
    set adalah himpunan dalam matematika sehingga dapat melakukan operasi union (gabungan) dan intersection (irisan) pada set.
    Python menyediakan method “.union()” dan “.intersection()” untuk tipe data set.
    contoh : x = {1,2,7,2,3,13,3}

4). Dictionary (`dict`) : merupakan kumpulan pasangan key-value yang bersifat tidak berurutan.
    digunakan untuk menyimpan data kecil hingga besar.
    dictionary didefinisikan dengan kurawal.
    contoh : x = {"nama": "Budi", "usia": 20, "jurusan": "Informatika"}

"""
