#Kullanicidan alinan maas ve zam orani ile yeni maas hesaplanmasi

maas = float(input("Maaşınızı giriniz :"))
zam_orani = float(input("Zam oranını giriniz :"))

yeni_maas = ( maas * zam_orani/100 ) + maas
print(yeni_maas)
