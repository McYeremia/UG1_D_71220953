print('---------- Nilai ke 1 ---------')
a1=int(input('Nilai Harian:'))
a2=int(input('Nilai UTS: '))
a3=int(input('Nilai UAS: '))

print('---------- Nilai ke 2 ---------')
b1=int(input('Nilai Harian:'))
b2=int(input('Nilai UTS: '))
b3=int(input('Nilai UAS: '))

tugas=((a1+b1)*(30/100))
uts=((a2+b2)*(30/100))
uas=((a3+b3)*(40/100))
hasil=round((tugas+uts+uas)/2,0)

print('--------- Total Nilai -------')
print('Total Nilai yang didapat :', hasil)
if hasil >= 80:
    print('Total nilai dalam huruf: A')
elif hasil >= 60:
    print('Total nilai dalam huruf: B')
elif hasil >= 40:
    print('Total nilai dalam huruf: C')
elif hasil >= 20:
    print('Total nilai dalam huruf: D')
elif hasil >= 0:
    print('Total nilai dalam huruf: E')