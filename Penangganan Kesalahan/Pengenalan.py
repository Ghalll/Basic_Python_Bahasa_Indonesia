# Penanganan Kesalahan (Error Handling and Exception Handling)
"""
Dua jenis kesalahan berdasarkan kejadiannya : 
1). Kesalahan Sintaks (Syntax Errors)
  ▶️ Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda.
      Hal ini terjadi ketika pemformatan indentasi pada kode Python tidak sesuai atau tidak konsisten. Python menggunakan
      indentasi (spasi atau tab) untuk menentukan blok kode, dan setiap blok kode harus memiliki indentasi yang konsisten. 

2). Pengecualian (Exceptions)
  ▶️ Pengecualian adalah kesalahan yang terjadi ketika Python mengerti perintah Anda, tetapi mendapatkan masalah saat mengikutinya.
      Pengecualian (exceptions) dalam Python merujuk pada situasi-situasi yang dapat menyebabkan kesalahan pada saat runtime.
      Ketika suatu pengecualian terjadi, Python akan menghentikan eksekusi program dan mencari blok kode yang dapat
      menangani pengecualian tersebut.
"""

# Contoh Indentation Error 
for i in range(5):
print(i)  # Ini akan menyebabkan IndentationError karena kurangnya indentasi pada baris ini
