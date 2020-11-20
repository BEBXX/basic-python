# SOAL 1
# ----- 0 ++++++ 5 ----- 8 +++++ 11 -----
print ("\n"," ======= SOAL 1 =======","\n")
inputUser = float(input("masukkan angka: "))

#1st step ------0++++++5-------
isA = (inputUser > 0)
print ("Lebih Dari 0 =", isA)

isB = (inputUser < 5)
print ("Kurang Dari 5 =", isB)

isBenar = isA and isB


#2nd Step ------8+++++++11--------
isC = (inputUser > 8)
print ("Lebih Dari 8 =", isC)

isD = (inputUser < 11)
print ("Kurang Dari 11 =", isD)

isCorrect = isC and isD

#3rd Step Penggabungan


isHasil = isBenar or isCorrect
print ("Hasil Dari Soal NO 1 Adalah:", isHasil)

# SOAL 2
# ++++0----5++++8----11+++++
print ("\n"," ======= SOAL 2 =======","\n")
inputUser = float(input("masukkan angka: "))

#1st step +++++0
isA1 = (inputUser < 0)
print ("Kurang Dari 0 =", isA1)

#2nd Step ------5+++++++8--------
isB1 = (inputUser > 5)
print ("Lebih Dari 5 =", isB1)

isC1 = (inputUser < 8)
print ("Kurang Dari 8 =", isA1)

isBenar1 = isB1 and isC1

#3rd step 11+++++++
isD1 =(inputUser > 11)
print ("Lebih Dari 11=", isD1)

#4TH step penggabungan 
ishasil2 = isA1 or isBenar1 or isD1
print ("Hasil Dari Soal NO 2 Adalah:", ishasil2)





#cara cepat menggunakan fungsi IF
print ("\n"," ======= CARA CEPAT SOAL 1=======","\n")
inputUser = float(input("masukkan angka: "))

if(inputUser>0 and inputUser<5) or (inputUser>8 and inputUser<11):  print ("true")
else:  print ("false")

print ("\n"," ======= CARA CEPAT SOAL 2=======","\n")
inputUser = float(input("masukkan angka: "))

if(inputUser<0) or (inputUser>5 and inputUser<8) or (inputUser>11):  print ("true")
else:  print ("false")




print ("\n"," ======= SELESAI =======","\n")

