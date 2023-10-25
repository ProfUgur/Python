#Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılardır.
#Örnek: 1, 4, 8, 99, 101, 363, 4004, 9889, 13531 vb.

#Bu program girilen sayı değerinin palindromik sayı olup olmadığını kontrol eder.

deger = int(input("\nLütfen bir sayı giriniz: "))
deger = str(deger)

if deger == deger[::-1]:
    print(f"\n{deger} palindromik sayıdır")
else:
    print(f"\n{deger} palindromik değildir")