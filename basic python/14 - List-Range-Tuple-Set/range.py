## nama = [1,2,3,4,5,6,7,8,9,10] #contoh data dalam list

## data dalam range

data = range(1, 11) #format (batas bawah, batas akhir + 1)

for no in data:
    print (no)

print ("======================================")

#atau bisa juga

for nomor in range(11, 21):
    print (nomor)

a = [1, 2, 3]       # terbentuk sebuah list dengan 3 item
print(a)
print(type(a))      # terlihat bahwa type data a adalah list


b = range(4)        # akan terbentuk range dengan 3 item yaitu 0, 1, 2
print(b)            # menampilkan objek range
print(list(b))      # untuk menampilkan isi, kita perlu ubah menjadi type list

c = range(10, 0, -1) # (start, stop, step)
print(list(c))