# Referans Projeler — Parlak Beton A.Ş

Bu dosya; müşteri hikayeleri, referans firma listesi ve proje detaylarını içerir.
İçerik üretimi, web sitesi referans sayfası ve satış sunumları için referans alınır.

---

## Öne Çıkan Endüstriyel Başarı Hikayeleri

### 1. Debak Denizli

- **Web:** debak.com.tr
- **Sektör:** Endüstriyel üretim (1992'den beri sektör lideri)
- **İhtiyaç:** Modern üretim tesisinde sürdürülebilir ve tozsuz zemin
- **Uygulama:** Mekanik elmas silme + lityum silikat kristalizasyon
  (Epoksi gibi kaplama maddesi kullanılmadı)
- **Müşteri yorumu:**
  > *"Uygulamanın üzerinden 6 yıl geçmesine rağmen, zeminler ilk günkü parlaklığını koruyor."*

---

### 2. Garanti İplik

- **Web:** garanti-iplik.com.tr
- **Sektör:** Tekstil — Akdeniz Havzası'nın melanj iplik lideri
- **İhtiyaç:** 7/24 kesintisiz üretimi aksatmayan, sıfır toz standardı
- **Uygulama:** Mekanik elmas aşındırma + yüzey sertleştirme | Aşamalı saha yönetimi
- **Müşteri yorumu:**
  > *"Tekstil üretiminde kritik olan sıfır toz standardı sağlandı. Işığı yansıtma verimliliği artarken, zemin ömrü endüstriyel bazda maksimize edildi."*

---

### 3. Tedak Elektrik

- **Web:** tedak.com.tr
- **Sektör:** Elektrik — Siemens teknoloji partneri
- **İhtiyaç:** Sürdürülebilirlik vizyonuna uygun, çevre dostu, düşük bakım maliyetli zemin
- **Uygulama:** Mekanik parlatma + kristalizasyon, lityum silikat ile yüzey güçlendirme
- **Müşteri yorumu:**
  > *"2016'da tamamlanan bu proje, beton parlatmanın neden epoksi kaplamalara oranla yatırımın geri dönüşü (ROI) en yüksek çözüm olduğunu kanıtlamaktadır."*

---

## Ek Referanslar

| Firma | Alan |
|-------|------|
| Sabiha Gökçen İSG | Havacılık & Güvenlik |
| Kansai Altan | Boya & Kaplama Sanayi |
| Sirmersan Mermer | Mermer & Doğaltaş |

---

## Referans İçin Kullanılacak Metrikler

Bir referans projesi tanımlarken şu verileri ekle:

- Proje tarihi / uygulamadan bu yana geçen süre
- Alan büyüklüğü (m²) — mümkünse
- Uygulanan sistemin adı
- Müşteri yorumu (varsa)
- Sektör & kullanım senaryosu
- Before/After görseli (web sitesine eklenecek)

---

## Referans Sayfası İçin Önerilen Yapı (Web Sitesi)

```
/projeler
├── Filtreleme: Sektör → Fabrika | Tekstil | Enerji | Havacılık | Konut
├── Proje Kartları: Logo + Firma Adı + Sektör + Kısa Sonuç
└── Detay Sayfası: /projeler/[firma-adi]
    ├── Proje hikayesi
    ├── Uygulanan çözüm
    ├── Müşteri yorumu (blockquote)
    └── Fotoğraf galerisi
```
