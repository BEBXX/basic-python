#break
#kata kunci ini dugunakan untuk menghentikan looping

for i in range(1,21):
    if i % 10 == 0:
        break    
    print (i)       
#pada kasus ini break akan menghentikan looping
#sampai data i pertama yang habis dibagi 10

print ("========== Contoh Lain ==========")

#contoh dalam penggunaan while loop
while True:
    nama = input("input nama anda : ")
    if nama == "ivan":
        break

#while loop digunakan ketika kondisi boolean bernilai true 
#sampai kondisi bernilai false atau dihentikan dengan kata kunci "break"