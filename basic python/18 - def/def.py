#tanpa menggunakan def
nama = []

print ("============================")
nama.append ("ivan")
for data in nama:
    print (data)

print ("============================")
nama.append ("ipin")
for data in nama:
    print (data)

print ("============================")
nama.append ("apin")
for data in nama:
    print (data)

print("========== menggunakan def ==========")

name = []
def listnama():     #==> mendefinisikan code yang akan diulang sehingga membuat penulisan code menjadi lebih muddah
    print ("============================")
    for identitas in name:
        print (identitas)

name.append ("albert")
listnama()
name.append ("alby")
listnama()
name.append ("sky")
listnama()