
dosyanınicindekiler = []
temiz_liste = []
with open("input.txt","r")as f:
    for satir in f:
        satir = satir.strip()  # Satır sonundaki boşlukları temizle
        dosyanınicindekiler.append(satir)
temiz_liste = list(set(dosyanınicindekiler))
temiz_liste = sorted(temiz_liste)
with open("output.txt","w")as f:
    for i in temiz_liste:
        f.write(i)
        f.write("\n")
print("İŞLEM BİTTİ")