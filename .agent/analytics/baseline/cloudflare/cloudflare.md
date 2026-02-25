# Cloudflare Baseline — parlakbeton.com

## Dönem: 26 Ocak 2026 – 24 Şubat 2026 (30 gün)

**Kaynak:** Cloudflare Analytics → Zone Analytics
**Export tarihi:** 2026-02-25 00:08 UTC

---

## 📊 30 Günlük Özet

| Metrik | Değer | Not |
|--------|-------|-----|
| **Toplam Request** | **~172.625** | Tüm istekler (bot dahil) |
| **Unique Visitors (IP)** | **~16.589** | 30 günlük toplam |
| **Günlük Ort. Visitor** | **~553** | Normal aralıkta |
| **Toplam Bant Genişliği** | **~3,8 GB** | Serve edilen veri |
| **Cache'den Serve** | **~232 MB** | Tüm verinin ~%6'sı |
| **Ortalama Cache Oranı** | **~%7,5** | ⚠️ Çok düşük |

---

## 📅 Günlük Ziyaretçi Tablosu

| Tarih | Unique Visitor |
|-------|---------------|
| 26 Oca | 490 |
| 27 Oca | 508 |
| 28 Oca | 517 |
| 29 Oca | 468 |
| 30 Oca | 522 |
| **31 Oca** | **733** 📈 |
| 1 Şub | 578 |
| 2 Şub | 538 |
| 3 Şub | 563 |
| 4 Şub | 501 |
| 5 Şub | 538 |
| 6 Şub | 634 |
| 7 Şub | 623 |
| 8 Şub | 497 |
| 9 Şub | 444 |
| **10 Şub** | **726** 📈 |
| 11 Şub | 568 |
| 12 Şub | 558 |
| 13 Şub | 606 |
| 14 Şub | 524 |
| 15 Şub | 481 |
| 16 Şub | 566 |
| 17 Şub | 576 |
| **18 Şub** | **727** 📈 |
| **19 Şub** | **798** 📈 Peak |
| 20 Şub | 569 |
| 21 Şub | 418 |
| 22 Şub | 431 |
| 23 Şub | 410 |
| 24 Şub | 532 |

**Pik gün:** 19 Şubat 2026 → 798 ziyaretçi  
**En düşük gün:** 23 Şubat 2026 → 410 ziyaretçi  
**Ort. gün:** ~553 ziyaretçi

---

## ⚠️ Dikkat: Cache Oranı Çok Düşük

Cloudflare cache oranı ortalama **%7,5** seviyesinde — bu WordPress için beklenen bir değer (dinamik sayfalar cache'lenemez). Ancak bu durum şunu gösteriyor:

- Sunucu her istek için PHP/WordPress çalıştırıyor
- TTFB yüksek kalıyor
- Trafik ani yükselimde sunucu görece zor duruma düşüyor

**Astro (SSG) geçişiyle beklenen iyileşme:**

- Cache oranı: %7,5 → **%90+** (statik HTML dosyaları)
- TTFB: ~400ms → **<50ms** (edge'den serve)
- Server yükü: minimuma inecek
- Bant genişliği maliyeti: dramatik düşüş

---

## ⚠️ Bot/Crawler Trafik Şüphesi

Cloudflare'in raporladığı ~553 günlük unique visitor, GA4'ün raporladığı günlük ~4-5 gerçek kullanıcının çok üzerinde. Bu delta şunu gösteriyor:

- **Cloudflare rakamları:** Her IP'yi unique sayar (bot + gerçek)
- **GA4 rakamları:** JavaScript çalıştıran gerçek kullanıcılar
- **Sonuç:** Günlük trafiğin büyük çoğunluğu crawler/bot — bu normal

> GA4 verisi (1.424 oturum/yıl) gerçek insan trafiği için referans alınmalı.
> Cloudflare verisi altyapı kapasitesi planlaması için kullanılmalı.

---

## 📅 Karşılaştırma Geçmişi

| Tarih | Ort. Günlük Visitor | Cache % | Bant Genişliği/gün | Notlar |
|-------|--------------------|---------|--------------------|--------|
| 2026-02-25 | ~553 (Cloudflare IP) | %7,5 | ~127 MB | Baseline — WordPress aşaması |
| _Migration sonrası_ | _TBD_ | _%90+_ | _~10 MB est._ | Astro SSG tahmin |
