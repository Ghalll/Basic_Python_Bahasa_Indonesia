# Fungsi sort() adalah metode pada objek list yang digunakan untuk mengurutkan
# Elemen-elemen list secara ascending (naik) atau descending (turun).

# Ascending (naik) sort
abjad = ['a', 'd', 't', 'e', 'x', 'p', 'b']
abjad.sort()
print(abjad)

# fungsi sort dapat membalikan urutan => decending (turun)
abjad.sort(reverse=True)
print(abjad)

# fungsi sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.
urutan = ['Programing', 1, 2, 'Indonesia', 3]
urutan.sort()
print(urutan)
"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""

# fungsi sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()
print(kendaraan)
