import re

def metin_ifadesinden_dakika_hesapla(metin_ifadesi):
    if not isinstance(metin_ifadesi, str)  or metin_ifadesi == "":      
        return None
    
    zaman_birimleri = {}

    for birim, desen in desenler.items():
        eslesme = desen.search(metin_ifadesi)
        zaman_birimleri[birim] = int(eslesme.group(1)) if eslesme else 0

    toplam_dakika = sum(zaman_birimleri[birim] * dakika_donusturme[birim] for birim in zaman_birimleri)

    return int(toplam_dakika)


desenler = {
    'YIL': re.compile(r'(\d+)\s*[Yy][İiIi][Ll]', re.I),
    'AY': re.compile(r'(\d+)\s*[Aa][Yy]', re.I),
    'HAFTA': re.compile(r'(\d+)\s*[Hh][Aa][Ff][Tt][Aa]', re.I),
    'GUN': re.compile(r'(\d+)\s*[Gg][ÜuUu][Nn]', re.I),
    'SAAT': re.compile(r'(\d+)\s*[Ss][Aa][Aa][Tt]', re.I),
    'DAKIKA': re.compile(r'(\d+)\s*[Dd][Aa][Kk][İiIi][Kk][Aa]', re.I),
    'SANIYE': re.compile(r'(\d+)\s*[Ss][Aa][Nn][İiIi][Yy][Ee]', re.I)
}

dakika_donusturme = {
    'YIL': 365 * 24 * 60,
    'AY': 30 * 24 * 60,
    'HAFTA': 7 * 24 * 60,
    'GUN': 24 * 60,
    'SAAT': 60,
    'DAKIKA': 1,
    'SANIYE': 1 / 60
}


text = "3 yıl 4 ay 5 gün 10 dakika"

print(f"\"{text}\" zaman verisi toplam {metin_ifadesinden_dakika_hesapla(text)} dakikadır")
