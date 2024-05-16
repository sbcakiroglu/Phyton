# for döngüsü sayesinde bir liste içerisindeki tüm elemanlara erişim sağlayabiliyoruz.

rakam_listesi = [1,3,7,8,9]

total = 0

for rakam in rakam_listesi:
    total = total + rakam
print(total)    

#--100'e kadar sayıları yazdır
for item in range(100):
    print(item)

#--100'e kadar olan tüm çift sayıları yazıdr
for sayi in range(100):
    if sayi % 2 == 0:
        print(sayi)

#--100'e kadar olan tüm tek sayıları yazıdr
for sayi in range(100):
    if sayi % 2 == 1:
        print(sayi)  

#- bir iismdeki tüm harfleri ayrı ayrı yazdırma
isim = "mustafa"

for harf in isim:
    print(harf)          