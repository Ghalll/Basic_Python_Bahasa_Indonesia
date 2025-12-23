# PARAMETER
"""
Menurut dokumentasi resmi Python, ada 5 jenis parameter 
  1. Positional-or-Keyword
  ▶️ Jenis ini merupakan parameter default dalam Python. Dengan jenis ini,
      dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.
  2. Positional-Only
  ▶️ Parameter ini hanya dapat dimanfaatkan dengan menggunakan jenis argumen posisi saat pemanggilan fungsi.
      Parameter ini ditentukan menggunakan sintaks "/".
  3. Keyword-Only
  ▶️ Parameter yang mengharuskan menggunakanya dengan keyword argument untuk memanggil fungsi dengan jenis parameter ini.
      Ditentukan dengan sintaks "*" (asterisk).
  4. Var-Positional (Variadic Positional Parameter)
  ▶️ Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi.
      Parameter ini ditentukan dengan menggunakan sintaks *args.
  5. Var-Keyword (Variadic Keyword Parameter)
  ▶️ Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi.
      Parameter ini # dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya).
    
"""

# Positional-or-Keyword


def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting("Programing", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Programing"))

# Posiotional-Only


def penjumlahan(a, b, /):
    return a + b


print(penjumlahan(8, 50))

# Keyword-Only


def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan


print(greeting(pesan="Selamat sore!", nama="Programing"))

# Var-Posiotional (Variadic Posiotional Parameter)


def tambah(*args):
    total = sum(args)
    return total


print(tambah(1, 2, 3, 4, 5, 6))

# Var-Keyword (Variadic Keyword Parameter)


def infodata(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info


print(infodata(nama="Ghaly", Pekerjaan="Mahasiswa", Asal="Pekanbaru"))
