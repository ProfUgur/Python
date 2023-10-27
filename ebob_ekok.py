#Bu program kullanıcıdan alınan iki sayının EBOB ev EKOK unu hesaplar

#Kullanıcıdan iki sayı alınır
birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))
 
 #İki sayıdan küçük olan belirlenir
if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi

#1'den başlanarak küçük olan sayıya kadar tüm ortak bölenler bir döngüyle taranır
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i #Her iki sayıyı bölebilen EBOB değeri(for döngüsünden en son çıkan değer) 
        ekok = (birinciSayi*ikinciSayi)//ebob#İki sayının çarpımı EBOB'a kalansız bölünür
                                             #(İki kez aynı sayıyla çarpılmaması için)       

print ("EBOB:", ebob," EKOK:", ekok)#EBOB ve EKOK değerleri yazdırılır