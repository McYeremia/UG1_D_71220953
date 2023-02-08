a= int(input("Masukan Angka:"))
for i in range(a):
    print(" " * (a - i - 1), "* " * (i + 1))
for j in range(a):
    print(" " * (j + 1), "* " * (a - j - 1))