#while loop digunakan ketika kondisi boolean bernilai true sampai kondisi bernilai false

print("-"*15,"contoh 1","-"*15)

count = 0
while count < 2:
    print(count)
    count = count + 1
print('Selesai')
#perulangan akan selesai jika tidak memenuhi kondisi yang ditentukan
#dalam kasus ini kondisi adalah "count < 2"



#kombinasi WHILE dan INPUT
print("-"*15,"contoh 2","-"*15)

nama = ""
while nama != "admin":
    nama = input("input nama anda : ")
#dalam kasus ini fungsi input akan terus diulang
#jika user tidak menginput "admin" perulangan tidak akan berhenti


#kombinasi WHILE dan IF ELSE
print("-"*15,"contoh 3","-"*15)

x = 1
jlh_genap = 0
jlh_ganjil = 0
while x <= 10:
    if x % 2 == 0:
        jlh_genap = jlh_genap + x
    else:
        jlh_ganjil = jlh_ganjil +x
    x = x + 1

#dalam kasus ini hasil perulanga akan dimasukkan kembali di fingsi while
#sampai hasil dari perulangan tidak memenuhi kondisi yang ditentukan

print("Jumlah bilangan genap dari 1-10 adalah :", jlh_genap)
print("Jumlah bilangan ganjil dari 1-10 adalah :", jlh_ganjil)



#kombinasi WHILE dan Range
print("-"*15,"contoh 4","-"*15)

for i in range(10):
    print("ipan baik banget")

#dalam kasus ini perulangan akan dilakukan sebanyak 9 kali
#karena yang diminta "range(10)"
#yang dimana 10 ini sebagai stop 
#dalam range diakhiri dengan stop-1 jadi 10 - 1 = 9 jadi akan stop di 9