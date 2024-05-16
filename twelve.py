#unpacking

def toplam(a, b, c, d):
    return a + b + c + d

sayilar = [1, 2, 3, 4]

sonuc = toplam(*sayilar)

print(sonuc)

#packing

def toplam(*args):
    print(args)
    
toplam(1, 2, 3, 4, 5, 6, 7, 8, 9)

#--------

def toplam(*args, **kwargs):
    print(args)
    print(kwargs)

toplam(1,2,3, isim = 'Ali', soyisim= 'Veli')

#------------

def yazdir(isim, soyisim):
    print(isim)
    print(soyisim)
kisi = {'isim': 'ali', 'soyisim': 'veli'}    
yazdir(**kisi)