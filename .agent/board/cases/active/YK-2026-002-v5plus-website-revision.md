# v5+ Web Sitesi Revizyonu (İnteraktivite + SEO + İçerik)

---

## 📌 Meta Bilgi

| Alan | Değer |
|------|-------|
| **Case No** | YK-2026-002 |
| **Tarih** | 2026-02-25 |
| **Durum** | ✅ Approved (3 Fazlı Sprint) |
| **Öncelik** | 🔴 Kritik |
| **Kategori** | Dijital / Pazarlama / Strateji |
| **İlgili Yöneticiler** | CEO, CMO, CDO |
| **Açan Kişi** | Kullanıcı |

---

## 📝 Özet

Yeni web sitesi (v5+) için üç temel revizyon: (1) İnteraktif component'ler ve modern sunum, (2) SEO ve AI indexleme için optimize mimari, (3) Build gerektirmeyen dinamik içerik yönetimi.

---

## 🎯 Kapsam ve Bağlam

### Durum

- Mevcut durum: v5.1 mockup hazır ama production'da değil
- Acil ihtiyaç: Lead almaya başlamak (şu an web sitesi yok)
- Stratejik hedef: Organik büyüme motoru + premium marka imajı

### Hedef

1. **MVP canlıya alınsın** → Lead generation başlasın
2. **İnteraktif UX** → Form dönüşüm oranı optimize edilsin
3. **SEO motoru** → Organik trafik compound effect (uzun vadeli)
4. **İçerik hızı** → Haftalık 2 blog yazısı eklenebilsin (build-free)

### Kısıtlar

- **Zaman:** Agresif timeline (MVP 2 hafta)
- **Kaynak:** Can dedicated (4 hafta), Serena içerik desteği
- **Bütçe:** 31.000 ₺

---

## 💬 Yönetici Görüşleri

### [CMO — Serena Öztürk]

📍 **KONU:** v5+ Mockup — İnteraktivite, İçerik & SEO Revizyonu

**ÖNERİLEN STRATEJİ:**

#### 1. İnteraktivite & Sunum Yöntemleri

**Hero Section:**
- Interactive scroll animation (zemin parlatma süreci)
- Before/after slider (mevcut v5.1 korunacak)
- 3D zemin modeli (optional — Spline)

**Hizmet Sayfaları:**
- Accordion/Tab sistemi
- Fiyat hesaplayıcı (alan m² + zemin durumu → tahmini fiyat)
- "Benim projeme uygun mu?" quiz

**Referans Projeler:**
- Filtrelenebilir galeri
- Video testimonial'lar
- Before/after slider

#### 2. SEO & AI Indexleme Mimarisi

**Pillar + Cluster Model:**

```
PILLAR: /beton-parlatma/
├── /beton-parlatma/fiyatlari/
├── /beton-parlatma/nasil-yapilir/
├── /beton-parlatma/ankara/
├── /beton-parlatma/istanbul/
└── /beton-parlatma/izmir/

SUPPORTING: /blog/ (haftalık yeni içerik)
```

**AI-Friendly İçerik:**
- Schema.org zengin markup
- Soru-cevap formatı (ChatGPT citation için)
- TL;DR özet blokları
- Tablolar (AI parse için)

#### 3. Dinamik İçerik (Build-Free)

**Astro Content Collections:**
- Yeni blog → `.md` dosyası ekle → git push → 2 dk deploy
- Decap CMS (web UI) → markdown editor
- Non-teknik ekip markdown bilmeden içerik ekleyebilir

**BEKLENEN ÇIKTI:**

- Sayfa engagement: +80%
- Organik trafik: +150% (6 ay)
- Featured snippet: 3+ anahtar kelime
- Yeni içerik yayın: ≤5 dakika

**BÜTÇE TAHMİNİ:** 31.000 ₺

---

### [CDO — Can Erdoğan]

📍 **KONU:** v5+ Web Sitesi — Teknik Mimari & Implementasyon

**ÖNERİ:** Astro + Content Collections

**Sebep:**
- Static generation → Lighthouse 95+
- Content Collections → `.md` = otomatik sayfa
- Islands architecture → JS sadece gerekli yerde
- SEO native (schema, sitemap auto)
- Ücretsiz hosting (Vercel free tier)

**IMPLEMENTASYON PLANI:**

**Sprint 1: MVP (Hafta 1-2)**
```
✅ Astro proje kurulumu
✅ Ana sayfa + 3 hizmet sayfası
✅ Referanslar (5 proje)
✅ İletişim + form
→ HEDEF: Lead almaya başla
```

**Sprint 2: İnteraktivite (Hafta 3-4)**
```
✅ Fiyat hesaplayıcı
✅ Quiz component
✅ Before/after slider (gelişmiş)
✅ Filtrelenebilir galeri
→ HEDEF: Form dönüşüm optimize
```

**Sprint 3: İçerik Motoru (Hafta 5-8)**
```
✅ Blog altyapısı + CMS
✅ İlk 10 blog yazısı (AI)
✅ Pillar/cluster model
✅ SEO teknik altyapı
→ HEDEF: Organik trafik başlat
```

