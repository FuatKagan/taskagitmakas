#Taş Kağıt Makas Oyunu    random.randomchoice()

import random as r
import time as t

skor = 0

eller = ["kağıt", "taş", "makas"]

print("Taş-Kağıt-Makas Oyununa Hoşgeldiniz!", "\n", 100*"*")
sayac = ["Taş", "Kağıt", "Makas"]
a = 0
for i in range(5):
    while a < 3:
        t.sleep(0.7)
        print(sayac[a], end = " ")
        a += 1
    t.sleep(0.5)
    print("\nTahminimi yaptım! Şimdi sen de yap")
    t.sleep(1)
    cvp = input("Tahminin: ")
    sonuc = r.choice(eller)
    if cvp.lower() == eller[0]:
        print("Berabere")
    elif cvp.lower() == "taş" and sonuc == "kağıt":
        print("Ben Kazandım!!")
    elif cvp.lower() == "kağıt" and sonuc == "makas":
        print("Ben Kazandım!!")
    elif cvp.lower() == "makas" and sonuc == "taş":
        print("Ben Kazandım!!")
    else:
        print("Sen Kazandın...")
        skor += 1

print(f"Skorun: {skor}/5")