# Fungsi Anonim (Lambda Expression)
"""
Adalah cara singkat untuk mendefinisikan fungsi anonim (tanpa nama) dalam Python.
Cara ini dikenal dengan ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya.

Struktur umum fungsi lamda : 
  func = lamda args: ret_val
  - `func` => adalah penamaan untuk fungsinya.
  - `args` => adalah parameternya.
  - `ret_val` => nilai yang akan dikembalikan.
"""

fungsiperkalian = lambda num1, num2 : num1*num2
print(fungsiperkalian(10,12))

# Fungsi lambda untuk mengkuadratkan suatu angka
kuadrat = lambda x: x**2

# Memanggil fungsi lambda
hasil = kuadrat(5)
print(hasil)  # Output: 25
