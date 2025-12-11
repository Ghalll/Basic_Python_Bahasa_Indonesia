# Percabangan Kondisional (`if`, `else`, `elif`):

#⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔
"""
Contoh Studi kasus:
"Setiap hari, Ibu selalu pergi ke pasar untuk membeli bahan makanan. Ibu selalu mengutamakan
untuk membeli daging ayam di pasar. Jika daging ayam tidak tersedia, maka Ibu akan membeli
tempe sebagai pengganti, lalu memasaknya."
"""
ketersediaan = "Daging Ayam"
if ketersediaan == "Daging Ayam":
  print("Ibu membeli dan memasak ayam")
else:
  print("Ibu membeli dan memasak tempe")


# contoh lain
x = 10
if x > 0:
    print("x adalah bilangan positif.")
elif x == 0:
    print("x adalah nol.")
else:
    print("x adalah bilangan negatif.")


