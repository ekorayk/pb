# Mockup Güncelleme Önerileri — v5.2

**Mevcut Mockup:** v5.1 editorial + liquid glass navbar
**Hedef Mockup:** v5.2 — İçerik mimarisi uyumlu
**Tarih:** 2026-02-25
**Sorumlu:** CDO Can Erdoğan + Tasarım Ekibi

---

## 📊 Güncelleme Gerekçesi

**Metrik Bazlı İhtiyaçlar:**
1. Click to Chat: 85 → 130+ hedefi → CTA optimizasyonu kritik
2. "Beton parlatma fiyatları" keyword (pozisyon 32) → Özel landing page gerekli
3. Referans sayfası: 68 görüntüleme → Sosyal kanıt vurgusu artırılmalı
4. 404 hatası: 112 görüntüleme → Güven kaybı → Trust signals güçlenmeli

**YK Kararları:**
- CEO: Trust badge + referans logoları öncelikli
- CMO: Sektör çözümleri bölümü eklenecek
- CSO: Lead niteleme formu optimize edilecek
- CXO: Müşteri yorumu (testimonial) vurgulanacak

---

## 🎨 Sayfa Bazlı Güncelleme Listesi

### 1️⃣ Ana Sayfa (/) — v5.2

#### A. Hero Section

**Mevcut (v5.1):**
- Genel başlık
- 1 CTA button

**Yeni (v5.2):**

**Başlıklar:**
```html
<h1>Betonunuzu Mermer Gibi Parlak ve Kalıcı Bir Yüzeye Dönüştürün</h1>
<p class="subtitle">
  15+ yıldır Türkiye'nin fabrika, depo ve ofislerinde
  beton parlatma teknolojisinin öncüsüyüz
</p>
```

**CTA Butonlar (2 Adet):**
```html
<button class="cta-primary">
  📱 WhatsApp ile Ücretsiz Keşif
</button>
<button class="cta-secondary">
  📋 Referansları İnceleyin
</button>
```

**Trust Badge Line (Hero Altında):**
```html
<div class="trust-badges">
  <span>✅ 200+ Tamamlanmış Proje</span>
  <span>✅ 15 Yıl Deneyim</span>
  <span>✅ ANSI Standartları</span>
</div>
```

**Görsel:**
- Hero background: Parlak beton zemin görseli (ayna yansıması vurgusu)
- Mobil: Before/After slider (opsiyonel)

---

#### B. Stats Panel (Liquid Glass)

**Mevcut (v5.1):**
- Genel istatistikler var ✅

**Güncelleme (v5.2):**

**4 Stat Kutusu:**
```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│   15+ Yıl       │    200+         │     ANSI        │      %100       │
│   Deneyim       │    Proje        │   A137.1        │    Müşteri      │
│                 │                 │  Sertifikalı    │  Memnuniyeti    │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

**Tasarım:**
- Liquid glass efekt korunacak ✅
- Sayılar büyük, açıklama küçük
- Hover efekti: Hafif scale up

---

#### C. Süreç (6 Adım) ⭐ YENİ BÖLÜM

**Layout:** Horizontal timeline (desktop) / Vertical accordion (mobile)

**6 Adım:**

```
1. 🔍 Zemin Analizi
   "Sertlik ve nem oranı analizi → uygun metodoloji belirlenir"

2. 🛠️ Zemin Tamirat
   "Çatlak, delik ve derz onarımı — monolitik görünüm"

3. 💎 Mekanik Silim
   "Metal bağlayıcı elmas uçlarla beton yüzey açılır"

4. 🧪 Lityum Silikat
   "Sıvı kristalizasyon — %400 aşınma direnci artışı"

5. ✨ Parlatma
   "3000 grit'e kadar kademeli rafine — ayna efekti"

6. 🛡️ Koruyucu
   "Nefes alan, sıvı geçirmez profesyonel kaplama"
