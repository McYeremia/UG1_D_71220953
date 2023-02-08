print('========== KASIR ==========')
while True:
    a = int(input('Harga Barang:'))
    pil = str(input('Apakah anda membeli barang lagi? [yes/no]'))
    a += a
    if pil == 'yes':
        print( )
    elif pil == 'no':
        print( )
        print('TOTAL BELANJA: ', a)
        break
    else:
        print('INVALID')
        break