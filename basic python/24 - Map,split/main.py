a, b, c, d = map(int, input("masukkan angka: ").split())
if ((a >= 2) or (8-a == 4)):
    a = a*a + 1
else:
    a = 0
if ((b >= 2) or (8-b == 4)):
    b = b*b + 1
else:
    b = 0
if ((c >= 2) or (8-c == 4)):
    c = c*c + 1
else:
    c = 0
if ((d >= 2) or (8-d == 4)):
    d = d*d + 1
else:
    d = 0
print(a+b+c+d)