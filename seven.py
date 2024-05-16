#dictionaries

person = {
    'isim': 'ali',
    'soyisim': 'yilmaz',
    'yas': 23
    
}

person['color'] = 'red' #dict içine obje ekleme
print(person['soyisim']) #sözlüğün içinden spesifik bir key'i kullanarak görüntüleme

#eğer person dict' içinde yemek key'i varsa karşılık geleni getrir yoksa alttakini yazdır
if "yemek" in person:
    print(person['yemek'])
else:
    print('Bu keye karışılık bir value bulunamadı.')



#print(dir(person)) --> person dict'i içinde hangi fonksiyonları kulalnabilirim

#print(help(person.get)) --> bu fonksiyonun nası çalıştıgı hakkınd ayardım et

#print(type(person))

person_2 = {
    'isim': 'enes',
    'soyisim': 'sahin',
    'yas': 42
}


name = "ali"
surname = "yilmaz"

name_2 = "enes"
surname= "sahin"