#Kullanicidan alinan 3 sayidan en buyuk sayiyi yazdirir

sayi1 = float(input("Lütfen birinci sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: "))

if((sayi1 > sayi2 ) & (sayi1 > sayi3)):
    buyuk = sayi1
elif((sayi2 > sayi1) & (sayi2 > sayi3)):
    buyuk = sayi2
else:
    buyuk = sayi3

print("En büyük sayı: ", buyuk)