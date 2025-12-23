# ARRAY PADA PYTHON ADALAH LIST
"""
Python tidak memiliki tipe data array. Sebaliknya, Python memiliki tipe data list yang dapat dikatakan mirip, tetapi tak sama dengan array.
Perbedaan yang menonjol adalah cara array menyimpan nilai sangat berbeda dengan list. Pada array, nilai di dalamnya 
memiliki tipe data yang sama. Namun, pada list, nilai di dalamnya tidak harus memiliki tipe data yang sama. 
"""

# Contoh list
x = [1,2,3,4,5]
var_list = [1, "Progaming", True, 1.0]


# Namun array dapat digunakan di Python dengan cara menklarasikan menggunakan library atau modul Python.
import array
num = array.array("i",[1, 2, 3, 4, 5])
print(num)
print(type(num))