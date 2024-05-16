#tuple: listelere benzer ama tuple'da verileri değiştiremezsin

sayilar = tuple()

print(type(sayilar))

#--------------------

sayilar = (1, 2, 45, 87, 123, 543)

for i in sayilar:
    print(i)
    
# print(sayilar)

isim, soyisim, yas = ('ali', 'veli', 23)

print(isim)
print(soyisim)
print(yas)