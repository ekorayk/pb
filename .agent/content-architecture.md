# Yeni Web Sitesi İçerik Mimarisi — parlakbeton.com

**Hazırlayan:** AI Yönetim Kurulu
**Tarih:** 2026-02-25
**Amaç:** Astro migration için içerik yapısı ve sayfa planlaması

**Veri Kaynakları:**
- Google Analytics 4: 1.424 oturum, 85 click-to-chat lead
- Search Console: 275 tıklama, 18.200 gösterim, pozisyon 15
- Mevcut WordPress arşivi: 25 blog yazısı + 4 ana sayfa
- Referans projeler: Debak, Garanti İplik, Tedak

---

## 🎯 Stratejik Hedefler (6 Ay)

| Hedef | Mevcut | Hedef | Strateji |
|-------|--------|-------|----------|
| **Organik Trafik** | %31 (440 oturum) | %50 artış (660+) | SEO içerik + teknik optimizasyon |
| **Click to Chat** | 85/yıl | 130+/yıl | CTA optimizasyonu + landing page |
| **"Beton parlatma fiyatları"** | Pozisyon 32 | Top 5 | Özel landing page + hesaplama aracı |
| **NPS Skoru** | Ölçülmüyor | ≥70 | CRM + otomatik anket sistemi |
| **PageSpeed Mobil** | 99/100 | 100/100 | Astro SSG + görsel optimizasyon |

---

## 📊 Metrik Bazlı İçerik Öncelikleri

### Search Console Fırsat Analizi

| Keyword | Gösterim | Tıklama | Pozisyon | Öncelik | Aksiyon |
|---------|----------|---------|----------|---------|---------|
| **parlak beton** | 1.227 | 34 | 1,11 ⭐ | 🔴 Kritik | Pozisyonu KORU |
| **beton parlatma fiyatları** | 114 | 0 | 32,4 | 🔴 Kritik | Yeni landing page |
| **beton zemin parlatma** | 496 | 0 | 13,27 | 🔥 Fırsat | İçerik derinleştir |
| **beton parlatma nedir** | 373 | 0 | 15,91 | 🔥 Fırsat | Eğitim içeriği |
| **beton parlatma makinesi nasıl çalışır** | 1.255 | 2 | 34,57 | 🟠 Yüksek | Teknik blog + video |
| **fabrika zemin parlatma** | 143 | 0 | 7,52 | 🔥 Fırsat | Sektör sayfası |

### Analytics Davranış Analizi

| Sayfa | Görüntüleme | Insight | Aksiyon |
|-------|-------------|---------|---------|
| **Ana Sayfa** | 768 | En çok trafik | Hero CTA + trust signals |
| **İletişim** | 153 | 3. sırada 🔥 | Form optimizasyonu + WhatsApp |
| **Mobil Robot Zemin** | 110 | Niş hedef kitle | İçerik zenginleştir |
| **404 Sayfası** | 112 ⚠️ | Kırık linkler | Redirect map uygula |
| **Referanslar** | 68 | Sosyal kanıt | Video testimonial ekle |

---

## 🗂️ Site Haritası & URL Yapısı

```
parlakbeton.com/
│
├── / (Ana Sayfa)
│   └── Hero + Trust Signals + Süreç + Referanslar + CTA
│
├── /hizmetler/
│   ├── index (Hizmet Hub Sayfası)
│   ├── beton-parlatma/
│   │   ├── index (Ana Hizmet)
│   │   ├── fiyatlari/ ⭐ YENİ — Kritik ticari keyword
│   │   ├── nasil-yapilir/ ⭐ YENİ — E-E-A-T içerik
│   │   └── lityum-silikat/ ⭐ YENİ — Teknik derinlik
│   ├── zemin-tamirat/
│   └── zemin-kaplama-danismanligi/
│
├── /sektorler/ ⭐ YENİ — Sektör odaklı landing pages
│   ├── index (Sektör Hub)
│   ├── tekstil-fabrikalari/
│   ├── gida-tesisleri/
│   ├── otomotiv-sanayi/
│   ├── lojistik-depolari/
│   ├── enerji-elektrik/
│   └── mobil-robot-fabrikalari/
│
├── /lokasyonlar/ ⭐ YENİ — Lokasyon SEO
│   ├── ankara-beton-parlatma/ (Mevcut blog'dan upgrade)
│   ├── istanbul-beton-parlatma/
│   └── izmir-beton-parlatma/
│
├── /projeler/ (Referanslar)
│   ├── index (Filtreli galeri: sektör, yıl, lokasyon)
│   ├── debak-denizli/
│   ├── garanti-iplik-corlu/
│   └── tedak-denizli/
│
├── /blog/ (İçerik hub)
│   ├── index (Kategori filtreleri)
│   ├── [kategori]/
│   │   ├── teknik/ (Lityum silikat, DCOF, Mohs)
│   │   ├── sektor/ (Fabrika, depo, ofis)
│   │   ├── karsilastirma/ (Epoksi vs. Parlak Beton)
│   │   └── sss/ (FAQ içerikleri)
│   └── [slug]/ (25+ mevcut blog + yeniler)
│
├── /hakkimizda/
│   └── Firma hikayesi + Ekip + Sertifikalar + Değerler
│
├── /iletisim/
│   └── Form + WhatsApp + Telefon + Harita + Ücretsiz Keşif CTA
│
└── /kaynaklar/ ⭐ YENİ
    ├── brosurler/ (PDF indirme)
    ├── teknik-dokuman/ (ANSI, DCOF standartları)
    └── sss/ (Detaylı FAQ)
```

