# PERNYATAAN CONTINUE
"""
Adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya.
Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.
"""

text = "BARALEK"
for i in text:
    if i == "R":
        continue
    print("Huruf : ", i)
