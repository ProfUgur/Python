#Asal sayılar, sadece kendisine ve 1 sayısına kalansız bölünebilen, 1'den büyük sayma sayılarıdır
#Bu program kullanıcıdan alınan sayının asal olup olmadığını söyler

#Kullanıcıdan bir tamsayı alınır
sayi = int(input("\nBir sayı giriniz: "))

#Sayının 1'den büyük olup olmadığı kontrol edilir
if sayi > 1:
    for i in range(2,sayi):#2'den sayıya kadar olan tüm bölenler kontrol edilir
        if sayi % i == 0:#Kalan sıfıra eşitse ikiden fazla böleni vardır, sayı asal değildir
            print(sayi," asal sayı değildir")
            break
    else:#İkiden fazla böleni yoksa sayı asaldır
        print(sayi," asal sayıdır")
else:
    print(sayi," asal sayı değildir")