import numpy as np
import time

# Veri kümesinin boyutu ve parça boyutu
veri_boyutu = 1000000000
parca_boyutu = 100000

# Ortalamaları saklamak için bir liste oluştur
ortalama_listesi = []

np_baslangic_zamani = time.time()

# Veri kümesini parçalara böl ve her parçanın ortalamasını hesapla
for _ in range(veri_boyutu // parca_boyutu):
    veri_kumesi = np.random.rand(parca_boyutu)
    ortalama = np.mean(veri_kumesi)
    ortalama_listesi.append(ortalama)

# Tüm parçaların ortalamasını hesapla
genel_ortalama = np.mean(ortalama_listesi)
np_bitis_zamani = time.time()

print(f"Veri kümesinin genel ortalaması: {genel_ortalama}")
print(f"Ortalama hesaplama süresi: {np_bitis_zamani - np_baslangic_zamani} saniye")
