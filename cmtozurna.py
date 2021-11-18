#For personal use only!

#For cleaning console/Konsolu temizlemek için
import os
import time 
cls = lambda: os.system('cls')
#

#For input/Girdiyi almak için
print("Choose a language/Bir dil seç! (TR or ENG) ")
lang = input().lower()

time.sleep(0.2)

#For Turkish/Türkçe için
if lang == "tr":
    print("Santimetreden Zurnaya Dönüştürme Aracı")
    print(" ")
    cm = int(input("Santimetre giriniz: "))
    print(" ")
    print("Sonuç:", cm / 70)

#For English/İngilizce için
elif lang == "eng":
    print("Centimeter to Zurna")
    print(" ")
    cm = int(input("Enter Centimeter: "))
    print("")
    print("Result:", cm / 70)

#End of code