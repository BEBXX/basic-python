#Tipe data dictonary

data = {"Nama":"Ivan", "Umur":18, "Alamat":"Bekasi"}

#untuk mengakses data dalam dictonary bisa menggunakan key
#key dalam data diatas adalah "Nama", "Umur", "Alamat"

Nama = data["Nama"]
Umur = data["Umur"]
Alamat = data["Alamat"]

#untuk menambahkan data
data ["Profesi"] = "Chef"


for key in data:
    value = data[key]
    print (f"{key}:{value}")

print("==================================")

#untuk menghapus data
del data ["Profesi"]

for key in data:
    value = data[key]
    print (f"{key}:{value}")