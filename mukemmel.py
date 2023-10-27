#Mükemmel sayı, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayı(Ör:6=1+2+3)
#Bu program kullanıcıdan alınan sayının mükemmel sayı olup olmadığını gösterir

sayi = int(input("\nBir sayı giriniz: "))#Kullanıcıdan bir tamsayı alınır

toplam = 0#Tam bölünen sayıları eklemek için toplam değişkeni oluşturulur
          #Toplamada etkisiz eleman olan 0'a eşitlenir

#1'den sayıya kadar dönen bir döngü oluşturulur
for i in range(1,sayi):
    if sayi % i == 0:#Sayının tam böleni toplama eklenir
        toplam += i

#Toplam ve sayının birbirine eşitliği kontrol edilir
if sayi == toplam:
    print(f"\n{sayi} mükemmel sayıdır")
else:
    print(f"\n{sayi} mükemmel sayı değildir")