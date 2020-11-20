#continue
#kata kunci ini berguna untuk meng-skip proses dalam looping

#mengskip data yang bernilai genap
for i in range(1,21):
    if i % 2 == 0: # ==> jika data i kalau dibagi sampai habis akan bernilai 0 maka dinyatakan genap
        continue   # ==> continue hanya akan dijalankan pada data bernilai True atau dlm kasus ini genap
    print (i)      # ==> maka data bernilai genap akan diskip dan yang dimunculkan data bernilai ganjil

print ("=================================")

#mengskip data yang bernilai ganjil
for i in range(1,21): 
    if i % 2 == 1: # ==> jika data i kalau dibagi sampai habis akan bernilai 1 maka dinyatakan ganjil
        continue   # ==> continue hanya akan dijalankan pada data bernilai True atau dlm kasus ini ganjil
    print (i)      # ==> maka data bernilai ganjil akan diskip dan yang dimunculkan data bernilai genap
