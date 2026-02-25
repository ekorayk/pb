# Bing Webmaster Baseline — parlakbeton.com

## Export tarihi: 25 Şubat 2026

**Kaynak:** Bing Webmaster Tools

---

## 📊 Arama Performansı (1 yıl: Şub 2025 – Şub 2026)

| Metrik | Değer |
|--------|-------|
| **Toplam Tıklama** | **7** |
| **Toplam Gösterim** | ~550 |
| **Ortalama CTR** | ~%1,3 |

> **Değerlendirme:** Bing'den gelen trafik son derece düşük. Google'ın ~275 tıklamasına karşılık Bing yalnızca 7 tıklama üretmiş. Türkiye'de Bing pazar payı düşük (~%3), bu beklenen bir tablo.

### Tıklama Olan Günler

| Tarih | Tıklama | CTR |
|-------|---------|-----|
| 01 Mar 2025 | 1 | %20 |
| 12 Mar 2025 | 1 | %33 |
| 14 May 2025 | 1 | %25 |
| 26 May 2025 | 1 | %25 |
| 27 Kas 2025 | 1 | %33 |
| 18 Ara 2025 | 1 | %100 |
| 26 Ara 2025 | 1 | %33 |

### Pik Gösterim

- **29 Nisan 2025:** 117 gösterim (olağandışı spike — muhtemelen bot tarama)
- **3 Eylül 2025:** 14 gösterim

---

## 🤖 Bing AI (Copilot) Performansı

**Dönem:** 25 Kasım 2025 – 22 Şubat 2026

| Metrik | Değer |
|--------|-------|
| Citations (AI Alıntı) | **1** |
| Cited Pages | **1** |
| Alıntı tarihi | **16 Şubat 2026** |

> Bing Copilot, 16 Şubat 2026'da parlakbeton.com'dan bir sayfayı **AI yanıtında kaynak olarak kullandı**. Bu erken bir AI SEO sinyali — yeni içeriklerle Copilot'ta görünürlük artırılabilir.

---

## 🗺️ Sitemap Durumu

| Site Haritası | Durum | Son İşlenme |
|--------------|-------|-------------|
| /sitemap_index.xml | ⚠️ **HATA** | 21 Şubat 2026 |

> **Kritik:** Bing sitemap'i okuyamıyor — muhtemelen içerik bulunamıyor veya engelleniyor. Yeni Astro sitesinde sitemap.xml doğru generate edilmeli ve Bing'e yeniden gönderilmeli.

---

## 🔗 Backlink Profili

| Domain | Backlink Sayısı |
|--------|----------------|
| **benimisyerim.net** | 8 |

> Tek referring domain. Backlink profili son derece zayıf — yeni sitede link building stratejisi kritik.

---

## ⚠️ SEO Sorunları (Bing SEO Analizi)

### Hatalar (Acil)

| Sorun | Etkilenen Sayfa |
|-------|----------------|
| **Meta Açıklama etiketi eksik** | 12 sayfa |
| **HTTP 400-499 hataları** | 3 sayfa |

### Uyarılar

| Sorun | Etkilenen Sayfa |
|-------|----------------|
| **Resimler için alt öznitelik eksik** | **95 sayfa** ⚠️ |
| Başlık çok uzun | 8 sayfa |
| Birden fazla h1 etiketi | 6 sayfa |
| H1 etiketi eksik | 1 sayfa |

> **95 görselde alt tag yok** — bu hem SEO hem erişilebilirlik (Accessibility skoru 95→+) için önemli. Astro'da tüm görsellere `alt=""` eklenmeli.

---

## 📄 Bing'de İndekslenen Sayfalar (Top)

| Sayfa | Görüntüleme | Tıklama | HTTP | Backlink |
|-------|------------|---------|------|---------|
| Ana Sayfa (/) | 11 | 1 | 200 | **8** |
| /beton-nedir-modern-insaatin-temeli | **15** | 0 | 200 | 0 |
| /parlak-beton | 4 | 0 | 200 | 0 |
| /beton-parlatma-uygulamasi-fiyatlar | 2 | 0 | 200 | 0 |
| /project-management | 0 | 0 | **301** | 0 |
| /fabrikalarda-kaymaz-zeminlerin... | 1 | 1 | 200 | 0 |

> **/project-management** sayfası Bing'de 301 redirect veriyor — kontrol edilmeli, yönlendirme doğru URL'ye gitmeli.

---

## 🎯 Aksiyon Planı (Yeni Site İçin)

| Öncelik | Aksiyon |
|---------|---------|
| 🔴 Acil | Sitemap.xml'i Bing'e yeniden gönder (IndexNow ile) |
| 🔴 Acil | Meta description eksik 12 sayfayı düzelt |
| 🟠 Yüksek | 95 görsele alt tag ekle |
| 🟠 Yüksek | Birden fazla H1 olan 6 sayfayı düzelt |
| 🟡 Orta | /project-management 301 redirect'i kontrol et |
| 🟡 Orta | IndexNow entegrasyonu kur (Astro'da her deploy'da otomatik bildir) |
| 🟢 Fırsat | Bing Copilot'ta daha fazla alıntı için teknik içerikler kuvvetlendir |

---

## 📅 Karşılaştırma Geçmişi

| Tarih | Toplam Tık (yıllık) | Sitemap | AI Citation | Notlar |
|-------|--------------------|---------|----|--------|
| 2026-02-25 | 7 | ⚠️ Hata | 1 | Baseline — WordPress aşaması |