```

**Tasarım:**
- Her adım: İkon (SVG) + Başlık + Kısa açıklama
- Timeline line: Gradient (gri → siyah)
- Aktif adım: Renk vurgusu

---

#### D. Avantajlar (4 Kart) — MEVCUT UPGRADE

**Mevcut (v5.1):**
- Avantaj listesi var

**Güncelleme (v5.2):**

**4 Ana Kart (Grid 2x2):**

**1. Ultra Dayanıklılık**
```
İkon: 💪
Başlık: Ultra Dayanıklılık ve Endüstriyel Sertlik
Açıklama: Lityum silikat teknolojisi ile betonun aşınma direnci
%400'e kadar artar. Mohs sertlik skalasında 7+ değer — ağır
forklift trafiğine karşı on yıllarca formunu korur.
Metrik Vurgusu: "%400 Aşınma Direnci Artışı"
```

**2. Kesin Tozumazlık**
```
İkon: 🌫️
Başlık: Maksimum Hijyen ve Kesin Tozumazlık
Açıklama: Betonun mikro gözenekleri moleküler düzeyde kapatılır.
%100 hipoalerjenik yapı — gıda tesisi, tekstil fabrikası,
hastane için ideal.
Metrik Vurgusu: "%100 Hipoalerjenik"
```

**3. Enerji Verimliliği**
```
İkon: 💡
Başlık: Işık Yansıtma ve Enerji Verimliliği
Açıklama: Ayna netliğindeki yüzey yansıması (DOI), ortamdaki
yapay aydınlatma ihtiyacını %30'a kadar azaltır. Elektrik
faturanızda fark yaratır.
Metrik Vurgusu: "%30 Aydınlatma Tasarrufu"
```

**4. Düşük Maliyet**
```
İkon: 💰
Başlık: Minimum İşletme ve Bakım Maliyeti
Açıklama: Epoksi veya diğer kaplama sistemlerine göre %60'a
varan düşük yaşam döngüsü maliyeti. Yeniden kaplama gerektirmez
— tek seferlik yatırım.
Metrik Vurgusu: "%60 Düşük Yaşam Döngüsü Maliyeti"
```

**Tasarım:**
- Kart arka plan: Hafif liquid glass efekt
- Metrik vurgusu: Büyük font, renkli (gradient)
- Hover: Kart yükselir (shadow artışı)

---

#### E. Referans Logoları ⭐ YENİ BÖLÜM

**Layout:**

```html
<section class="references">
  <h2>200+ Firma Bize Güvendi</h2>
  <p class="subtitle">
    Tekstil, gıda, otomotiv, enerji sektörlerinde lider firmalar
  </p>

  <div class="logo-grid">
    <img src="debak-logo.svg" alt="Debak Denizli" />
    <img src="garanti-iplik-logo.svg" alt="Garanti İplik" />
    <img src="tedak-logo.svg" alt="Tedak Elektrik" />
    <img src="sabiha-gokcen-logo.svg" alt="Sabiha Gökçen İSG" />
    <img src="kansai-altan-logo.svg" alt="Kansai Altan" />
    <img src="sirmersan-logo.svg" alt="Sirmersan Mermer" />
  </div>

  <button class="cta-secondary">Tüm Referansları Gör</button>
</section>
```

**Tasarım:**
- Logoları grayscale (hover'da renkli)
- Grid: 3 kolon (desktop), 2 kolon (mobile)
- Liquid glass arka plan

---

#### F. Vaka Çalışması Spotlight ⭐ YENİ BÖLÜM

**Layout:** 2 Kolon (Sol: Görsel | Sağ: İçerik)

```html
<section class="case-study">
  <div class="image">
    <img src="garanti-iplik-fabrika.jpg" alt="Garanti İplik Fabrika Zemini" />
    <span class="badge">Tekstil Sektörü</span>
  </div>

  <div class="content">
    <h3>Garanti İplik A.Ş. — Akdeniz'in Melanj İplik Lideri</h3>
    <p class="meta">2023 • Çorlu, Tekirdağ • 5.000 m²</p>

    <blockquote>
      "Tekstil üretiminde kritik olan sıfır toz standardı sağlandı.
      Işığı yansıtma verimliliği artarken, zemin ömrü endüstriyel
      bazda maksimize edildi."
    </blockquote>

    <ul class="results">
      <li>✅ %100 Tozumazlık — İplik Kalitesi Korundu</li>
      <li>✅ %30 Aydınlatma Verimliliği Artışı</li>
      <li>✅ Üretim Aksatmadan 7 Günde Tamamlandı</li>
    </ul>

    <a href="/projeler/garanti-iplik-corlu/" class="link">
      Detayları Gör →
    </a>
  </div>
