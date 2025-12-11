# formatting String adalah format cara bagaimana menampilkan teks berdasarkan input
# terdapat 3 metode formatting string
"""
1. F-String => menggunakan 'f' di depan string dan menempatkan variabel dalam kurung kurawal.
2. str.format() => menggunakan metode 'format()' untuk menampilkan string juga menyisipkan nilai kedalam string.
3. %-formatting => menggunakan tanda modulo ('%'), untuk memasukan nilai variabel ke dalam string yang tergantung tipe datanya
"""

name = "Ghaly"

print(f"nama saya {name}")  # metode pertama
print("nama saya {}". format(name))  # metode kedua
print("nama saya %s" % (name))  # metode ketiga

"""
untuk metode ketiga tidak disarankan, karena itu metode lawas pada python versi 2
sekarang python versi 3.11.6
"""