---

## 📄 Sayfa Bazlı İçerik Planı

### 1. Ana Sayfa (/)

**SEO Hedef:** "parlak beton" (#1 koru), "beton parlatma" (top 3)

**Meta:**
- **Title:** `Parlak Beton | Profesyonel Beton Parlatma Uzmanı | 15+ Yıl Deneyim`
- **Description:** `Türkiye'nin beton parlatma lideri. Lityum silikat teknolojisi, ANSI standartları, 200+ tamamlanmış proje. Ankara·İstanbul·İzmir. Ücretsiz keşif: 0507 218 5318`

**Bölümler:**

1. **Hero Section**
   - H1: "Betonunuzu Mermer Gibi Parlak ve Kalıcı Bir Yüzeye Dönüştürün"
   - Alt başlık: "15+ yıldır Türkiye'nin fabrika, depo ve ofislerinde beton parlatma teknolojisinin öncüsüyüz"
   - CTA: "Ücretsiz Keşif Talep Edin" (WhatsApp + Form)
   - Trust badge: "200+ Tamamlanmış Proje • 15 Yıl Deneyim • ANSI Standartları"

2. **Liquid Glass Stats Panel** (Mevcut mockup'ta var)
   - "15+ Yıl Deneyim"
   - "200+ Proje"
   - "ANSI A137.1 Sertifikalı"
   - "%100 Müşteri Memnuniyeti"

3. **Süreç (6 Adım)** — İnfografik + Kısa açıklamalar
   - Zemin Analizi → Tamirat → Silim → Lityum Silikat → Parlatma → Koruyucu

4. **Neden Parlak Beton?** (4 Ana Avantaj Kartları)
   - Ultra Dayanıklılık (Mohs 7+, %400 aşınma direnci)
   - Kesin Tozumazlık (%100 hipoalerjenik)
   - Enerji Verimliliği (%30 aydınlatma tasarrufu)
   - Düşük Bakım Maliyeti (%60 düşük yaşam döngüsü maliyeti vs. epoksi)

5. **Referans Logoları + Öne Çıkan Vaka**
   - Debak, Garanti İplik, Tedak logoları
   - 1 vaka çalışması spotlight (Garanti İplik — tekstil sektörü)

6. **Sektör Çözümleri (6 Kart)**
   - Tekstil • Gıda • Otomotiv • Lojistik • Enerji • Mobil Robot

7. **Sosyal Kanıt**
   - Müşteri testimonial (Tedak: "8 yıl sonra ilk günkü gibi")
   - Video testimonial embed (gelecek faz)

8. **CTA Section**
   - "Zeminizi Ücretsiz Değerlendirmemize İzin Verin"
   - Form + WhatsApp + Telefon

9. **FAQ (Accordion — 6 soru)**
   - Schema.org FAQPage markup
   - "Beton parlatma fiyatları neye göre belirlenir?"
   - "Parlatılmış beton kaygan mıdır?"
   - "Epoksiden ne farkı var?"

10. **Blog Snippet (Son 3 yazı)**

**Schema.org:**
- LocalBusiness
- FAQPage
- Service (Beton Parlatma)

---

### 2. Hizmet Hub (/hizmetler/)

**SEO Hedef:** "beton parlatma hizmetleri"

**Meta:**
- **Title:** `Beton Parlatma Hizmetleri | Lityum Silikat | Zemin Tamirat | Parlak Beton`
- **Description:** `Profesyonel beton parlatma, lityum silikat kristalizasyon, zemin tamirat ve kaplama danışmanlığı. Fabrika, depo, ofis. ANSI standartları. Ücretsiz keşif.`

**İçerik:**

1. **Hero**
   - H1: "Endüstriyel Zemin Çözümlerimiz"
   - Alt başlık: "Her sektörün ihtiyacına özel, kanıtlanmış teknolojiler"

2. **Hizmet Kartları (3 Ana Hizmet)**

   **A. Beton Parlatma**
   - Kısa açıklama
   - "Mekanik silim + lityum silikat kristalizasyon"
   - CTA: "Detaylı Bilgi" → /hizmetler/beton-parlatma/

   **B. Zemin Tamirat**
   - "Çatlak, derz, delik onarımı — monolitik görünüm"
   - CTA: "Detaylı Bilgi" → /hizmetler/zemin-tamirat/

   **C. Zemin Kaplama Danışmanlığı**
   - "Hangi zemin çözümü size uygun? Ücretsiz analiz."
   - CTA: "Danışmanlık Talep Et" → İletişim formu

3. **Karşılaştırma Tablosu**
   - Beton Parlatma vs. Epoksi vs. Seramik
   - Kriterler: Maliyet, Dayanıklılık, Bakım, ROI

4. **CTA**
   - "Hangi Hizmet Size Uygun? — Ücretsiz Keşif Talep Edin"

**Schema.org:**
- Service (3 adet)

---

### 3. Beton Parlatma Fiyatları (/hizmetler/beton-parlatma/fiyatlari/) ⭐ YENİ — KRİTİK

**SEO Hedef:** "beton parlatma fiyatları" (pozisyon 32 → top 5)

**Meta:**
- **Title:** `Beton Parlatma Fiyatları 2026 | m² Bazında Hesaplama | Parlak Beton A.Ş.`
- **Description:** `Beton parlatma m² fiyatları: zemin durumu, alan büyüklüğü ve parlaklık seviyesine göre belirlenir. Ücretsiz keşif ve detaylı fiyat teklifi için hemen arayın.`

**İçerik:**

1. **Hero**
   - H1: "Beton Parlatma Fiyatları 2026"
   - Alt başlık: "Fiyat nasıl belirlenir? Hangi faktörler etkiler? Şeffaf bilgilendirme."

2. **Fiyat Etkileyen Faktörler (5 Kart)**

   **A. Metrekare (Alan Büyüklüğü)**
   - "Büyük alan = m² maliyeti düşer"
   - Örnek: 500 m² vs. 5.000 m² karşılaştırması

   **B. Zeminin Mevcut Durumu**
   - "Çatlak, boşluk, derz miktarı → onarım ihtiyacı"
   - Zemin durumu testi: Ücretsiz keşifte yapılır

   **C. Agrega Görünüm Derecesi**
   - "Yüzeysel silim mi, derin agrega açılımı mı?"
   - Görseller: Yüzeysel vs. Derin

   **D. Parlaklık Seviyesi**
   - Mat (800 grit) • Yarı Parlak (1500 grit) • Ayna Efekti (3000 grit)
   - Her seviye için süre ve maliyet farkı

   **E. Lojistik & Lokasyon**
   - Proje uzaklığı, ekipman nakli, konaklama

3. **Fiyat Aralığı Tablosu** (Yaklaşık — Keşif Gerekli)

   | Alan | Zemin Durumu | Parlaklık | Yaklaşık m² Fiyat |
   |------|-------------|----------|------------------|
   | 500-1.000 m² | İyi | Yarı Parlak | [Aralık — keşif sonrası] |
   | 1.000-3.000 m² | Orta | Tam Parlak | [Aralık — keşif sonrası] |
   | 3.000+ m² | İyi | Mat | [Aralık — keşif sonrası] |

   **Not (CFO Dilek onaylı):** Sabit fiyat listesi vermiyoruz. Tablo genel fikir için — keşif zorunlu.

4. **"Neden Sabit Fiyat Yok?" (Transparency Box)**
   - "Her zemin benzersizdir"
   - "Ücretsiz keşifte 6 kritik faktörü analiz ediyoruz"
   - "Keşif sonrası garantili fiyat teklifi"

5. **Hesaplama Aracı (İnteraktif)** ⭐ Faz 2
   - Alan m²
   - Zemin durumu (İyi/Orta/Kötü)
   - Parlaklık seviyesi
   - → "Yaklaşık Fiyat Aralığı" + CTA: "Kesin Fiyat İçin Keşif Talep Edin"

6. **TCO (Total Cost of Ownership) Karşılaştırma**
   - Beton Parlatma vs. Epoksi (10 yıllık maliyet)
   - Grafik: İlk yatırım + Bakım + Yeniden kaplama

7. **CTA**
   - "Zeminiz İçin Ücretsiz Keşif ve Fiyat Teklifi Alın"
   - Form + WhatsApp

8. **FAQ (Fiyat odaklı)**
   - "Beton parlatma ortalama ne kadar?"
   - "En ucuz zemin çözümü hangisi?"
   - "Epoksiden daha pahalı mı?"

**Schema.org:**
- Article (Price Guide)
- FAQPage

---

### 4. Sektör Sayfaları (/sektorler/[sektor]/) ⭐ YENİ

**Hedef:** Sektör bazlı long-tail keyword'ler
- "tekstil fabrikası zemin çözümleri"
- "gıda tesisi hijyenik zemin"
- "mobil robot zemin gereksinimleri"

**Şablon Yapısı (Her Sektör İçin):**

**Örnek: /sektorler/tekstil-fabrikalari/**

**Meta:**
- **Title:** `Tekstil Fabrikaları İçin Beton Parlatma | Sıfır Toz Standardı | Parlak Beton`
- **Description:** `Tekstil üretiminde kritik sıfır toz standardı. Lityum silikat uygulaması ile %100 tozumazlık. Garanti İplik referansımız. Ücretsiz keşif: 0507 218 5318`

**İçerik:**

1. **Hero**
   - H1: "Tekstil Fabrikaları İçin Zemin Çözümleri"
   - Alt başlık: "Sıfır toz standardı + ışık yansıtma verimliliği = kaliteli üretim"

2. **Sektör İhtiyaçları (3 Kritik Faktör)**
   - %100 Tozumazlık (iplik kalitesi)
   - Yüksek ışık yansıtma (renk kontrolü)
   - Kimyasal direnç (boya, kimyasal maruziyeti)

3. **Çözüm: Beton Parlatma**
   - Lityum silikat kristalizasyon → mikro gözenekler kapatılır
   - Sonuç: Hipoalerjenik, %100 tozsuz zemin

4. **Vaka Çalışması: Garanti İplik**
   - 2023 — Çorlu, Tekirdağ
   - Müşteri yorumu: "Tekstil üretiminde kritik olan sıfır toz standardı sağlandı."
   - Before/After görselleri

5. **Teknik Standartlar**
   - ANSI A137.1
   - ISO 8573-1 (hava kalitesi — toz sınıfı)

6. **CTA**
   - "Tekstil Fabrikanız İçin Ücretsiz Zemin Analizi"

**Diğer Sektör Sayfaları (Benzer Şablon):**
- Gıda Tesisleri: FDA uyumlu hijyen, HACCP
- Otomotiv Sanayi: Yağ direnci, ağır yük taşıma
- Lojistik Depoları: Forklift trafiği, darbe dayanımı
- Enerji & Elektrik: ESD (elektrostatik deşarj), güvenlik
- Mobil Robot Fabrikaları: Düşük sürtünme, DCOF 0.42+, hassasiyet

---

### 5. Projeler (Referanslar) (/projeler/)

**SEO Hedef:** "beton parlatma referansları"

**Meta:**
- **Title:** `Referans Projelerimiz | 200+ Başarılı Beton Parlatma Uygulaması | Parlak Beton`
- **Description:** `Debak, Garanti İplik, Tedak ve 200+ endüstriyel tesis. Sektör bazlı referanslarımız, müşteri yorumları ve before/after görseller.`

**İçerik:**

1. **Hero**
   - H1: "200+ Tamamlanmış Beton Parlatma Projesi"
   - Alt başlık: "Türkiye'nin her yerinde, her sektörde güvenilir çözüm ortağınız"

2. **Filtreler**
   - Sektör: Tekstil • Gıda • Otomotiv • Enerji • Lojistik • Diğer
   - Yıl: 2016-2023
   - Lokasyon: Ankara • İstanbul • İzmir • Denizli • Tekirdağ

3. **Proje Kartları (Grid)**
   - Firma logosu
   - Proje adı
   - Sektör
   - Yıl
   - Kısa sonuç: "8 yıldır ilk günkü gibi parlaklık"
   - CTA: "Detayları Gör" → /projeler/[firma-slug]/

4. **Öne Çıkan 3 Vaka (Detaylı Kartlar)**

   **A. Garanti İplik A.Ş. — Tekstil**
   - 2023 — Çorlu, Tekirdağ
   - Müşteri yorumu + görseller
   - [Detayları Gör](/projeler/garanti-iplik-corlu/)

   **B. Tedak Elektrik — Enerji**
   - 2016 — Denizli
   - 8 yıl sonra müşteri geri bildirimi
   - [Detayları Gör](/projeler/tedak-denizli/)

   **C. Debak Denizli — Endüstriyel Üretim**
   - 2017 — Denizli
   - 6 yıl kullanım deneyimi
   - [Detayları Gör](/projeler/debak-denizli/)

5. **Video Testimonial Section** (Faz 2)
   - Garanti İplik fabrika turu + yorum
   - YouTube embed

6. **CTA**
   - "Sizin Projeniz de Başarı Hikayemiz Olsun"

**Schema.org:**
- ItemList (Proje listesi)

---

### 6. Lokasyon Sayfaları (/lokasyonlar/[sehir]-beton-parlatma/)

**SEO Hedef:**
- "ankara beton parlatma"
- "istanbul beton parlatma"
- "izmir beton parlatma"

**Şablon Yapısı:**

**Örnek: /lokasyonlar/ankara-beton-parlatma/**

**Meta:**
- **Title:** `Ankara Beton Parlatma | Profesyonel Zemin Hizmetleri | Parlak Beton A.Ş.`
- **Description:** `Ankara ve çevresinde beton parlatma hizmetleri. 15+ yıl deneyim, ANSI standartları, ücretsiz keşif. Fabrika, depo, ofis. Hemen arayın: 0507 218 5318`

**İçerik:**

1. **Hero**
   - H1: "Ankara Beton Parlatma Hizmetleri"
   - Alt başlık: "Başkent'in fabrika ve işletmelerinde güvenilir zemin çözüm ortağınız"

2. **Ankara'da Hizmet Verdiğimiz Sektörler**
   - Otomotiv (OSB'ler)
   - Gıda
   - Lojistik
   - Elektrik & Enerji

3. **Ankara Referanslarımız** (Varsa)
   - [Firma adı] — [Sektör]
   - [Proje yılı]

4. **Neden Biz?**
   - Ankara'da 5+ yıl tecrübe
   - Yerel ekip — hızlı müdahale
   - Ücretsiz keşif — 24 saat içinde yanıt

5. **Ankara Haritası** (Google Maps embed)
   - Hizmet verdiğimiz bölgeler işaretli

6. **CTA**
   - "Ankara'da Ücretsiz Keşif Talep Edin"

**Diğer Lokasyon Sayfaları:**
- İstanbul: Anadolu Yakası / Avrupa Yakası ayrımı
- İzmir: Ege bölgesi vurgusu

---

### 7. Blog (/blog/)

**SEO Hedef:** Long-tail keyword'ler + E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

**Mevcut İçerikler (25 Blog):**

**Öncelikli Upgrade (Metrik Bazlı):**

1. **Beton Parlatma Makinesi Nasıl Çalışır** (1.255 gösterim, pozisyon 34)
   - Zenginleştir: Video + grit sıralaması detayı + lityum kimyası
   - Target: Top 10

2. **Beton Parlatma Fiyatları** (Mevcut)
   - → Landing page'e yönlendir (/hizmetler/beton-parlatma/fiyatlari/)

3. **Ankara Beton Parlatma** (Mevcut blog)
   - → Lokasyon sayfasına upgrade (/lokasyonlar/ankara-beton-parlatma/)

4. **Mobil Robot Zemin** (110 sayfa görüntüleme)
   - Zenginleştir: DCOF standardı + AGV/AMR teknik gereksinimler

5. **İstanbul Fabrika Zemini** (Mevcut blog)
   - → Lokasyon sayfasına upgrade

**Yeni İçerikler (SEO Fırsat):**

6. **"Beton Parlatma Nedir?" (373 gösterim, pozisyon 15)**
   - E-E-A-T odaklı kapsamlı kılavuz
   - Target: Top 3

7. **"Beton Parlatma mı Epoksi mi?"**
   - Karşılaştırma makalesi
   - TCO analizi + karar ağacı

8. **"Lityum Silikat Nedir ve Nasıl Çalışır?"**
   - Kimya: Li₂SiO₃ + Ca(OH)₂ → C-S-H jel
   - Bing Copilot citation fırsatı (teknik derinlik)

9. **"DCOF Nedir? Zemin Güvenlik Standardı"**
   - ANSI A137.1 açıklama
   - Test yöntemi: BOT-3000E

10. **"Parlatılmış Beton Kaç Yıl Dayanır?"**
    - Debak (6 yıl), Tedak (8 yıl) referansları
    - Yaşam döngüsü analizi

**Blog Kategorileri:**

- **Teknik:** Lityum silikat, DCOF, Mohs, grit sıralaması
- **Sektör:** Tekstil, gıda, otomotiv, lojistik
- **Karşılaştırma:** Epoksi, seramik, poliüretan
- **SSS:** Sıkça sorulan sorular detaylandırılmış

**Blog Format:**
- H1: SEO odaklı başlık
- Meta description: 150-160 karakter
- İçerik: 1.500-2.500 kelime (E-E-A-T için derinlik)
- Görseller: Alt tag zorunlu
- İç linkler: Hizmet sayfaları + diğer blog yazıları
- CTA: "Ücretsiz Keşif" her yazıda
- Schema.org: Article + Author (Dr. Emre Yıldız — CTO)

---

### 8. Hakkımızda (/hakkimizda/)

**SEO Hedef:** "parlak beton A.Ş."

**Meta:**
- **Title:** `Hakkımızda | Parlak Beton A.Ş. | 15+ Yıl Beton Parlatma Deneyimi`
- **Description:** `2009'dan beri Türkiye'nin beton parlatma öncüsü. 200+ proje, ANSI standartları, lityum silikat uzmanlığı. Ekibimiz, değerlerimiz ve hikayemiz.`

**İçerik:**

1. **Hero**
   - H1: "Betonun Parlak Yüzünü Keşfetmenize Yardımcı Oluyoruz"
   - Alt başlık: "15+ yıldır Türkiye'nin endüstriyel zemin teknolojilerinde güvenilir çözüm ortağı"

2. **Firma Hikayesi**
   - 2009: Kuruluş — endüstriyel zemin vizyonu
   - 2015: Lityum silikat teknolojisi Türkiye'ye ilk getirenlerden
   - 2020: 100. proje tamamlandı
   - 2024: 200+ proje, 6 farklı sektör

3. **Değerlerimiz (4 Kart)**
   - Teknik Mükemmellik
   - Müşteri Odaklılık
   - Sürdürülebilirlik
   - Şeffaflık

4. **Ekibimiz** (Opsiyonel — YK kararı)
   - Saha teknisyenleri
   - Teknik danışmanlar
   - Fotoğraflar (isteğe bağlı)

5. **Sertifikalar & Standartlar**
   - ANSI A137.1
   - NFSI
   - ISO (varsa)

6. **Sayılarla Parlak Beton**
   - 15+ Yıl Deneyim
   - 200+ Tamamlanmış Proje
   - 6 Sektörde Uzmanlaşma
   - %100 Müşteri Memnuniyeti (NPS ≥70 hedefi)

7. **CTA**
   - "Bizimle Çalışmak İster misiniz?"

**Schema.org:**
- Organization
- LocalBusiness

---

### 9. İletişim (/iletisim/)

**SEO Hedef:** "beton parlatma keşif"

**Meta:**
- **Title:** `İletişim | Ücretsiz Keşif Talep Edin | Parlak Beton A.Ş.`
- **Description:** `Beton parlatma hizmetlerimiz için ücretsiz keşif ve fiyat teklifi. WhatsApp, telefon veya form ile 24 saat içinde yanıt. 0507 218 5318`

**İçerik:**

1. **Hero**
   - H1: "Zeminizi Ücretsiz Değerlendirmemize İzin Verin"
   - Alt başlık: "24 saat içinde size ulaşıyor, ihtiyaçlarınızı analiz ediyoruz"

2. **İletişim Kanalları (3 Kutucuk)**

   **A. WhatsApp (Öncelikli)**
   - "En hızlı yanıt"
   - QR kod + tıklanabilir link
   - +90 507 218 5318

   **B. Telefon**
   - "Doğrudan görüşme"
   - +90 507 218 5318
   - Çalışma saatleri: 09:00-18:00 (Hafta içi)

   **C. E-posta**
   - info@parlakbeton.com

3. **Ücretsiz Keşif Formu**
   - İsim Soyisim *
   - Telefon *
   - E-posta
   - Firma Adı
   - Proje Lokasyonu (İl) *
   - Tahmini Alan (m²) *
   - Zemin Mevcut Durumu: İyi / Orta / Kötü / Bilmiyorum
   - Mesajınız
   - KVKK Aydınlatma metni onay checkbox *
   - "Ücretsiz Keşif Talep Et" (CTA button)

4. **Adres & Harita** (Opsiyonel — ofis adresi varsa)
   - Google Maps embed

5. **SSS (İletişim odaklı)**
   - "Keşif ne kadar sürer?"
   - "Keşif ücretli mi?"
   - "Teklif ne kadar sürede hazırlanır?"

**Schema.org:**
- ContactPage

---

### 10. Kaynaklar (/kaynaklar/) ⭐ YENİ

**SEO Hedef:** E-E-A-T sinyalleri + lead nurturing

**Alt Sayfalar:**

**A. Broşürler (/kaynaklar/brosurler/)**
- PDF 1: Parlak Beton Zemin Teknolojileri — Genel Broşür (8 MB)
- PDF 2: Mobil Robot Kullanan Fabrikalarda Parlak Beton (18 MB)
- İndirme: E-posta + KVKK onay gerekli (lead capture)

**B. Teknik Dokümanlar (/kaynaklar/teknik-dokuman/)**
- ANSI A137.1 Standardı Özeti
- DCOF Test Yöntemi
- Lityum Silikat Kimyası (Li₂SiO₃ reaksiyonu)
- Grit Sıralaması Kılavuzu

**C. Detaylı SSS (/kaynaklar/sss/)**
- 20+ soru-cevap
- FAQPage schema
- İçerik: Ana sayfadaki FAQ'leri genişlet

---

## 🎨 Mockup Güncelleme Önerileri

**Mevcut Mockup:** v5.1 editorial + liquid glass navbar

**Güncelleme Gereken Bölümler:**

### 1. Hero Section

**Mevcut:**
- Genel başlık

**Öneri:**
- H1: "Betonunuzu Mermer Gibi Parlak ve Kalıcı Bir Yüzeye Dönüştürün"
- Alt başlık: "15+ yıldır Türkiye'nin fabrika, depo ve ofislerinde beton parlatma teknolojisinin öncüsüyüz"
- **2 CTA button:**
  1. "Ücretsiz Keşif Talep Edin" (Primary — WhatsApp)
  2. "Referansları İnceleyin" (Secondary — scroll to referanslar)
- Trust badge line: "200+ Tamamlanmış Proje • 15 Yıl Deneyim • ANSI Standartları"

### 2. Stats Panel (Liquid Glass)

**Mevcut:** Var ✅

**Güncelleme:**
- "15+ Yıl Deneyim"
- "200+ Proje"
- "ANSI A137.1 Sertifikalı"
- "%100 Müşteri Memnuniyeti"

### 3. Süreç (6 Adım)

**Eklenecek:**
- İnfografik timeline
- Her adımda ikon + kısa açıklama (2-3 cümle)
- Zemin Analizi → Tamirat → Silim → Lityum Silikat → Parlatma → Koruyucu

### 4. Avantajlar (4 Kart)

**Kart Yapısı:**
- İkon
- Başlık
- Kısa açıklama (3-4 cümle)
- Metrik vurgusu (ör. "%400 aşınma direnci artışı")

### 5. Referans Logoları

**Eklenecek:**
- Debak, Garanti İplik, Tedak logoları
- "200+ Firma Bize Güvendi" başlığı

### 6. Vaka Çalışması Spotlight

**Format:**
- Sol: Garanti İplik görseli (fabrika)
- Sağ: Proje hikayesi + müşteri yorumu
- CTA: "Tüm Referansları Gör"

### 7. Sektör Çözümleri (6 İkon Kart)

**Eklenecek:**
- Tekstil • Gıda • Otomotiv • Lojistik • Enerji • Mobil Robot
- Her kart: İkon + başlık + 1 cümle
- CTA: "Detayları Gör" → /sektorler/[slug]/

### 8. Testimonial Section

**Format:**
- Blockquote (büyük font)
- Müşteri yorumu: "Parlak Beton uygulamasının kalitesi ve dayanıklılığı, 8 yıl boyunca geçen sürede bile ilk günkü gibi korunmuştur."
- Firma logosu + isim: Tedak Elektrik
- Video embed (Faz 2)

### 9. FAQ Accordion

**6 Soru:**
1. "Beton parlatma fiyatları neye göre belirlenir?"
2. "Parlatılmış beton kaygan mıdır?"
3. "Epoksiden ne farkı var?"
4. "Uygulama ne kadar sürer?"
5. "Beton parlatma kalıcı mı?"
6. "Hangi sektörlere uygundur?"

### 10. CTA Section (Final)

**Format:**
- Arka plan: Gradient veya parlak beton görseli
- Başlık: "Zeminizi Ücretsiz Değerlendirmemize İzin Verin"
- Alt başlık: "24 saat içinde size ulaşıyor, ihtiyaçlarınızı analiz ediyoruz"
- Form (inline) + WhatsApp button

### 11. Footer

**Eklenecek:**
- 4 Kolon:
  1. Logo + slogan + iletişim
  2. Hizmetler (linkler)
  3. Sektörler (linkler)
  4. Şirket (Hakkımızda, Projeler, İletişim, Gizlilik Politikası)
- Sosyal medya ikonları (varsa)
- Copyright: "© 2026 Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş."

---

## 📊 İçerik Üretim Öncelikleri

### Faz 1: Migration (0-14 gün)

| # | Sayfa | Öncelik | Aksiyon | Sorumlu |
|---|-------|---------|---------|---------|
| 1 | Ana Sayfa | 🔴 Kritik | Yeni içerik + mockup | CMO + CDO |
| 2 | İletişim | 🔴 Kritik | Form + WhatsApp + KVKK | CDO + CLO |
| 3 | Beton Parlatma (hizmet) | 🔴 Kritik | Mevcut içerik + SEO optimize | CMO |
| 4 | Hakkımızda | 🟠 Yüksek | Firma hikayesi + değerler | CEO + CMO |
| 5 | Projeler (referanslar) | 🟠 Yüksek | 3 vaka çalışması | CXO + CMO |
| 6 | 404 Redirect Map | 🔴 Kritik | 78 redirect test | CDO + CLO |
| 7 | Gizlilik Politikası | 🔴 Kritik | KVKK uyumlu metin | CLO |

### Faz 2: SEO Expansion (14-60 gün)

| # | Sayfa | Öncelik | Aksiyon | Sorumlu |
|---|-------|---------|---------|---------|
| 8 | Beton Parlatma Fiyatları | 🔴 Kritik | Yeni landing page | CMO + CFO |
| 9 | Beton Parlatma Nasıl Yapılır | 🟠 Yüksek | E-E-A-T içerik | CTO + CMO |
| 10 | Lityum Silikat | 🟠 Yüksek | Teknik derinlik | CTO + CMO |
| 11 | Tekstil Sektör Sayfası | 🟡 Orta | Garanti İplik vaka | CMO |
| 12 | Ankara Lokasyon | 🟡 Orta | Blog'dan upgrade | CMO |
| 13 | "Beton Parlatma Nedir" Blog | 🔥 Fırsat | 373 gösterim keyword | CMO |
| 14 | "Makinesi Nasıl Çalışır" Blog | 🔥 Fırsat | 1.255 gösterim + video | CTO + CMO |

### Faz 3: Advanced Content (60-90 gün)

| # | Sayfa | Öncelik | Aksiyon | Sorumlu |
|---|-------|---------|---------|---------|
| 15 | Diğer 4 Sektör Sayfası | 🟡 Orta | Gıda, Otomotiv, Lojistik, Enerji | CMO |
| 16 | İstanbul + İzmir Lokasyon | 🟡 Orta | Lokasyon SEO | CMO |
| 17 | 10+ Yeni Blog | 🟡 Orta | Long-tail keyword'ler | CTO + CMO |
| 18 | Video Testimonial | 🟢 Düşük | Garanti İplik çekimi | CXO + COO |
| 19 | Fiyat Hesaplama Aracı | 🟢 Düşük | İnteraktif tool | CDO + CFO |
| 20 | Kaynaklar (Broşür + Teknik) | 🟡 Orta | Lead capture | CMO + CTO |

---

## 🔍 SEO Teknik Checklist

**Migration Öncesi:**
- [ ] 404 redirect map %100 test
- [ ] robots.txt hazır
- [ ] Sitemap.xml formatı Astro ile uyumlu
- [ ] Canonical URL'ler tanımlı
- [ ] Meta tag şablonları hazır

**Migration Sırası:**
- [ ] Google Search Console: sitemap submit
- [ ] Bing Webmaster: sitemap submit + IndexNow
- [ ] Schema.org: LocalBusiness + Service + FAQPage
- [ ] Open Graph etiketleri (her sayfa)
- [ ] Alt tag'ler (95 görsel + yeniler)

**Migration Sonrası:**
- [ ] Haftalık SEO monitoring (CMO + CDO)
- [ ] Lighthouse CI (otomatik build)
- [ ] Broken link check (2 haftada bir)
- [ ] NPS anketi sistemi (CRM)

---

## 📞 İletişim & Lead Capture Stratejisi

### Form Optimizasyonu

**Alan Minimizasyonu:**
- İsim Soyisim *
- Telefon *
- E-posta
- Proje Lokasyonu *
- Tahmini Alan (m²) *
- Mesaj
- KVKK onay *

**CSO Mehmet Önerisi: Lead Niteleme Soruları**
- Zemin Durumu: İyi / Orta / Kötü / Bilmiyorum
- Proje Aciliyeti: 1 ay içinde / 1-3 ay / 3-6 ay / Sadece bilgi

### WhatsApp İntegrasyonu

**URL:**
```
https://wa.me/905072185318?text=Merhaba,%20beton%20parlatma%20hizmeti%20hakkında%20bilgi%20almak%20istiyorum.
```

**CTA Button Metni:**
- "WhatsApp ile Hızlı İletişim"
- "Ücretsiz Keşif Talep Et"

### Lead Takip (CRM)

**HubSpot Free Kurulumu (CDO):**
- Form → otomatik CRM kayıt
- Lead kaynağı takibi (sayfa + keyword)
- WhatsApp lead'leri manuel giriş (CSO ekibi)
- NPS anketi entegrasyonu (CXO)

---

## 🎯 Başarı Metrikleri (6 Ay Hedef)

| Metrik | Baseline | 6 Ay Hedef | Ölçüm |
|--------|----------|-----------|-------|
| **Organik Trafik** | 440 oturum | 660+ | GA4 |
| **Click to Chat** | 85/yıl | 130+/yıl | GA4 Event |
| **"Beton parlatma fiyatları"** | Pozisyon 32 | Top 5 | Search Console |
| **Sayfa Hızı (Mobil LCP)** | 1,9s | <1,5s | PageSpeed |
| **NPS Skoru** | — | ≥70 | CRM Anket |
| **Lead → Kapanış** | %35 (tahmini) | %40 | CRM Pipeline |

---

## 📝 Sonraki Adımlar

1. **YK Onayı:** Bu içerik mimarisi onaylanmalı (CEO + tüm departmanlar)
2. **Mockup Güncelleme:** CDO + tasarımcı (v5.2)
3. **İçerik Üretimi Başlangıç:** Faz 1 sayfaları (CMO + CTO)
4. **Migration Planlama:** CDO teknik takvim
5. **CRM Kurulumu:** CDO + CSO (HubSpot Free)

---

**Hazırlayan:** AI Yönetim Kurulu
**Onay Bekliyor:** CEO Alexander Kaya
**Tarih:** 2026-02-25
