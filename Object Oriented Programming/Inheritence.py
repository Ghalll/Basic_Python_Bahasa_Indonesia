# INHERITANCE (PEWARISAN)
"""
Pewarisan (inheritance) dalam Python adalah suatu konsep dalam pemrograman berorientasi objek
di mana sebuah kelas (subclass atau turunan) dapat mewarisi atribut dan metode dari kelas lain (superclass atau induk). 

yaitu dimana dapat membuat kelas baru dengan menggunakan kelas induk yang sudah ada.

Fungsi `super` 
  ▶️ Merujuk ke kelas induk atau superclass. Ini digunakan untuk mengakses metode atau atribut
      dari kelas induk dalam kelas turunan atau subclass.
"""

# Class induk
class Kendaraan:
  def __init__(self, roda, warna):
    self.roda = roda
    self.warna = warna

  def info(self):
    print(f"Jumlah roda: {self.roda}, Warna: {self.warna}")

# Class turunan
class Mobil(Kendaraan):
  def __init__(self, roda, warna, merk, speed):
    super().__init__(roda, warna)
    self.merk = merk
    self.speed = speed
  
  def turbo(self):
    self.speed += 30

# Membuat objek dari kelas induk
motor = Kendaraan(2, "Merah")

# Membuat objek dari kelas turunan
mobil1 = Mobil(4, "Silver", "Ford", 160)