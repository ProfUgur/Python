#Bu program girilen yarıçap değerine göre dairenin alanını ve çevresini hesaplar
#Pi sayısı 3.14 olarak belirlenmiştir

yaricap = float(input("\nLütfen dairenin yarıçap değerini giriniz: "))
pi = 3.14
if yaricap > 0:
    alan = round(pi*(yaricap**2))
    cevre = round(2*pi*yaricap)
    print(f"\nDairenin alanı {alan} cm2 ve çevresi {cevre} cm'dir")
else:
    print("\nLütfen yarıçap değerini 0'dan büyük giriniz")