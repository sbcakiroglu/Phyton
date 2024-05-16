# fonksiyonlar

def toplama(a, b):
    """
    verilan a ve b parametresi için toplama işlemi gerçekleşmiştir.
    """
    return a + b

help(toplama)
x = toplama(2,5)
print(x)

#-----------------------------------

def toplama(x,y):
    return x + y

toplam = toplama(2,4)

print(toplam)

#----args--kwargs--------

def toplama(*args, **kwargs):
    toplam = 0
    for eleman in args:
        toplam = toplam + eleman
    return toplam

toplam = toplama(1,2,3,4,5,6)
print(toplam)