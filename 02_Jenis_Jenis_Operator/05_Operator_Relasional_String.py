# OPERATOR RELASIONAL PADA STRING
"""
Operator relasional untuk tipe data string pada Python berfungsi untuk membandingkan dua string 
dan mengembalikan nilai kebenaran berdasarkan hasil perbandingan tersebut
"""
# ⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔
"""
▶️ Sama dengan `(==)` : Menghasilkan True, jika kedua string memiliki nilai yang identik/sama persis.
▶️ Tidak Sama dengan `(!=)` : Menghasilkan True, jika kedua string memiliki nilai yang tidak sama.
▶️ Lebih Besar dari `(>)` : Menghasilkan True, jika huruf pertama pada string pertama lebih BESAR dari huruf pertama pada string kedua dalam urutan alfabet.
▶️ Kurang dari `(<)` : Menghasilkan True, jika huruf pertama pada string pertama lebih KECIL dari huruf pertama pada string kedua dalam urutan alfabet. 
▶️ Lebih Besar dari Sama dengan `(>=)` : 
    Menghasilkan True, jika huruf pertama pada string pertama lebih besar atau sama dengan dari huruf pertama pada string kedua dalam urutan alfabet. 
▶️ Kurang dari Sama dengan `(<=)` :
    Menghasilkan True, jika huruf pertama pada string pertama lebih kecil atau sama dengan dari huruf pertama pada string kedua dalam urutan alfabet. 
"""

x = "Programing"
y = "Indonesia"

print(x == y)   # false
print(x != y)   # true
print(x > y)    # false
print(x < y)    # true
print(x >= y)   # false
print(x <= y)   # true
