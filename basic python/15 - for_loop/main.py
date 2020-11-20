# for biasa digunakan bersama list jika kita ingin menggunakan 
# satu persatu item di dalam list untuk aksi yang sama, 
# mulai dari yang paling simple seperti print 
# atau proses lainnya yang lebih komplek.

user = ["ipan", "ipin", "epin","epun"]

for nama in user:
    print ("user data = ", nama ) 

#forloop akan melakukan perulangan sampai batas akhir data
print("-"*15,"contoh lain","-"*15)
list_hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

for i in list_hari:
    print(i)