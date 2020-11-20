#contoh pergunnan argumen list pada def
#argument list hanya bisa ditaruh di paling belakang dan hanya bisa 1 dalam def


def penjumlahan(*list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka

    print (f"total {list_angka} = {total}")

penjumlahan (2 , 4, 5)

#jika ingin menambahkan argument value lainnya harus ditaruh dipaling depan
#contoh

def jumlahkan(nomer, *list_angka): 
    total = 0
    for angka in list_angka:
        total = total + angka

    print (f"total {list_angka} = {total}")

jumlahkan (2 , 4, 5)
#dalam kasusu ini 2 akan masuk ke argument value nomer sehingga tidak ikut dijumlahkan