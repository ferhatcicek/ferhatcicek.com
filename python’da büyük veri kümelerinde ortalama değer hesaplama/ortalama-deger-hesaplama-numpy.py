import numpy as np
import time

# Veri kümesinin ortalamasını bulan fonksiyon
def ortalama_bul(veri_kumesi):
    toplam = sum(veri_kumesi)
    eleman_sayisi = len(veri_kumesi)
    ortalama = toplam / eleman_sayisi
    return ortalama

# veri kümesi oluştur
veri_kumesi = np.random.rand(10000)

# numpy ile ortalama bulma
np_baslangic_zamani = time.time()
np_ortalama = np.mean(veri_kumesi)
np_bitis_zamani = time.time()
print(f"Numpy ile Ortalama hesaplama süresi: {np_bitis_zamani - np_baslangic_zamani} saniye")
print(f"Numpy ile Veri kümesinin ortalaması: {np_ortalama}")


# ortalama_bul fonksiyonunu kullanarak ortalama bulma
fonk_baslangic_zamani = time.time()
fonk_ortalama = ortalama_bul(veri_kumesi)
fonk_bitis_zamani = time.time()
print(f"Fonksiyon Ortalama hesaplama süresi: {fonk_bitis_zamani - fonk_baslangic_zamani} saniye")
print(f"Fonksiyon ile Veri kümesinin ortalaması: {fonk_ortalama}")
