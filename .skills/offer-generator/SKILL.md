---
name: offer-generator
description: Parlak Beton A.Ş. için müşteri teklifi ve keşif formu hazırlar. Saha verilerini alır, teklif yapısını üretir.
---

# Offer Generator Skill

## Ne Zaman Kullanılır?

- Müşteri keşif sonrası teklif hazırlanacakken
- Standart teklif şablonu gerektiğinde
- CRM şablonlarından teklif e-postası oluşturulacakken

## Teklif Hazırlamak İçin Gereken Veriler

```yaml
musteri:
  firma_adi: ""
  yetkili_adi: ""
  yetkili_unvan: ""
  telefon: ""
  email: ""

proje:
  adres: ""
  toplam_alan_m2: 0
  zemin_mevcut_durum: ""   # iyi / orta / kötü / açıkla
  uygulama: ""             # beton-parlatma / lityum-silikat / zemin-tamiri
  parlaklık_seviyesi: ""   # mat / yarı-parlak / tam-parlak
  ozel_gereksinim: ""

teklif:
  birim_fiyat: 0           # KDV hariç, m² başına
  toplam_kdv_haric: 0
  kdv_orani: 20
  toplam_kdv_dahil: 0
  gecerlilik_gun: 30
  tahmini_sure_gun: 0
```

## Teklif Çıktı Formatı

```markdown
## Proje Teklifi

**Teklif No:** PB-[YIL]-[4 haneli sıra]
**Tarih:** [TARIH]
**Geçerlilik:** [TARIH + 30 gün]

---

**Müşteri:** [Firma Adı]
**Yetkili:** [Ad Soyad] / [Unvan]

---

### Proje Kapsamı

| Alan | m² | Uygulama | Parlaklık |
|------|----|----------|-----------|
| [Adres] | [M²] | [Hizmet] | [Seviye] |

### Uygulama Süreci

[services.md'den ilgili aşamalar özetlenerek eklenir]

### Fiyatlandırma

| Kalem | Birim | Miktar | Birim Fiyat | Toplam |
|-------|-------|--------|-------------|--------|
| [Hizmet] | m² | [M²] | [Fiyat] ₺ | [Toplam] ₺ |

**Ara Toplam (KDV Hariç):** [TUTAR] ₺
**KDV (%20):** [KDV] ₺
**GENEL TOPLAM:** [TOPLAM] ₺

### Notlar

- Fiyata dahil: İşçilik, ekipman, sarf malzemeleri
- Fiyata dahil değil: Mobilya/ekipman taşıma, elektrik bağlantısı
- Ödeme: %30 avans + teslimatta %70

### Garanti

Uygulama, Parlak Beton A.Ş. iş kalite standartlarına uygun tamamlanacaktır.

---

**Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş.**
+90 507 218 5318 | parlakbeton.com
```

## CRM Şablonuyla Birlikte Kullan

Teklif hazırlandıktan sonra `.agent/context/crm.md` içindeki
"Şablon 3 — Teklif Sunumu E-posta" şablonuna entegre et.
