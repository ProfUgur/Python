#Bu program girilen üç sayı değeri arasından en büyüğünü gösterir

birinciSayi = float(input("İlk sayıyı giriniz: "))
ikinciSayi = float(input("İkinci sayıyı giriniz: "))
ucuncuSayi = float(input("Üçüncü sayıyı giriniz: "))

if birinciSayi>ikinciSayi and birinciSayi>ucuncuSayi:
    enBuyuk = birinciSayi
elif ikinciSayi>birinciSayi and ikinciSayi>ucuncuSayi:
    enBuyuk = ikinciSayi
else:
    enBuyuk = ucuncuSayi

print(f"\nEn büyük sayı: {enBuyuk}")