**TEKNİK RİSK:**

⚠️ Markdown eğrimi → **Önlem:** Decap CMS web UI (WYSIWYG)
⚠️ Performans (JS yükü) → **Önlem:** Lazy loading + code splitting
⚠️ Git workflow → **Önlem:** Decap otomatik commit atar

---

### [CEO — Alexander Kaya]

📍 **KONU:** v5+ Web Sitesi Stratejik Karar

**STRATEJİK GÖRÜŞ:**

Üç kritik iş değeri:
1. Lead generation altyapısı
2. Organik büyüme motoru
3. Marka prestiji

**3 yıllık hedeflerle uyum:**
- "En güvenilir marka" → E-E-A-T içerik
- Coğrafi genişleme → Lokasyon sayfaları
- %25 büyüme → Organik kanal (düşük CPL)

**ÖNERİ:** ✅ ONAYLIYORUM — 3 Fazlı Sprint

**Öncelik sırası:**
1. Sprint 1: MVP (2 hafta) → Lead almaya başla
2. Sprint 2: İnteraktivite (2 hafta) → Dönüşüm optimize
3. Sprint 3: İçerik (4 hafta) → SEO motoru

**RİSK:**

⚠️ Execution timing (2 hafta agresif) → **Önlem:** SADECE MVP Sprint 1'de
⚠️ İçerik sürdürülebilirliği → **Önlem:** İlk 3 ay AI toplu üretim
⚠️ Odak dağılması (Multimedia case paralel) → **Önlem:** Farklı timeline'lar

**AKSİYON SAHİBİ:**
- CDO (Can) — Sprint 1-2 (dedicated 4 hafta)
- CMO (Serena) — Sprint 3 (içerik)
- Haftalık CEO sync (15 dk)

---

## ✅ Final Karar

**Karar Veren:** CEO (Alexander Kaya)

**Karar:** ✅ **ONAYLANDI — 3 Fazlı Sprint Modeli**

**Gerekçe:**

Web sitesi yokluğu → acil MVP gerekiyor
İnteraktivite + içerik → uzun vadeli büyüme motoru
3 yıllık stratejik hedeflerle tam uyumlu

**Sprint Planı:**

| Sprint | Süre | Hedef | Sorumlu |
|--------|------|-------|---------|
| 1: MVP | 2 hafta | Lead almaya başla | CDO |
| 2: İnteraktivite | 2 hafta | Dönüşüm optimize | CDO |
| 3: İçerik Motoru | 4 hafta | SEO başlat | CMO + CDO |

---

## 🚀 Aksiyon Planı