</section>
```

**Tasarım:**
- Görsel: Before/After slider (opsiyonel)
- Blockquote: Büyük font, özel stil
- Mobil: Stack (görsel üstte, içerik altta)

---

#### G. Sektör Çözümleri (6 İkon Kart) ⭐ YENİ BÖLÜM

**Layout:** Grid 3x2 (desktop) / 2x3 (tablet) / 1x6 (mobile)

```html
<section class="sectors">
  <h2>Her Sektöre Özel Çözümler</h2>

  <div class="sector-grid">
    <!-- Kart 1 -->
    <a href="/sektorler/tekstil-fabrikalari/" class="sector-card">
      <div class="icon">🧵</div>
      <h3>Tekstil</h3>
      <p>Sıfır toz standardı — iplik kalitesi</p>
    </a>

    <!-- Kart 2 -->
    <a href="/sektorler/gida-tesisleri/" class="sector-card">
      <div class="icon">🍞</div>
      <h3>Gıda</h3>
      <p>FDA uyumlu hijyen — HACCP</p>
    </a>

    <!-- Kart 3 -->
    <a href="/sektorler/otomotiv-sanayi/" class="sector-card">
      <div class="icon">🚗</div>
      <h3>Otomotiv</h3>
      <p>Yağ direnci — ağır yük taşıma</p>
    </a>

    <!-- Kart 4 -->
    <a href="/sektorler/lojistik-depolari/" class="sector-card">
      <div class="icon">📦</div>
      <h3>Lojistik</h3>
      <p>Forklift trafiği — darbe dayanımı</p>
    </a>

    <!-- Kart 5 -->
    <a href="/sektorler/enerji-elektrik/" class="sector-card">
      <div class="icon">⚡</div>
      <h3>Enerji & Elektrik</h3>
      <p>ESD koruması — güvenlik standartları</p>
    </a>

    <!-- Kart 6 -->
    <a href="/sektorler/mobil-robot-fabrikalari/" class="sector-card">
      <div class="icon">🤖</div>
      <h3>Mobil Robot</h3>
      <p>Düşük sürtünme — DCOF 0.42+</p>
    </a>
  </div>
</section>
```

**Tasarım:**
- Kart: Liquid glass arka plan
- İkon: Büyük emoji veya SVG
- Hover: Kart yükselir + renk geçişi

---

#### H. Testimonial Section

**Layout:** Center-aligned blockquote

```html
<section class="testimonial">
  <blockquote>
    <p class="quote">
      "Parlak Beton uygulamasının kalitesi ve dayanıklılığı,
      8 yıl boyunca geçen sürede bile ilk günkü gibi korunmuştur."
    </p>
    <footer>
      <img src="tedak-logo.svg" alt="Tedak Elektrik" class="logo" />
      <cite>
        <strong>Tedak Elektrik</strong><br />
        2016 — Denizli
      </cite>
    </footer>
  </blockquote>

  <!-- Faz 2: Video Testimonial -->
  <div class="video-placeholder">
    <button class="play-button">▶ Video Referansı İzle</button>
  </div>
