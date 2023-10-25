#Bu program girilen boy ve ağırlık değerlerine göre yetişkinlerin beden kitle indeksini hesaplar

boy  = float(input("\nLütfen boyunuzu 'metre' cinsinden yazınız: "))
kilo = float(input("\nLütfen ağırlığınızı 'kilogram' cinsinden yazınız: "))

if boy >= 1.58 and kilo > 45:
    bki = round(kilo/(boy**2))
    if bki<=18.5:
        print(f"\nBeden kitle indeksiniz: {bki}, zayıfsınız")
    elif bki >18.5 and bki < 25:
        print(f"\nBeden kitle indeksiniz: {bki}, normalsiniz")
    elif bki >=25 and bki < 30:
        print(f"\nBeden kitle indeksiniz: {bki}, kilolusunuz")
    elif bki >= 30 and bki < 35:
        print(f"\nBeden kitle indeksiniz: {bki}, obezsiniz")
    else:
        print(f"\nBeden kitle indeksiniz: {bki}, morbid obezsiniz")
else:
    print("\nLütfen vücut değerlerinizi doğru giriniz")