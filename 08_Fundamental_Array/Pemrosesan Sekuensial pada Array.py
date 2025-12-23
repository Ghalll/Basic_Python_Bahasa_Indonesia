# Pemrosesan Sekuensial pada Array.
# Pemrosesan sekuensial lebih sering menggunakan pengulangan (loop/iterasi) dalam setiap prosesnya.
"""
Pemrosesan array merujuk kepada operasi-operasi yang dilakukan pada elemen-elemen suatu array.
Operasi ini melibatkan manipulasi hingga pengolahan elemen yang ada pada array. 
"""

myarr = [10,20,30,40,50,60]
for i in range(len(myarr)):
  current = myarr[i]
  next = i + 1

  if next < len(myarr):
    next = myarr[next]
  else:
    next = None

    print(f"Current element: {current}, next elements: {next}")