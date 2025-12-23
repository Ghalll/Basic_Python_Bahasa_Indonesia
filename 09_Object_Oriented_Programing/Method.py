# Method 
"""
Merupakan perilaku atau tindakan yang dapat dilakukan oleh objek atau kelas
Python membagi method jadi 3 jenis :
  1. Metode dari object (object method)
    ▶️ Adalah method yang melekat pada objek. ciri method ini adanya parameter `self` yang merujuk pada objek saat ini.
  2. Metode secara statis (static method)
    ▶️ Adalah method yang ada pada class bersifat statis. artinya, method ini bersifat indenpenden dan tidak teriakat pada
        instance kelas. Untuk membuat-Nya perlu menambahkan dekorator @staticmethod pada sebelum mendefinisikan method.
  3. Metode dari class  (class method)
    ▶️ Adalah method yang termasuk jenis metode spesial. method ini perlu menambahkan parameter.
        Untuk membuat-Nya perlu menambahkan dekorator @classmethod pada sebelum mendefinisikan method.
"""
# Contoh Object Method
class Car:
  def __init__(self, warna, merk, speed):
    self.warna = warna
    self.merk = merk
    self.speed = speed
  
  def turbo(self):
    self.speed += 100

car1 = Car("merah","supra",180)
print(car1.speed)
car1.turbo()            # Memanggil method turbo
print(car1.speed)

# Contoh Static Method
class Book:
  def __init__(self, penerbit, penulis, halaman):
    self.penerbit = penerbit
    self.penulis = penulis
    self.halaman = halaman
  
  @staticmethod
  def intro():
    print("penulis buku ini adalah")

book1 = Book("Gramedia","Tere Liye", 250)
book1.intro()


# Contoh Class Method
class Duck:
  def __init__(self, gender, usia, nama):
    self.gender =gender
    self.usia = usia
    self.nama = nama
  
  @classmethod
  def swim(cls):
    print("Bebek lagi berenang")