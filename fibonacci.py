#İlk 20 Fibonacci sayısını gösteren program

#Elemanların ekleneceği boş bir liste oluşturulur
sayilar = []

#Fibonacci hesaplama fonksiyonu
def fibonacci(a):
    if a in {0,1}:#İlk iki değerin "1" olması sağlanır(İlk değer belirtilmezse fonksiyon hata verir)
        return 1
    return fibonacci(a - 1) + fibonacci(a - 2)#Her fonksiyon kendinden önceki iki fonksiyon sonucunun toplamı

#Fonksiyonu 20 kez çağıran döngü oluşturulur
for i in range(20):
    sayilar.append(fibonacci(i))#Her bir döngüden elde edilen eleman listeye sırayla eklenir

print(sayilar)#Tüm elemanlar eklendikten sonra liste yazdırılır