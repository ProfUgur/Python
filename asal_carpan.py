#Bu program kullanıcıdan alınan sayının asal çarpanlarını gösterir

sayi = int(input("\nBir sayı giriniz:"))#Kullanıcıdan sayı alınır

#Girilen sayının tüm bölenlerinin yazılacağı liste
tum_bolenler = []

#Sayının tüm bölenlerini hesaplayan döngü
for i in range(1,sayi+1):
    if sayi % i == 0:
        tum_bolenler.append(i)
    

#Asal bölenlerin yazılacağı liste
asal_bolenler = []

#Tüm bölenler içinden sadece asal olanları seçmek için aşağıdaki döngü kullanılır
for i in tum_bolenler:
    toplam = 0#Koşul değişkeni oluşturulur

    if i in {0,1}:#i=0 ve i=1 değerleri listeye eklenmez
        continue
    elif i == 2:#Aşağıdaki for döngüsünde toplamı arttırmaması için 2 sayısı listeye önceden eklenir
        asal_bolenler.append(i)
    else:
        for j in range(2,i):#2'den bölen sayıya kadar döngü oluşturulur(her bölen için ayrı bir döngü oluşturulur)
            if i % j == 0:#Eğer bölen başka sayılara da tam bölünüyorsa asal değildir(toplamı 1 arttırır)
                toplam += 1
                break
        if toplam == 0:#for j döngüsünde toplamı arttırmayan değişken listeye eklenir
            asal_bolenler.append(i)

print(asal_bolenler)#Tüm asal çarpanlar eklendikten sonra liste yazdırılır