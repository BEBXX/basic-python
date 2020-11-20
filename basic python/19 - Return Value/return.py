#return berguna untuk mengembalikan code program dalam sebuah def

#tanpa return
def jumlahkan(*list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka

    print (f"total {list_angka} = {total}")

jumlahkan (2 , 4, 5)

#menggunakan return
def penjumlahan(*list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka
    return total #mengembalikan "total"

total = penjumlahan (2 , 4, 5)

print (total)