</section>
```

**Tasarım:**
- Quote: Çok büyük font (32-48px)
- Logo: Grayscale
- Arka plan: Parlak beton görseli (blurred)

---

#### I. FAQ Accordion

**6 Soru (Schema.org FAQPage):**

```html
<section class="faq">
  <h2>Sıkça Sorulan Sorular</h2>

  <details>
    <summary>Beton parlatma fiyatları neye göre belirlenir?</summary>
    <p>
      Fiyat; metrekare, zeminin mevcut durumu (çatlak/boşluk miktarı),
      agrega görünüm derecesi, parlaklık seviyesi ve proje lokasyonuna
      göre değişir. Ücretsiz keşiften sonra garantili fiyat teklifi sunuyoruz.
    </p>
  </details>

  <details>
    <summary>Parlatılmış beton zeminler kaygan mıdır?</summary>
    <p>
      Hayır. ANSI A137.1 ve NFSI standartlarında yüksek sürtünme katsayısı
      (DCOF 0.42+) ile ıslak ve kuru koşullarda güvenlidir. Birçok kaplama
      türünden daha güvenlidir.
    </p>
  </details>

  <details>
    <summary>Epoksiden ne farkı var?</summary>
    <p>
      Beton parlatma mekanik süreç — kaplama değil. Yeniden uygulama
      gerektirmez, yaşam döngüsü maliyeti %60 düşüktür. Epoksi 5-7 yılda
      yenilenir, parlak beton kalıcıdır.
    </p>
  </details>

  <details>
    <summary>Uygulama ne kadar sürer?</summary>
    <p>
      Alan büyüklüğüne göre 2-7 gün. 1.000 m² standart fabrika zemini
      ortalama 3-4 iş günü. Üretimi aksatmayan aşamalı uygulama mümkün.
    </p>
  </details>

  <details>
    <summary>Beton parlatma kalıcı mıdır?</summary>
    <p>
      Evet. Lityum silikat moleküler düzeyde beton ile birleşir.
      Referanslarımızdan Tedak Elektrik 8 yıl, Debak Denizli 6 yıl
      sonra hala ilk günkü parlaklıkta.
    </p>
  </details>

  <details>
    <summary>Hangi sektörlere uygundur?</summary>
    <p>
      Fabrika, depo, AVM, ofis, hastane, gıda tesisi, tekstil, otomotiv,
      enerji, lojistik — her sektöre uygun. Özellikle ağır trafik ve
      hijyen gerekliliği olan alanlarda ideal.
    </p>
  </details>
</section>
```

**Tasarım:**
- Accordion: Liquid glass arka plan
- Açık soru: Siyah arka plan + beyaz metin
- Kapalı soru: Beyaz arka plan + siyah metin
- İkon: + (kapalı) / - (açık)

---

#### J. CTA Section (Final)

**Layout:** Full-width hero + inline form

```html
<section class="final-cta">
  <h2>Zeminizi Ücretsiz Değerlendirmemize İzin Verin</h2>
  <p class="subtitle">
    24 saat içinde size ulaşıyor, ihtiyaçlarınızı analiz ediyoruz
  </p>

  <div class="cta-options">
    <!-- WhatsApp (Öncelikli) -->
    <a href="https://wa.me/905072185318?text=..." class="whatsapp-cta">
      <img src="whatsapp-icon.svg" alt="WhatsApp" />
      <span>WhatsApp ile Hızlı İletişim</span>
      <small>Ortalama yanıt süresi: 2 saat</small>
    </a>

    <!-- Form (Inline) -->
    <form class="contact-form">
      <input type="text" placeholder="İsim Soyisim *" required />
      <input type="tel" placeholder="Telefon *" required />
      <input type="text" placeholder="Proje Lokasyonu (İl) *" required />
      <select required>
        <option>Tahmini Alan (m²) *</option>
        <option>500 m² altı</option>
        <option>500-1.000 m²</option>
        <option>1.000-3.000 m²</option>
        <option>3.000+ m²</option>
      </select>
      <button type="submit" class="cta-primary">
        Ücretsiz Keşif Talep Et
      </button>
      <label class="kvkk">
        <input type="checkbox" required />
        <a href="/gizlilik-politikasi/">KVKK Aydınlatma Metni</a>'ni okudum, onaylıyorum.
      </label>
    </form>
  </div>
