#membuat list
nama_kosong = [] #contoh list kosongan
nama = ["ipan","ipin","epin"] #contoh sudah terisis

print (nama)

#menambahkan data ke list
nama.append ("apin")

print (nama , "\n")

#index list selalu dimulai dari angka 0
nama [0] 
nama [1] 
nama [2]
nama [3]

print (nama [0])
print (nama [1])
print (nama [2])
print (nama [3] , "\n")

#menghapus nama dari list (akan mengubah index list)
nama.remove ("ipin") #ipin adalah index ke 1
print (nama [1], "\n") #index 1 berubah menjadi epin yg sebelumnya index ke 2

#mengubah data dilist
nama [0] = "albert"
print (nama [0])