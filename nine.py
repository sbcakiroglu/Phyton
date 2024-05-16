#sets/kümeler

alacaklar = set()

alacaklar.add('araba')
alacaklar.add('ev')
alacaklar.add('kitap')

alacaklar.remove('araba') # set içinden eleman silme
#alacaklar.clear() # set içindeki tüm veriyi silme

print(alacaklar)

#-----------örnek-----------------------

tek_sayilar = set([1, 3, 5, 7, 9])
cift_Sayilar = set([2,4,6,8])
asal_sayilar = set([2,3,5,7])
# çiftlerle tekleri birleştirip yazdırma
print(tek_sayilar.union(cift_Sayilar))
# asal sayılarla tek sayıların kesişimi
print(tek_sayilar.intersection(asal_sayilar))