| # | Aksiyon | Sorumlu | Deadline | Durum | Notlar |
|---|---------|---------|----------|-------|--------|
| 1 | Astro proje kurulumu + ilk commit | CDO (Can) | 2026-02-26 | ⏳ | Scaffold + Tailwind |
| 2 | v5+ mockup wireframe (interaktif component'ler) | CMO (Serena) | 2026-02-28 | ⏳ | frontend-premium-design skill |
| 3 | Ana sayfa + layout bileşenleri | CDO (Can) | 2026-03-02 | ⏳ | Hero + Header + Footer |
| 4 | 3 hizmet sayfası (/beton-parlatma/, /lityum-silikat/, /zemin-tamiratı/) | CDO (Can) | 2026-03-05 | ⏳ | Content Collections |
| 5 | Referans projeler sayfası (ilk 5 proje) | CDO (Can) | 2026-03-07 | ⏳ | Galeri + filtre |
| 6 | İletişim sayfası + form | CDO (Can) | 2026-03-09 | ⏳ | Form validation |
| 7 | **MVP DEPLOY (Sprint 1 tamamlandı)** | CDO (Can) | **2026-03-11** | ⏳ | **Milestone 1** |
| 8 | Fiyat hesaplayıcı component | CDO (Can) | 2026-03-15 | ⏳ | Preact island |
| 9 | "Benim projeme uygun mu?" quiz | CDO (Can) | 2026-03-18 | ⏳ | Lead segmentation |
| 10 | Before/after slider (gelişmiş) | CDO (Can) | 2026-03-21 | ⏳ | v5.1'den port + iyileştirme |
| 11 | **Sprint 2 DEPLOY (İnteraktivite tamamlandı)** | CDO (Can) | **2026-03-25** | ⏳ | **Milestone 2** |
| 12 | İlk 10 blog yazısı konu seçimi | CMO (Serena) | 2026-03-27 | ⏳ | Long-tail SEO hedef |
| 13 | Blog altyapısı + Content Collections (blog/) | CDO (Can) | 2026-04-01 | ⏳ | Astro blog template |
| 14 | Decap CMS kurulumu (OPSIYONEL - 3. ay sonunda karar) | CDO (Can) | 2026-05-31 | ⏸️ | Serena: İlk 3 ay AI+markdown test |
| 15 | İlk 10 blog yazısı (AI üretimi + Serena editöryel kontrol) | CMO (Serena) | 2026-04-10 | ⏳ | content-writer skill → Can commit |
| 16 | Schema.org markup (LocalBusiness, Service, FAQPage, HowTo) | CDO (Can) | 2026-04-12 | ⏳ | AI indexleme optimize |
| 17 | Sitemap + robots.txt + Analytics | CDO (Can) | 2026-04-15 | ⏳ | SEO teknik altyapı |
| 18 | Lighthouse CI kurulumu | CDO (Can) | 2026-04-17 | ⏳ | Build-time performans check |
| 19 | **Sprint 3 DEPLOY (İçerik motoru tamamlandı)** | CDO + CMO | **2026-04-22** | ⏳ | **Milestone 3 (FINAL)** |
| 20 | İlk aylık SEO raporu (trafik, sıralama, dönüşüm) | CMO (Serena) | 2026-05-01 | ⏳ | KPI baseline ölçümü |
| 21 | **3 aylık CEO Review Toplantısı** | CEO + CMO + CDO | 2026-07-25 | ⏳ | KPI değerlendirme |

---

## 📊 KPI'lar ve Ölçüm

| KPI | Baseline | Hedef (3 ay) | Hedef (6 ay) | Ölçüm Yöntemi | Sorumlu |
|-----|----------|-------------|-------------|---------------|---------|
| **Web sitesi canlı** | Hayır | ✅ MVP | ✅ Full | Vercel deploy | CDO |
| **Lead (form submission)** | 0 | 20+/ay | 40+/ay | GA4 form tracking | CMO + CDO |
| **Organik trafik** | 0 | 500+/ay | 2.000+/ay | GA4 acquisition | CMO |
| **"beton parlatma fiyatları" sırası** | N/A | ≤20 | ≤5 | Search Console | CMO |
| **Featured snippet** | 0 | 1+ | 3+ | Search Console | CMO |
| **Sayfa engagement time** | N/A | 2+ dk | 3+ dk | GA4 engagement | CMO |
| **Form dönüşüm oranı** | N/A | %2.5+ | %3.5+ | GA4 conversion | CMO |
| **Blog yazısı sayısı** | 0 | 10+ | 25+ | Content inventory | CMO |
| **Lighthouse Mobile skoru** | N/A | 90+ | 95+ | Lighthouse CI | CDO |

**Review Tarihleri:**
- **Milestone 1:** 2026-03-11 (MVP canlı mı?)
- **Milestone 2:** 2026-03-25 (İnteraktivite tamamlandı mı?)
- **Milestone 3:** 2026-04-22 (İçerik motoru hazır mı?)
- **3 Aylık Review:** 2026-07-25 (KPI'lar hedefte mi?)

---

## 💰 Bütçe

| Kalem | Tutar | Onay Durumu |
|-------|-------|-------------|
| v5+ Mockup Tasarım (frontend-premium-design skill) | 8.000 ₺ | ✅ Onaylandı |
| Astro Implementasyon (CDO dedicated 4 hafta) | 12.000 ₺ | ✅ Onaylandı |
| İnteraktif Component'ler (fiyat hesaplayıcı, quiz, slider) | 6.000 ₺ | ✅ Onaylandı |
| Decap CMS Kurulumu (opsiyonel - 3. ay karar) | 2.000 ₺ | ⏸️ Beklemede (Serena C seçeneği) |
| SEO Teknik Altyapı (schema, sitemap, analytics) | 3.000 ₺ | ✅ Onaylandı |
| **TOPLAM (Garantili)** | **29.000 ₺** | **✅ CFO Onaylandı** |
| **CMS (Koşullu - 3. ay)** | **+2.000 ₺** | **⏸️ Serena kararına bağlı** |

**Hosting Maliyeti:** 0 ₺/ay (Vercel free tier yeterli — 100 GB bandwidth/ay)

---

## 📎 Ekler ve Referanslar

- [CMO Profili](.agent/board/CMO.md)
- [CDO Profili](.agent/board/CDO.md)
- [CEO Profili](.agent/board/CEO.md)
- [SEO Stratejisi](.agent/context/seo.md)
- [Mevcut v5.1 Mockup](.agent/mockups/v5.1-editorial.html)
- [Frontend Design Skills](.skills/frontend-design/, .skills/frontend-premium-design/)

---

## 📅 Tarihçe

| Tarih | Olay | Düzenleyen |
|-------|------|------------|
| 2026-02-25 | Case oluşturuldu | AI Agent |
| 2026-02-25 | YK görüşleri alındı (CEO, CMO, CDO) | AI Agent |
| 2026-02-25 | Karar verildi: 3 Fazlı Sprint Onaylandı | CEO (Alexander Kaya) |
| 2026-02-25 | Aksiyon planı oluşturuldu (21 aksiyon) | AI Agent |

---

## 🏷️ Etiketler

`#web-sitesi` `#dijital` `#pazarlama` `#seo` `#içerik` `#astro` `#interaktivite` `#mvp` `#2026` `#sprint`

---

**Son Güncelleme:** 2026-02-25
**Dosya:** `YK-2026-002-v5plus-website-revision.md`
**Durum:** ✅ Approved — 3 Sprint (8 hafta)
**İlk Milestone:** 2026-03-11 (MVP DEPLOY)
**Final Milestone:** 2026-04-22 (Full Site)