</section>
```

**Tasarım:**
- Arka plan: Parlak beton görseli (gradient overlay)
- WhatsApp CTA: Yeşil (#25D366) — büyük buton
- Form: Beyaz arka plan, liquid glass border
- Mobil: Stack (WhatsApp üstte, form altta)

---

#### K. Footer

**Layout:** 4 Kolon (desktop) / Accordion (mobile)

```html
<footer>
  <div class="footer-grid">
    <!-- Kolon 1: Firma Bilgisi -->
    <div class="footer-col">
      <img src="logo.svg" alt="Parlak Beton" class="footer-logo" />
      <p class="slogan">Betonun parlak yüzünü keşfedin</p>
      <p class="contact">
        📞 +90 507 218 5318<br />
        📧 info@parlakbeton.com
      </p>
      <div class="social">
        <!-- Sosyal medya ikonları (varsa) -->
      </div>
    </div>

    <!-- Kolon 2: Hizmetler -->
    <div class="footer-col">
      <h4>Hizmetler</h4>
      <ul>
        <li><a href="/hizmetler/beton-parlatma/">Beton Parlatma</a></li>
        <li><a href="/hizmetler/beton-parlatma/fiyatlari/">Fiyatlar</a></li>
        <li><a href="/hizmetler/lityum-silikat/">Lityum Silikat</a></li>
        <li><a href="/hizmetler/zemin-tamirat/">Zemin Tamirat</a></li>
      </ul>
    </div>

    <!-- Kolon 3: Sektörler -->
    <div class="footer-col">
      <h4>Sektörler</h4>
      <ul>
        <li><a href="/sektorler/tekstil-fabrikalari/">Tekstil</a></li>
        <li><a href="/sektorler/gida-tesisleri/">Gıda</a></li>
        <li><a href="/sektorler/otomotiv-sanayi/">Otomotiv</a></li>
        <li><a href="/sektorler/lojistik-depolari/">Lojistik</a></li>
        <li><a href="/sektorler/mobil-robot-fabrikalari/">Mobil Robot</a></li>
      </ul>
    </div>

    <!-- Kolon 4: Şirket -->
    <div class="footer-col">
      <h4>Şirket</h4>
      <ul>
        <li><a href="/hakkimizda/">Hakkımızda</a></li>
        <li><a href="/projeler/">Referanslar</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/iletisim/">İletişim</a></li>
        <li><a href="/gizlilik-politikasi/">Gizlilik Politikası</a></li>
        <li><a href="/kvkk/">KVKK</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-bottom">
    <p>
      © 2026 Parlak Beton Zemin Teknolojileri San. ve Tic. A.Ş.
      Tüm hakları saklıdır.
    </p>
  </div>
</footer>
```

**Tasarım:**
- Arka plan: Siyah (#0C0C0A)
- Metin: Gri (#B0A898)
- Link hover: Beyaz (#FAFAF8)
- Footer logo: Beyaz versiyonu

---

### 2️⃣ Beton Parlatma Fiyatları Landing Page ⭐ YENİ SAYFA

**URL:** `/hizmetler/beton-parlatma/fiyatlari/`

#### Mockup Gereksinimleri:

**Hero:**
- H1: "Beton Parlatma Fiyatları 2026"
- Alt başlık: "Fiyat nasıl belirlenir? Şeffaf bilgilendirme."
- Breadcrumb: Ana Sayfa > Hizmetler > Beton Parlatma > Fiyatları

**5 Faktör Kartları:**
- İkon + Başlık + Açıklama + Görsel
- Grid: 1x5 (desktop scroll) / 1x5 (mobile stack)

**Fiyat Aralığı Tablosu:**
- Responsive tablo
- 3 satır (farklı alan aralıkları)
- 4 kolon: Alan | Zemin Durumu | Parlaklık | Fiyat Aralığı

**"Neden Sabit Fiyat Yok?" Box:**
- Açıklama + CTA: "Ücretsiz Keşif Talep Et"

**TCO Karşılaştırma Grafiği:**
- 10 yıllık maliyet çubuğu grafiği
- Beton Parlatma vs. Epoksi
- Kriterler: İlk Yatırım + Bakım + Yenileme

**CTA:**
- Form (inline) + WhatsApp

**FAQ (Fiyat odaklı — 5 soru):**
- Accordion

---

### 3️⃣ İletişim Sayfası (/iletisim/)

#### Mockup Gereksinimleri:

**Hero:**
- H1: "Zeminizi Ücretsiz Değerlendirmemize İzin Verin"
- Alt başlık: "24 saat içinde yanıt veriyoruz"

**3 İletişim Kanalı (Kutucuklar):**

```
┌─────────────┬─────────────┬─────────────┐
│  WhatsApp   │   Telefon   │   E-posta   │
│  (Öncelik)  │             │             │
│             │             │             │
│  QR Kod     │ 0507 218... │ info@...    │
│  + Link     │ 09:00-18:00 │             │
└─────────────┴─────────────┴─────────────┘
```

**Ücretsiz Keşif Formu:**
- 8 alan (yukarıda detaylı)
- KVKK checkbox + link

**Google Maps** (Opsiyonel — adres varsa)

**FAQ (İletişim odaklı — 3 soru):**
- "Keşif ne kadar sürer?"
- "Keşif ücretli mi?"
- "Teklif ne kadar sürede hazırlanır?"

---

### 4️⃣ Projeler (Referanslar) Sayfası (/projeler/)

#### Mockup Gereksinimleri:

**Hero:**
- H1: "200+ Tamamlanmış Beton Parlatma Projesi"
- Alt başlık: "Türkiye'nin her yerinde güvenilir çözüm ortağınız"

**Filtreler (Horizontal Pills):**
```html
<div class="filters">
  <button class="active">Tümü</button>
  <button>Tekstil</button>
  <button>Gıda</button>
  <button>Otomotiv</button>
  <button>Enerji</button>
  <button>Lojistik</button>
