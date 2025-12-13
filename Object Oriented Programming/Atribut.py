# Atribut
"""
ada 2 jenis atribut, yaitu :
  1. atribut kelas
    ▶️ Atribut kelas adalah jenis atribut yang secara otomatis terdefinisi dan menjadi
        bawaan kelas ketika instance dibuat berdasarkan kelas tersebut.
  2. atribut objek
    ▶️ Jenis atribut ini memungkinkan setiap instance dari kelas memiliki atribut yang berbeda-beda
        untuk membuat atribut instance kita perlu menggunakan class constructor.
"""
# Contoh Atribut Kelas
class Car:
  warna = "Merah"  # langsung memberikan nilai default

# Contoh atribut Objek
class Book:
  def __init__(self, penulis, penerbit, halaman):
    self.penulis = penulis
    self.penerbit = penerbit
    self.halaman = halaman
