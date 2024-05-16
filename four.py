# while(iken) döngüsü

while sayi <= 5:
    print(sayi)
    sayi = sayi + 1
else:
    print(sayi) 
    
# continue ve break

baslangic = 0

while baslangic < 10:
    baslangic = baslangic + 1
    if baslangic % 2 == 0:
        continue #atla
    print(baslangic)
    
#-----------------------------

while True:
     alinan = input('isim giriniz:')
     if alinan == 'cikis':
         break #kır
     print(alinan)   