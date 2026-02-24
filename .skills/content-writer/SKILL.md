---
name: content-writer
description: Parlak Beton A.Ş. için SEO uyumlu, teknik otorite yansıtan Türkçe web içeriği üretir.
---

# Content Writer Skill

## Ne Zaman Kullanılır?

- Yeni sayfa içeriği yazılacağında
- Blog / makale üretiminde
- Mevcut içerik yenilenecekken

## Yazım Kuralları

### Ton & Ses

- **Otorite:** Teknik bilgiyi sade Türkçe ile sun — jargon açıkla
- **Güven:** Veri ve standartlarla destekle (ANSI, NFSI, Mohs, DCOF)
- **Aktif:** "yapılır" değil "yapıyoruz / sağlar / sunar"
- **Sıcaklık:** Müşteri odaklı — problemi, sonra çözümü anlat

### SEO Yapısı

```
H1: [Ana anahtar kelime] — sayfa başına 1 adet
H2: Alt kategoriler — 2-4 arası
H3: Detay başlıkları
```

- **Başlık:** 50-60 karakter | Anahtar kelime öne yakın
- **Meta description:** 150-160 karakter | CTA içermeli
- **İlk paragraf:** Anahtar kelimeyi ilk 100 kelimede kullan
- **İç link:** Her sayfada en az 2 iç bağlantı
- **CTA:** Her bölüm sonunda yumuşak CTA ("Ücretsiz Keşif İsteyin")

### İçerik Yapısı (Sayfa Şablonu)

```
1. Hero H1 + güçlü alt başlık
2. Özet paragraf (problemi tanımla)
3. Hizmetin nasıl çalıştığı (süreç adımları)
4. Avantajlar (madde listesi + veri)
5. Kimler için? (hedef kitle)
6. Referans/sosyal kanıt
7. SSS (FAQPage schema ile)
8. CTA blok ("Ücretsiz Keşif")
```

### Anahtar Kelime Entegrasyon Yoğunluğu

- Ana kelime: %1-2 (zorlama — doğal)
- LSI (ilişkili) kelimeler: Sayfaya organik dağıt
- Kaynak: `.agent/context/seo.md`

### Yapısal Veriler (Her İçerik Üretiminde Kontrol Et)

- **Ana Sayfa:** `LocalBusiness` + `WebSite`
- **Hizmet Sayfaları:** `Service` + `LocalBusiness`
- **SSS Bölümü:** `FAQPage` (mevcut sitede var — koru/genişlet)
- **Referans Sayfaları:** `Review` + `Organization`

## Örnek SSS Bloğu (Kullanıma Hazır)

```astro
---
const faqs = [
  {
    q: "Beton parlatma fiyatları neye göre belirlenir?",
    a: "Fiyatlandırma; metrekare, zeminin mevcut durumu, agrega görünüm derecesi ve parlaklık seviyesine göre değişir. Ücretsiz keşif sonrası doğru maliyet analizi yapılır."
  },
  {
    q: "Parlatılmış beton zeminler kaygan mıdır?",
    a: "Hayır. ANSI A137.1 ve NFSI standartlarına göre test edilen yüzeyler, ıslak ve kuru koşullarda 0.42+ DCOF değeriyle güvenli kaymazlık sağlar."
  }
]
---
```
