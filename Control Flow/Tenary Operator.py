# TENARY OPERATOR
# Yaitu menulis percabangan kondisional dalam satu baris kode
# ⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔
"""
Syntaxnya :
nilai_jika_true if kondisi else nilai_jika_false
"""

x = 5
num = "Bilangan positif" if x > 0 else "Bilangan negatif"
print(num)

lulus = False
ket = "Selamat" if lulus else "Tidak lulus"
print(ket)

# TENARY OPERATOR DENGAN TUPLES
nilai = 80
keterangan = ("Nilai dibawah 85", "Sangat Baik Grade : A")[nilai > 85]
print(keterangan)
