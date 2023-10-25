#Kullanicidan alinan sayinin palindrom olup olmadigini bulan program

sayi = int(input("Bir sayı giriniz: "))

ters = int(str(sayi)[::-1])

if(sayi == ters):
    print(sayi, "palindrom sayıdır")
else:
    print(sayi, "palindrom sayı değildir")



