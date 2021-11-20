#For personal use only!

#For cleaning console/Konsolu temizlemek için
import os
import time 
cls = lambda: os.system('cls')

#For input/Girdiyi almak için
print("Choose a language/Bir dil seç! (TR or ENG)")
lang = input().lower()

time.sleep(0.2)
cls()

#For Turkish/Türkçe için
if lang == "tr":
    print("Santimetreden Zurnaya Dönüştürme Aracı \n")
    cm = int(input("Santimetre giriniz: \n"))
    print("Sonuç:", cm / 70)

#For English/İngilizce için
elif lang == "eng":
    print("Centimeter to Zurna \n")
    cm = int(input("Enter Centimeter: \n"))
    print("Result:", cm / 70)

#End of code