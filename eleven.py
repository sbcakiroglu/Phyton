#recursive functions= yeniden cagırılan fonksşyon

def faktoriyel(x):
    if x == 1:
        return 1
    else:
        return (x * faktoriyel(x - 1))

sonuc = faktoriyel(3)
print(sonuc)

#lambda expression = isimsiz fonksiyon

isim_soyisim = ['Ali Veli', 'Serkan Tutu', 'Memati Bas', 'Recep Ivedik']
isim_soyisim.sort(key=lambda x: x.split('')[-1].lower())

print(isim_soyisim)

#Filter function = süzgeç

sayi_listesi = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
yeni_liste = list(filter(lambda x:(x % 2 == 0), sayi_listesi)) 

print(yeni_liste)

#map function

liste = [10, 9, 8, 7, 6]

yeni_liste = list(map(lambda x: x * 2 , liste))

print(yeni_liste)
