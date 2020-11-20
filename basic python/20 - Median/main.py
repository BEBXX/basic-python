data = [4, 2, 1, 3] #data di dalam list
data.sort () #mengurutkan data dari yg terkecil [1, 2, 3, 4]

if len(data) % 2 == 0:
    median1 = data[len(data) // 2]
    median2 = data[len(data) // 2 - 1]
    
    median = (median1 + median2) / 2

else:
    median = data[len(data) // 2]

print(len(data))

print(median)