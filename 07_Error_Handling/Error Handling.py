# BLOK PENANGANAN KESALAHAN 
"""
Error Handling :
  ▶️ Adalah pendekatan dalam pemrograman untuk mengantisipasi, mendeteksi, dan menangani kesalahan
      yang mungkin terjadi selama eksekusi program.
  ▶️  Tujuan dari error handling adalah untuk menjaga program tetap berjalan bahkan ketika terjadi kesalahan,
      dan memberikan respons yang sesuai terhadap situasi tersebut.  
⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔

  Dalam Python, Error Handling menggunakan blok `try`,`except`,`else`,dan `finally`.
  Berikut penjelasan tiap statement nya :

  try:
    # Blok kode yang mungkin terjasi error.
  except:
    # Pernyataan yang dioperasikan jika terjadi error.
  else:
    # Pernyataan yang dioperasikan jika TIDAK terjadi error.
  finally:
    # Pernyataan yang operasikan setelah semua pernyataan di atas terjadi.

"""

# CONTOH
var_dict = {"rata_rata": "1.0"}
try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

# Contoh lain
try:
    # Potensi kode yang dapat menyebabkan kesalahan
    result = 10 / 0
except ZeroDivisionError:
    # Blok yang akan dieksekusi jika terjadi ZeroDivisionError
    print("Error: Pembagian dengan nol tidak diizinkan.")
except Exception as e:
    # Blok yang akan dieksekusi untuk kesalahan umum lainnya
    print(f"Error: {e}")
else:
    # Blok yang akan dieksekusi jika tidak ada kesalahan
    print("Tidak ada kesalahan.")
finally:
    # Blok yang akan dieksekusi setelah try block selesai, terlepas dari kesalahan
    print("Eksekusi selesai.")
