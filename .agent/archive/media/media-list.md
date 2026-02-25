# Media Dosyası Listesi — parlakbeton.com

# Tarih: 2026-02-25

# Kaynak: Sayfa crawl + Wayback Machine arşiv analizi

---

## ÖNEMLİ NOTLAR

- wp-content/uploads/ dizini kamuya açık değil (404 dönüyor)
- Dosyaların tamamı SFTP ile indirilmelidir (CPanel/CyberPanel → Files)
- Alternatif: tüm dosyaları ZIP olarak CyberPanel'den export et

---

## BROŞÜRLER (İndirildi ✅)

| Dosya | Kaynak URL | Boyut | Yerel Kopyası |
|-------|-----------|-------|--------------|
| Parlak-Beton-Zemin-Teknolojileri-Brosur.pdf | /docs/Parlak%20Beton%20Zemin%20Teknolojileri%20-%20Brosur.pdf | 8 MB | content/Parlak-Beton-Zemin-Teknolojileri-Brosur.pdf |
| Parlak-Beton-Mobil-Robot-Brosur.pdf | /docs/Parlak%20Beton%20Zemin%20Teknolojileri%20-%20Mobil%20Robot%20Kullanan%20Fabrikalar%20-%20Brosur.pdf | 18 MB | content/Parlak-Beton-Mobil-Robot-Brosur.pdf |

---

## GÖRSELLER (wp-content — Tespit Edildi, İndirilmeli)

### Broşür Görseli

- `/wp-content/uploads/2024/09/Parlak-Beton-Zemin-Teknolojileri-Brosur-kapak-724x1024.jpg`
- `/wp-content/uploads/2024/09/Parlak-Beton-Zemin-Teknolojileri-Brosur-kapak-724x1024.webp`

### Referans Sayfası Görselleri (Tespit Edilen)

- Debak projesi fotoğrafları
- Garanti İplik fabrika fotoğrafları
- Tedak Elektrik zemin fotoğrafları

### Galeri (hakkimizda/galeri/)

- Beton parlatma uygulama aşaması görselleri
- Farklı endüstriyel alanlarda zemin uygulaması fotoğrafları

---

## WAYBACK MACHINE ARŞİVİ

| Sayfa | Arşiv URL | Tarih |
|-------|-----------|-------|
| Ana Sayfa | <https://web.archive.org/web/20260224233537/https://parlakbeton.com/> | 2026-02-24 |
| Parlak Beton | <https://web.archive.org/save/https://parlakbeton.com/parlak-beton/> | 2026-02-25 |

**Bekleyen:** Tüm kritik sayfaların Wayback arşivinin tamamlanması
→ Manuel: <https://web.archive.org/save/> adresine her URL'yi gir veya
→ Tarayıcıdan: <https://timetravel.mementoweb.org/> kullan

---

## SFTP İLE İNDİRME TALİMATI

```bash
# CyberPanel SSH erişimi ile tüm wp-content indirme:
sftp user@parlakbeton.com
get -r /home/parlakbeton.com/public_html/wp-content/uploads/ ./media-backup/

# Veya rsync ile:
rsync -avz user@parlakbeton.com:/home/parlakbeton.com/public_html/wp-content/uploads/ ./media-backup/
```

**COO Notu:** Medya yedekleme CDO Can sorumluluğunda. Tahmini boyut: 200-500 MB.