</div>
```

**Proje Kartları (Grid 3 kolon):**
```
┌────────────────────────────────┐
│  [Firma Logosu]                │
│                                │
│  Garanti İplik A.Ş.            │
│  Tekstil • 2023                │
│                                │
│  "8 yıldır ilk günkü gibi"     │
│                                │
│  [Detayları Gör →]             │
└────────────────────────────────┘
```

**Öne Çıkan 3 Vaka (Büyük Kartlar):**
- Görsel + İçerik (2 kolon)
- Müşteri yorumu (blockquote)
- CTA: "Detayları Gör"

**Video Testimonial Placeholder** (Faz 2)

---

### 5️⃣ Hakkımızda Sayfası (/hakkimizda/)

#### Mockup Gereksinimleri:

**Hero:**
- H1: "Betonun Parlak Yüzünü Keşfetmenize Yardımcı Oluyoruz"
- Görsel: Ekip fotoğrafı veya fabrika

**Firma Hikayesi (Timeline):**
```
2009 ──────► 2015 ──────► 2020 ──────► 2024
Kuruluş    Lityum      100. Proje   200+ Proje
           Teknolojisi
```

**Değerlerimiz (4 Kart — Grid 2x2):**
- Teknik Mükemmellik
- Müşteri Odaklılık
- Sürdürülebilirlik
- Şeffaflık

**Sayılarla Parlak Beton (Stats):**
- 15+ Yıl • 200+ Proje • 6 Sektör • %100 Memnuniyet

**Sertifikalar (Logo Grid):**
- ANSI A137.1
- NFSI
- ISO (varsa)

---

## 🎨 Tasarım Sistemi Güncellemeleri

### Renk Paleti (Mevcut Korunacak)

```css
:root {
  --white: #FAFAF8;
  --black: #0C0C0A;
  --grey: #B0A898;
  --grey-l: #E8E4DE;
  --grey-d: #3A3830;

  /* Yeni Aksan Renkler */
  --accent-green: #25D366; /* WhatsApp */
  --accent-blue: #2563EB;  /* Link hover */
  --accent-gold: #D4AF37;  /* Premium vurgu */
}
```

### Tipografi

```css
/* Başlıklar */
h1 { font-size: 48px; font-weight: 700; line-height: 1.1; }
h2 { font-size: 36px; font-weight: 600; line-height: 1.2; }
h3 { font-size: 24px; font-weight: 600; line-height: 1.3; }

/* Mobil */
@media (max-width: 768px) {
  h1 { font-size: 32px; }
  h2 { font-size: 24px; }
  h3 { font-size: 20px; }
}
```

### Liquid Glass Efekt (Mevcut Korunacak ✅)

```css
.liquid-glass {
  background: rgba(255, 255, 255, .08);
  backdrop-filter: blur(48px) saturate(200%) brightness(1.05);
  border: 1px solid rgba(255, 255, 255, .18);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, .12),
    inset 0 1px 0 rgba(255, 255, 255, .35);
}
```

### CTA Buton Stilleri

```css
/* Primary CTA (WhatsApp, Form Submit) */
.cta-primary {
  background: linear-gradient(135deg, var(--black), var(--grey-d));
  color: var(--white);
  padding: 16px 32px;
  border-radius: 100px;
  font-weight: 600;
  transition: all .3s var(--ease);
}

.cta-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, .2);
}

/* Secondary CTA (Referanslar, Detaylar) */
.cta-secondary {
  background: transparent;
  color: var(--black);
  border: 1px solid var(--grey);
  padding: 16px 32px;
  border-radius: 100px;
}

.cta-secondary:hover {
  background: var(--black);
  color: var(--white);
  border-color: var(--black);
}

/* WhatsApp CTA */
.whatsapp-cta {
  background: linear-gradient(135deg, #25D366, #128C7E);
  color: white;
  /* ... */
}
```

### Kart Stilleri

```css
.card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 32px;
  transition: all .3s var(--ease);
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 24px 48px rgba(0, 0, 0, .12);
  border-color: var(--black);
}

