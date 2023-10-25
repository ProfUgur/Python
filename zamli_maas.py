#Bu program çalışma sürenize göre zamlı maaşınızı hesaplar
#Maaş zam değerleri 0-5 yıl için %10, 6-10 yıl için %20, 11 yıl ve üzeri için %30 olarak belirlenmiştir

isim = input("Adınızı giriniz: ")
maas = int(input("Maaşınızı giriniz: "))
yil = int(input("Çalışma sürenizi yıl olarak giriniz: "))
zam = 0
if maas > 0 and yil >0:
    if yil <= 5:
        zam = maas*10/100
    elif yil >5 and yil < 11:
        zam = maas*20/100
    else:
        zam = maas*30/100

    print(f"{isim} Bey/Hanım, zamlı maaşınız: {int(maas+zam)}")
else:
    print("Lütfen maaş veya yıl değerlerinizi doğru giriniz")