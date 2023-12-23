import dask.array as da
import dask
import time

dask_baslangic_zamani = time.time()

# örnek veri kümesi oluştur
veri_kumesi = da.random.random(size=(1000000000,), chunks=1000000)

# Ortalama hesaplama
ortalama = da.mean(veri_kumesi)

# Dask hesaplamasını başlatma
with dask.config.set(scheduler='threads'):
    sonuc = ortalama.compute()

dask_bitis_zamani = time.time()

# Hesaplanan ortalama değeri ekrana yazdırma
print(f"Veri kümesinin ortalaması: {sonuc}")
print(f"Dask ile Ortalama hesaplama süresi: {dask_bitis_zamani - dask_baslangic_zamani} saniye")
