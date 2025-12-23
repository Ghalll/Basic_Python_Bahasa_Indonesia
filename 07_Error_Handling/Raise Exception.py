# 
"""
`raise`
▶️ Adalah statement dalam Python digunakan untuk memicu atau melemparkan pengecualian secara manual.
❗ Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.
"""

# Contoh 
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)