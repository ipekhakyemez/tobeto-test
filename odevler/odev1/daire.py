#Dairenin alani ve çevresini hesaplama

r = float(input("Yarıçapı giriniz: "))

import math
alan = (math.pi * r ** 2)
cevre = (math.pi * 2 * r)

print("Dairenin alanı: ", alan)
print("Dairenin çevresi: ", cevre)