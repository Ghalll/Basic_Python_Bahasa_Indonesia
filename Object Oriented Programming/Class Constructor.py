# Class Constructor
"""
Pembangun kelas atau class constructor adalah sebuah fungsi khusus dalam Python yang digunakan untuk
menentukan nilai awal atau kondisi awal dari suatu kelas.
`__init__` adalah fungsi khusus untuk membuat constructor
Parameter `self`, yakni sebuah kata kunci untuk merujuk pada objek yang sedang diproses saat ini.
"""

class Car:
  def __init__(self, warna, merk, speed):
    self.warna = warna
    self.merk = merk
    self.speed = speed
car1 = Car("Hitam","Toyota",180)
