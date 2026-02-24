---
name: cfo-tr-advisor
description: Use when handling Turkish-specific financial matters including KDV (VAT), e-fatura, e-arşiv, SGK costs, İş-Kur, project-based cash flow, proforma invoice, Turkish tax regulations, or financial modeling for Parlak Beton. Activate with keywords like "KDV", "fatura", "vergi", "nakit akışı", "SGK", "maliyet hesabı", "e-fatura", "CFO Türkiye".
---

# CFO TR Advisor — Türkiye Finansal Çerçevesi

## Parlak Beton Finansal Profili

**Model:** Proje bazlı B2B hizmet (KOBİ)
**KDV Mükellefi:** Evet — %20 KDV (2024 itibari)
**Muhasebe:** Bilanço esası
**Banka:** TL bazlı işlemler öncelikli

---

## Fiyatlama Hesaplama Modeli

### Proje Maliyet Yapısı

```
MALİYET KALEMLERİ (m² başına)
───────────────────────────────
Taşeron işçilik        : X ₺/m²
Malzeme (kimyasal)     : X ₺/m²
Makine amortisman       : X ₺/m²
Seyahat/konaklama      : proje toplam ÷ m²
Genel gider payı (%15) : X ₺/m²
───────────────────────────────
TOPLAM MALİYET         : X ₺/m²

SATIŞ FİYATI           : MALİYET × 2.5-3.5
KDV (%20)              : SATIŞ × 0.20
MÜŞTERİYE FATURA       : SATIŞ + KDV
```

### Nakit Akışı Kuralı (COO onaylı)

```
Küçük proje (< 500K ₺):
  %30 avans → iş başlangıcı
  %70 teslimde

Orta proje (500K - 1M ₺):
  %30 avans → iş başlangıcı
  %40 ara hakediş (50% tamamlanınca)
  %30 teslimde

Büyük proje (> 1M ₺):
  %30 avans → iş başlangıcı
  %30 1. hakediş
  %30 2. hakediş
  %10 kabul sonrası
```

---

## Vergi Yükümlülükleri

| Vergi | Oran | Beyan | Ödeme |
|-------|------|-------|-------|
| KDV | %20 | Aylık (26'sı) | Aylık |
| Gelir/Kurumlar Vergisi | %25 | Nisan | 4 taksit |
| Geçici Vergi | %25 avans | 3 aylık | Dönem sonu |
| Damga Vergisi | %0.948 (sözleşme) | Sözleşmede | İmzada |
| Stopaj (taşeron) | %3 hizmet | Aylık | Muhtasar |

---

## Fatura Sistemi (GİB Uyumu)

### e-Fatura

- Zorunluluk: Yıllık ciro > 3M ₺ veya GİB kapsamına alındıysa
- Sistem: GİB portal veya entegratör (Logo, Mikro, Luca)
- Gönderim: İş tamamlanma + 7 gün içinde

### e-Arşiv

- Zorunluluk: e-Fatura mükellefi olmayanlar için internet satışı
- Fatura içeriği zorunlu: TCKN/VKN, adres, KDV ayrımı

### Proforma Fatura Şablonu

```
PROFORMA FATURA
Tarih: [tarih]
Müşteri: [ticari unvan + VKN]
Proje: [lokasyon] — Beton Parlatma Uygulaması
Alan: [m²]

Hizmet Bedeli:     [tutar] ₺ + KDV
Malzeme Bedeli:    [tutar] ₺ + KDV
KDV (%20):         [tutar] ₺
TOPLAM:            [tutar] ₺

Ödeme Planı:
  %30 Avans: [tarih]
  Kalan: Teslimde

Geçerlilik: 30 gün
```

---

## Taşeron Maliyet Yönetimi

```
Taşeron ödemesi:
  → Alt yüklenici faturası alınmalı (KDV dahil)
  → %3 stopaj kesilir (2 No'lu muhtasar)
  → Ödeme makbuz veya banka havalesi ile belgelenir

SGK kontrolü:
  → Taşeron SGK borcu yoktur yazısı alınmalı
  → Aksi halde iş akdi reddedilir
```

---

## Aylık Finansal Dashboard

Her ay 1'inde üretilecek rapor:

```
GELİR
  Bu ay kesilecek faturalar     : X ₺
  Tahsil edilecek alacaklar     : X ₺
  Toplam beklenen tahsilat      : X ₺

GİDER
  Taşeron ödemeleri             : X ₺
  Malzeme alımları              : X ₺
  Sabit giderler                : X ₺
  Vergi ödemeleri               : X ₺

NET NAKİT POZİSYONU            : X ₺
12 AY PROJEKSİYON HEDEF        : 5.000.000 ₺ net kâr
```

---

## 5M ₺ Hedef Yol Haritası

```
Haftalık takip metrikleri:
  Teklif havuzu toplam değeri   → hedef: 3M ₺+
  Bu ay beklenen tahsilat       → hedef: 1M ₺+
  Dönüşüm oranı (son 30 gün)   → hedef: %25+
  Ortalama proje değeri         → hedef: 400K+ ₺
```
