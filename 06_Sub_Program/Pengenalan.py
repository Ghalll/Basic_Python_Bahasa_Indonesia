# SUBPROGRAM
"""
⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔
Subprogram adalah serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program.
Subprogram yang sering digunakan terdiri dari dua jenis, yakni berikut.
  1). Fungsi
      ▶️ Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output.
      ▶️ Fungsi dalam Python adalah blok kode yang dapat dipanggil dan digunakan untuk melakukan tugas tertentu.
  2). Prosedur
      ▶️ Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state).
      ▶️ Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.

"""

# Syntax umum untuk mendefinisikan fungsi
def nama_fungsi(parameter1, parameter2):
  # Blok kode fungsi
  hasil = parameter1 + parameter2
  # Melakukan tugas atau operasi tertentu
  return hasil

"""
▶️ `def` => kata kunci untuk mendefinisikan fungsi.
▶️ `nama_fungsi` => nama yang berikan untuk fungsi.
▶️ `parameter1, parameter2, ...` => parameter yang diperlukan oleh fungsi.
▶️ `return` => kata kunci untuk mengembalikan hasil dari fungsi
"""

# Contoh sederhana dari fungsi
def sum(num1, num2):
  result = num1 + num2
  return result

# Memanggil fungsi
penjumlahan = sum(7,4)
print("Hasil penjumlahan : ", penjumlahan)    # 11