/* Liquid Glass Card Variant */
.card-glass {
  background: rgba(255, 255, 255, .08);
  backdrop-filter: blur(48px);
  border: 1px solid rgba(255, 255, 255, .18);
}
```

---

## 📱 Responsive Breakpoints

```css
/* Mobile First */
@media (min-width: 640px)  { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large Desktop */ }
```

**Kritik Responsive Noktalar:**

1. **Hero CTA Butonlar:**
   - Desktop: Horizontal (yan yana)
   - Mobile: Vertical (stack)

2. **Stats Panel:**
   - Desktop: 4 kolon
   - Tablet: 2x2 grid
   - Mobile: 1x4 stack

3. **Süreç Timeline:**
   - Desktop: Horizontal
   - Mobile: Vertical accordion

4. **Avantajlar Kartları:**
   - Desktop: 2x2 grid
   - Tablet: 2x2 grid
   - Mobile: 1x4 stack

5. **Sektör Kartları:**
   - Desktop: 3x2 grid
   - Tablet: 2x3 grid
   - Mobile: 1x6 stack

6. **Footer:**
   - Desktop: 4 kolon
   - Mobile: Accordion

---

## ✅ Mockup Checklist

### Genel
- [ ] Liquid glass navbar korundu ✅
- [ ] Renk paleti tutarlı (v5.1 ile)
- [ ] DM Sans font ailesi
- [ ] Noise texture arka plan
- [ ] Responsive: 320px → 1920px

### Ana Sayfa Bölümleri
- [ ] Hero: Başlık + 2 CTA + Trust badge
- [ ] Stats Panel: 4 stat (liquid glass)
- [ ] Süreç: 6 adım timeline/accordion
- [ ] Avantajlar: 4 kart (metrik vurgusu)
- [ ] Referans Logoları: 6+ logo
- [ ] Vaka Çalışması: Garanti İplik spotlight
- [ ] Sektör Çözümleri: 6 ikon kart
- [ ] Testimonial: Tedak yorumu
- [ ] FAQ: 6 soru accordion
- [ ] CTA Final: Form + WhatsApp
- [ ] Footer: 4 kolon

### Yeni Sayfalar
- [ ] Fiyatlar Landing: 5 faktör + tablo + TCO
- [ ] İletişim: 3 kanal + form + FAQ
- [ ] Projeler: Filtreler + grid + spotlight
- [ ] Hakkımızda: Timeline + değerler + stats

### Performans
- [ ] Görseller WebP format
- [ ] Lazy loading (hero hariç)
- [ ] Alt tag tüm görsellerde
- [ ] Icon set optimize (SVG)

---

## 📦 Mockup Teslim Dosyaları

**Beklenen Çıktılar:**

1. **HTML Mockup (v5.2-editorial.html)**
   - Ana sayfa tam
   - Tüm bölümler interaktif
   - Responsive test edilmiş

2. **Asset Klasörü (/mockup-assets/)**
   - Logo (SVG + PNG)
   - İkonlar (SVG)
   - Placeholder görseller
   - Referans firma logoları

3. **CSS Dosyası (v5.2-styles.css)**
   - Design tokens
   - Component styles
   - Responsive breakpoints

4. **Diğer Sayfa Mockupları (Opsiyonel):**
   - `v5.2-fiyatlar.html`
   - `v5.2-iletisim.html`
   - `v5.2-projeler.html`

---

## 🎯 Sonraki Adımlar

1. **CDO Can:** Mockup v5.2 geliştirme başlatır
2. **CMO Serena:** İçerik üretimi (kopyalar, başlıklar, açıklamalar)
3. **CTO Emre:** Teknik içerik (lityum silikat, DCOF açıklamaları)
4. **Tasarımcı:** Görsel asset üretimi (ikonlar, placeholder görseller)
5. **YK Toplantısı:** Mockup v5.2 onay (1 hafta sonra)

---

**Hazırlayan:** CDO Can Erdoğan + AI Yönetim Kurulu
**Onay Bekliyor:** CEO Alexander Kaya + CMO Serena Öztürk
**Hedef Teslim:** 2026-03-03 (7 gün)
