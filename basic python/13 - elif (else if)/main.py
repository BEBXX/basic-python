#penggunaan elif

#kondisi salah
pilihan_menu = input ("pilih menu antara 1-3 : ")
if(pilihan_menu == "1"): 
    print("Anda memilih menu 1")

if(pilihan_menu == "2"): 
    print("Anda memilih menu 2")

if(pilihan_menu == "3"): 
    print("Anda memilih menu 3")

else: print("Menu tidak tersedia")

#kondisi benar
pilihan_menu = input ("pilih menu antara 1-3 : ")
if(pilihan_menu == "1"): 
    print("Anda memilih menu 1")

elif(pilihan_menu == "2"):
     print("Anda memilih menu 2")

elif(pilihan_menu == "3"):
     print("Anda memilih menu 3")

else: print("Menu tidak tersedia")

#else akan berpasangan dengan fungsi if paling akhir
#ketika program dijalankan if statement akan dijalankan secara bersamaan
#sehingga pada kasus diatas jika output = 1 dan 2 maka akan memunculkan juga else dari if ke 3
#maka digunakan fungsi elif diantara if dan else