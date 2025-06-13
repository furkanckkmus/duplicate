dosyanınicindekiler = []
temiz_liste = []
try:
    with open("input.txt", "r", encoding="utf-8") as f:
        for satir in f:
            satir = satir.strip()  # Satır sonundaki boşlukları temizle
            dosyanınicindekiler.append(satir)
    temiz_liste = list(set(dosyanınicindekiler))
    temiz_liste = sorted(temiz_liste)
    
    with open("output.txt", "w", encoding="utf-8") as f:  # encoding parametresini ekleyerek yazma işlemi yapıyoruz
        for i in temiz_liste:
            f.write(i)
            f.write("\n")
    print("İŞLEM BİTTİ")
except Exception as e:
    print(f"Hata oluştu: {e}")  # Hata mesajını yazdırıyoruz
